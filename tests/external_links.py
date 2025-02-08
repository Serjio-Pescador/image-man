import allure
import pytest
import os
import datetime
from dotenv import load_dotenv
from utils import make_screenshot, compare_screenshot
from utils import maker_of_test_data
from utils import check_response
from static.link_for_test import LinkData

load_dotenv()

host_url = os.getenv("HOST")

data = maker_of_test_data(LinkData)

@allure.story('Внешние ссылки')
class TestExternalLinks:
    @allure.title('Доступы в по внешним ключам и ссылкам')
    @pytest.mark.parametrize("kind, link",
                             data
                             )
    def test_external_link(self, page, image_snapshot, kind, link):
        page.set_default_timeout(90000)

        image_manager_url = f"{host_url}{link}"
        current_date = datetime.datetime.now()
        current_date_string = current_date.strftime('%d%m%y_%H%M%S')
        # name_file = f"{kind}_{current_date_string}"
        name_file = f"{kind}_{link}"

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        # make_screenshot(page, img_uuid=name_file)
        compare_screenshot(page, image_snapshot, img_uuid=name_file, diff=0.3, src_path='./static/layouts/')