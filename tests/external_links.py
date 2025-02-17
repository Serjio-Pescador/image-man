import sys

import allure
import pytest
import os
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
    @allure.title('Доступы в по внешним ключам и ссылкам OLD')
    @pytest.mark.parametrize("kind, link",
                             data
                             )
    def test_external_link(self, page, image_snapshot, kind, link):
        page.set_default_timeout(60000)

        image_manager_url = f"{host_url}{link}"
        # current_date = datetime.datetime.now()
        # current_date_string = current_date.strftime('%d%m%y_%H%M%S')
        # # name_file = f"{kind}_{current_date_string}"
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split('[')[0]
        link_hash = hash(link)
        # name_file = f"{test_name}_{kind}_{link_hash}"

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        # make_screenshot(page, img_uuid=name_file)
        compare_screenshot(page, image_snapshot, img_uuid=link_hash, timeout=3000, diff=0.3, src_path='./static/layouts/')

    @allure.title('Доступы в по внешним ключам и ссылкам NEW')
    @pytest.mark.parametrize("kind, link",
                             data
                             )
    def test_external_link_new_api(self, page, image_snapshot, kind, link):
        page.set_default_timeout(60000)


        modified_link = str(link).replace('[', '').replace(']', '')
        image_manager_url = f"{host_url.replace('images/v4/', 'external/v1/')}{modified_link}"
        # test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split('[')[0]
        link_hash = hash(link)
        # name_file = f"{test_name}_{link_hash}"

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        # make_screenshot(page, img_uuid=name_file)
        compare_screenshot(page, image_snapshot, img_uuid=link_hash, timeout=3000, diff=0.3, src_path='./static/layouts/')