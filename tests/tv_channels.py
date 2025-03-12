import allure
import pytest
import os
from dotenv import load_dotenv
from utils.compare_picture import compare_screenshot
from utils.make_storage_picture import make_screenshot
from utils.receive_response import check_response
from static.test_uuid import TVchannels
from utils.app_logger import get_logger
from utils.utils_func import compare_two_string, compare_two_digital, make_rounded_required_size
# from conftest import test_ops


logger = get_logger(__name__)

load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")


@allure.story('ТВ каналы - height=72')
@allure.label('owner', "s.rybak@okko.tv")
class TestTvChannels:
    @pytest.mark.parametrize("preset", TVchannels.tv_presets.value)
    @pytest.mark.parametrize("tv_channel_uuid", TVchannels.tv_channel.value)
    @allure.title("{tv_channel_uuid} - {preset}")
    @allure.issue("DEV-129400", name="DEV-129400")
    # @allure.link("195053")
    # @allure.link("194912")
    # @allure.link("195049")
    def test_tv_preset(self, image_snapshot, preset, tv_channel_uuid):
        logger.info("TV channel uuid: %s", tv_channel_uuid)
        height = 72

        query_tail = f"presetId={preset}&clienttype=tv&mediatype=png&height={height}"
        response_height = make_rounded_required_size(height, 'height')
        query_im = f"clienttype=tv&height={response_height}&mediatype=png&presetid={preset}"

        image_manager_url = f"{host_url}{tv_channel_uuid}?{query_im}"
        logger.info("IM url: %s", image_manager_url)
        response_im = check_response(image_manager_url)

        name_screenshot = f"{preset}_{tv_channel_uuid}"
        img_width, img_height = make_screenshot(response_im, img_uuid=name_screenshot)

        stat_img_url = f"{static_url}{tv_channel_uuid}?{query_tail}"
        logger.info("static url: %s", stat_img_url)
        response_static = check_response(stat_img_url, timeout=10)

        if not compare_two_digital(response_height, img_width, "HEIGHT"):
            pytest.fail("Different HEIGHT")
        compare_two_string(response_im.headers.get('etag'), response_static.headers.get('etag'), "ETAG")
        compare_screenshot(response_static, image_snapshot, img_uuid=name_screenshot)

    if __name__ == "__main__":
        test_tv_preset()
