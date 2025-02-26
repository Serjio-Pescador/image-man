from typing import Tuple

import allure
import pytest
from urllib.parse import parse_qs
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
    if width % 10 == 0:
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


def compare_two_digital(from_request: int, from_image: int, name: str):
    if from_request:
        # if from_request != from_image:
        # Допустимое расхождение размеров 1 пиксель
        if abs(from_request - from_image) > 1:
            logger.error("Different %s! %s != %s", name, from_request, from_image)
            pytest.fail(f" Different {name} of image! ")
    return None


def compare_two_string(first_str: str, second_str: int, name: str) -> str:
    if first_str != second_str:
        logger.warning("different %s! %s != %s", name, first_str, second_str)
    else:
        logger.info("Equal %s. %s == %s", name, first_str, second_str)
    return f"Equal %s is %s.".format(name, first_str == second_str)
