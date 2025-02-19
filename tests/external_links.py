import sys
import allure
import pytest
import os
import logging
from dotenv import load_dotenv
from utils import make_screenshot, compare_screenshot
from utils import maker_of_test_data
from utils import check_response, remove_prefix, remove_suffix
from static.link_for_test import LinkData, LinkNotValid

load_dotenv()

host_url = os.getenv("HOST")

data = maker_of_test_data(LinkData)
invalid_data = maker_of_test_data(LinkNotValid)


@allure.story('Внешние ссылки')
class TestExternalLinks:
    @allure.title('Доступы в по внешним ключам и ссылкам OLD')
    @pytest.mark.parametrize("kind, link",
                             data
                             )
    def test_external_link(self, page, image_snapshot, kind, link):
        page.set_default_timeout(60000)
        logging.info("Link is %s: %s", kind, link)

        image_manager_url = f"{host_url}{link}"
        logging.info("IM url: %s", image_manager_url)

        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split('[')[0]
        link_hash = hash(link)

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        # make_screenshot(page, img_uuid=name_file)
        compare_screenshot(page, image_snapshot, img_uuid=link_hash, timeout=3000, diff=0.3)

    @allure.title('Доступы в по внешним ключам и ссылкам NEW')
    @pytest.mark.parametrize("kind, link",
                             data
                             )
    def test_external_link_new_api(self, page, image_snapshot, kind, link):
        page.set_default_timeout(60000)
        logging.info("Link is %s: %s", kind, link)

        modified_link = str(link).replace('[', '').replace(']', '')
        modified_link = remove_prefix(modified_link, "%5B")
        modified_link = remove_suffix(modified_link, "%5D")

        image_manager_url = f"{host_url.replace('images/v4/', 'external/v1/')}{modified_link}"
        logging.info("IM url: %s", image_manager_url)

        link_hash = hash(link)

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        # make_screenshot(page, img_uuid=link_hash)
        compare_screenshot(page, image_snapshot, img_uuid=link_hash, timeout=3000, diff=0.3)

    @allure.title('Доступы в по внешним ключам и ссылкам невалидные значения')
    # @pytest.mark.xfail
    @pytest.mark.parametrize("kind, link",
                             invalid_data
                             )
    def test_external_link_not_valid(self, page, kind, link):
        logging.info("Link is %s: %s", kind, link)

        modified_link = str(link).replace('[', '').replace(']', '')
        image_manager_url = f"{host_url.replace('images/v4/', 'external/v1/')}{modified_link}"
        logging.info("IM url: %s", image_manager_url)

        response = page.goto(image_manager_url)
        while check_response(response) == 429:
            response = page.goto(image_manager_url)
        assert response.status == 400

