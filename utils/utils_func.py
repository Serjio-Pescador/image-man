import allure
import pytest
from urllib.parse import parse_qs
import urllib
from pathlib import Path
from utils.app_logger import get_logger

logger = get_logger(__name__)


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def maker_of_test_data(data_source):
    all_values = []
    all_keys = []
    for data in data_source:
        all_values += data.value
        all_keys += [data.name.split('_')[-1]] * len(data.value)
    return list(tuple(zip(all_keys, all_values)))


def make_new_url_tail_rounded_width(base_tail: str) -> tuple[str, int]:
    query_params = parse_qs(base_tail)
    width: int = int(query_params['width'][0])
    new_width: int = 1
    if width < 10:
        new_width = 10
    elif width < 100:
        new_width = width // 10 + 9
    elif width % 10 == 0:
        new_width = width
    elif 99 >= width % 100 > 80:
        new_width = width // 100 * 100 + 99
    elif width % 20 != 0:
        new_width = width + 20 - (width % 20)

    logger.info("Required width: %s", new_width)
    # assert new_width % 10 == 0

    eql_query_im = query_params.copy()
    eql_query_im['width'] = [str(new_width)]

    query_tail_im = ("&".join(f'{k}={v[0]}' for k, v in eql_query_im.items()))
    return query_tail_im, new_width


def make_rounded_required_size(param: int, name: str) -> int:
    new_param: int = 1
    if param < 10:
        new_param = 10
    elif param < 100:
        new_param = param // 10 + 9
    elif param % 10 == 0:
        new_param = param
    elif 99 >= param % 100 > 80:
        new_param = param // 100 * 100 + 99
    elif param % 20 != 0:
        new_param = param + 20 - (param % 20)

    logger.info("Required {name} in IM: %s", new_param)
    return new_param


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def remove_suffix(text, suffix):
    if suffix and text.endswith(suffix):
        return text[:-len(suffix)]
    return text


def allure_attach_image(src_path, img_uuid, suffix: str = ''):
    try:
        allure.attach.file(
            str(src_path.replace('.png', f'{suffix}.png')),
            name=img_uuid + f'{suffix}.png',
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception as e:
        logger.error("The snapshot not found in screenshots.")
        # logging.exception("%s", e)
    return


def compare_two_digital(from_request: int, from_image: int, name: str) -> bool:
    try:
        # Допустимое расхождение размеров 1 пиксель
        assert abs(from_request - from_image) <= 1, f" Different {name} of image!"
    except AssertionError:
        with allure.step("Different {}! {} != {}".format(name, from_request, from_image)):
            logger.error("Different %s! %s != %s", name, from_request, from_image)
            pytest.fail("Different {} of image!".format(name))
    else:
        with allure.step("{} изображения. {} == {}".format(name, from_request, from_image)):
            logger.info("Equal %s! %s == %s", name, from_request, from_image)
    finally:
        if from_request is not None:
            return from_request == from_image
        else:
            return True


def compare_two_string(first_str: str, second_str: int, name: str) -> bool:
    try:
        assert first_str == second_str, f"Different {name} of image!"
    except AssertionError:
        with allure.step("Different {}! {} != {}".format(name, first_str, second_str)):
            logger.warning("Different %s! %s != %s", name, first_str, second_str)
            pytest.fail("Different {} of image!".format(name))
    else:
        with allure.step("Equal {}! {} == {}".format(name, first_str, second_str)):
            logger.info("Equal %s. %s == %s", name, first_str, second_str)
    finally:
        return first_str == second_str


def make_url_tail_in_alphabet_lower(base_url: str) -> str:
    if base_url.find("?") != -1:
        url_path, tail = base_url.split("?")
    else:
        url_path = ''
        tail = base_url
    query_params = parse_qs(tail.lower())
    sorted_keys = dict()
    for key in sorted(query_params):
        sorted_keys[key] = sorted(query_params[key])
    new_tail = urllib.parse.urlencode(sorted_keys, doseq=True)
    if url_path:
        final_url = url_path + '?' + new_tail
    elif not query_params:
        final_url = base_url
    else:
        final_url = new_tail
    return final_url
