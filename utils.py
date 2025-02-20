import logging
import os

import allure
from PIL import Image
from io import BytesIO
from urllib.parse import parse_qs
import pytest, time
from playwright.sync_api import Page
from pathlib import Path

def make_screenshot(self, img_uuid, timeout: float = 2000, **kwargs):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-1].split('[')[0]
    self.screenshot(path=f"./screenshots/{test_name}_{img_uuid}.png", timeout=timeout, **kwargs)
    return


def compare_screenshot(self, image_snapshot, img_uuid, timeout: float = 2000, diff: float = 0.5, **kwargs):
    if kwargs:
        path = kwargs['src_path']
    else:
        path = './screenshots/'
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-1].split('[')[0]
    screenshot = Image.open(BytesIO(self.screenshot(timeout=timeout)))

    try:
        allure.attach.file(
            str(f"{path}{test_name}_{img_uuid}.png"),
            name=f"{test_name}_{img_uuid}.png",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception as e:
        # logging.exception("%s", e)
        make_screenshot(self, img_uuid=f"{path}{test_name}_{img_uuid}.png", timeout=timeout)
        logging.info("The snapshot not found in screenshots.")

    try:
        image_snapshot(screenshot, f"{path}{test_name}_{img_uuid}.png", diff)
    except Exception as e:
        # logging.error("Image does not match the snapshot stored in screenshots.", e)
        logging.error("Image does not match the snapshot stored in screenshots.")
        allure.attach.file(
            str(f"{path}{test_name}_{img_uuid}.new.png"),
            name=f"{test_name}_{img_uuid}.new.png",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach.file(
            str(f"{path}{test_name}_{img_uuid}.diff.png"),
            name=f"{test_name}_{img_uuid}.diff.png",
            attachment_type=allure.attachment_type.PNG,
        )
        pytest.fail("Image does not match the snapshot stored in screenshots.", e)
    return


def maker_of_test_data(data_source):
    all_values = []
    all_keys = []
    for data in (data_source):
        all_values += data.value
        all_keys += [data.name.split('_')[-1]] * len(data.value)
    return list(tuple(zip(all_keys, all_values)))


def make_new_url_tail_rounded_width(base_tail: str) -> str:
    query_params = parse_qs(base_tail)
    width: int = int(query_params['width'][0])

    if width % 10 == 0:
        new_width = width
    elif width % 20 != 0:
        new_width = width + 20 - (width % 20)
    logging.info("Asked width: %s", new_width)
    assert new_width % 10 == 0

    eql_query_IM = query_params.copy()
    eql_query_IM['width'] = [str(new_width)]

    query_tail_im = ("&".join(f'{k}={v[0]}' for k, v in eql_query_IM.items()))
    return query_tail_im


def check_response(response):
    if response.status == 404:
        logging.warning("404, Image not found.")
        pytest.skip("Image not found")
    if response.status == 403:
        pytest.xfail("403, Access denied")
    elif response.status == 429 or response.status == 500:
        time.sleep(2)
    return response.status


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def remove_suffix(text, suffix):
    if suffix and text.endswith(suffix):
        return text[:-len(suffix)]
    return text