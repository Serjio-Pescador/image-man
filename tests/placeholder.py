import allure
import pytest
import os
from dotenv import load_dotenv
from utils import make_screenshot, compare_screenshot
from utils import maker_of_test_data
from utils import check_response
from static.test_uuid import PlaceholderPresets

load_dotenv()

host_url = os.getenv("HOST")

data = maker_of_test_data(PlaceholderPresets)

@allure.story('Плейсхолдеры имен')
class TestPlaceholders:
    @allure.title('Плейсхолдеры инициалов')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_placeholder_preset(self, page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(120000)
        query_tail = f"presetId={preset}&width=720"

        image_manager_url = f"{host_url}{review_uuid}?{query_tail}"

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        # make_screenshot(page, img_uuid=review_uuid)
        compare_screenshot(page, image_snapshot, img_uuid=review_uuid, diff=0.05, src_path='./static/layouts/')