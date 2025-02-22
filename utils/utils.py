import logging
import os
import allure
from PIL import Image
import io
from urllib.parse import parse_qs
import pytest, time
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def make_screenshot(self, img_uuid,
                    src_path: str = 'screenshots/',
                    required_width: int = None,
                    required_height: int = None,
                    **kwargs):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-1].split('[')[0]

    folder = os.path.join(get_project_root(), src_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    rel_path = f"{test_name}_{img_uuid}.png"
    abs_file_path = os.path.join(folder, rel_path)

    img_obj = Image.open(io.BytesIO(self.content))
    img_obj.save(abs_file_path)

    image_manager_img_width, image_manager_img_height = img_obj.size
    logging.info("image_manager_img_width=%s, image_manager_img_height=%s", image_manager_img_width,
                 image_manager_img_height)

    allure_attach_image(abs_file_path, rel_path)
    compare_two_digital(required_width, image_manager_img_width, "WIDTH")
    compare_two_digital(required_height, image_manager_img_height, "HEIGHT")

    return


def compare_screenshot(self, image_snapshot, img_uuid, diff: float = 0.5,
                       src_path: str = 'screenshots/',
                       required_width: int = None,
                       required_height: int = None,
                       **kwargs):
    for key in ('src_path', 'required_width', 'required_height', 'timeout'):
        if key in kwargs:
            setattr(self, key, kwargs[key])

    test_name = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-1].split('[')[0]

    folder = os.path.join(get_project_root(), src_path)
    rel_path = f"{test_name}_{img_uuid}.png"
    abs_file_path = os.path.join(folder, rel_path)

    picture = Image.open(io.BytesIO(self.content))

    try:
        image_snapshot(picture, f"{abs_file_path}", diff)
    except Exception as e:
        # logging.error("Image does not match the snapshot stored in screenshots.", e)
        logging.error("Image does not match the snapshot stored in screenshots.")
        allure.attach.file(
            str(f"{abs_file_path.replace('.png','.new.png')}"),
            name=f"{test_name}_{img_uuid}.new.png",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach.file(
            str(f"{abs_file_path.replace('.png', '.diff.png')}"),
            name=f"{test_name}_{img_uuid}.diff.png",
            attachment_type=allure.attachment_type.PNG,
        )
        pytest.fail("Image does not match the snapshot stored in screenshots.", e)

    static_img_width, static_img_height = picture.size
    logging.info("static_img_width=%s, static_img_height=%s", static_img_width, static_img_height)

    compare_two_digital(required_width, static_img_width, "width")
    compare_two_digital(required_height, static_img_height, "height")
    return


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

    logging.info("Required width: %s", new_width)
    # assert new_width % 10 == 0

    eql_query_im = query_params.copy()
    eql_query_im['width'] = [str(new_width)]

    query_tail_im = ("&".join(f'{k}={v[0]}' for k, v in eql_query_im.items()))
    return query_tail_im, new_width


def check_response(response):
    if response.status_code == 404:
        logging.warning("404, Image not found.")
        pytest.skip(" -> Image not found <- ")
    if response.status_code == 403:
        pytest.xfail(" XXX 403, Access denied XXX ")
    elif response.status_code == 429 or response.status_code == 500:
        time.sleep(2)
    return response.status_code


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
            str(src_path),
            name=img_uuid,
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception as e:
        logging.warning("The snapshot not found in screenshots.")
        # logging.exception("%s", e)
    return


def compare_two_digital(from_request: int, from_image: int, name: str):
    if from_request:
        # if from_request != from_image:
        # Допустимое расхождение размеров 1 пиксель
        if abs(from_request - from_image) >= 1:
            logging.error("Different %s! %s != %s", name, from_request, from_image)
            pytest.fail(f" Different {name} of image! ")
    return None
