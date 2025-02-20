import allure
import pytest
import os
from dotenv import load_dotenv
import logging
from playwright.sync_api import Page
from utils import make_screenshot, compare_screenshot
from utils import maker_of_test_data, make_new_url_tail_rounded_width
from utils import check_response
from static.test_uuid import TVchannels

load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")


@allure.story('ТВ каналы')
class TestTvChannels:

    @allure.title('72 высота')
    @pytest.mark.parametrize("preset", TVchannels.tv_presets.value)
    @pytest.mark.parametrize("tv_channel_uuid", TVchannels.tv_channel.value)
    def test_tv_preset(self, page: Page, image_snapshot, preset, tv_channel_uuid):
        page.set_default_timeout(90000)
        logging.info("TV channel uuid: %s", tv_channel_uuid)

        query_tail = (f"presetId={preset}&clienttype=tv&mediatype=png&height=72")
        querries_im = (f"clienttype=tv&height=79&mediatype=png&presetid={preset}")

        image_manager_url = f"{host_url}{tv_channel_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{tv_channel_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        name_screenshot = f"{preset}_{tv_channel_uuid}"
        make_screenshot(page, img_uuid=name_screenshot)

        response = page.goto(stat_img_url)
        page.wait_for_load_state('domcontentloaded')
        while check_response(response) != 200:
            response = page.goto(stat_img_url)
            page.wait_for_load_state('domcontentloaded')
        assert response.ok

        compare_screenshot(page, image_snapshot, img_uuid=name_screenshot, timeout=3000)
