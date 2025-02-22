import allure
import pytest
import os
from dotenv import load_dotenv
import logging
from utils.utils import make_screenshot, compare_screenshot
from utils.receive_ok_response import check_response
from static.test_uuid import TVchannels

load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")


@allure.story('ТВ каналы - height=72')
class TestTvChannels:

    @pytest.mark.parametrize("preset", TVchannels.tv_presets.value)
    @pytest.mark.parametrize("tv_channel_uuid", TVchannels.tv_channel.value)
    @allure.title("{tv_channel_uuid} - {preset}")
    def test_tv_preset(self, image_snapshot, preset, tv_channel_uuid):

        logging.info("TV channel uuid: %s", tv_channel_uuid)

        query_tail = (f"presetId={preset}&clienttype=tv&mediatype=png&height=72")
        query_im = (f"clienttype=tv&height=79&mediatype=png&presetid={preset}")

        image_manager_url = f"{host_url}{tv_channel_uuid}?{query_im}"
        stat_img_url = f"{static_url}{tv_channel_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

        response = check_response(image_manager_url)
        name_screenshot = f"{preset}_{tv_channel_uuid}"

        make_screenshot(response, img_uuid=name_screenshot)

        response_stat = check_response(stat_img_url)
        compare_screenshot(response_stat, image_snapshot, img_uuid=name_screenshot)
