import allure
import pytest
import os
import re
import logging
from dotenv import load_dotenv
from utils.utils import compare_screenshot
from utils.utils import maker_of_test_data
from utils.receive_ok_response import check_response
from utils.utils import remove_prefix, remove_suffix
from static.link_for_test import LinkData, LinkNotValid


load_dotenv()

host_url = os.getenv("HOST")

data = maker_of_test_data(LinkData)
invalid_data = maker_of_test_data(LinkNotValid)


@allure.story('Внешние ссылки и ключи')
class TestExternalLinks:
    @allure.title('External link/key OLD')
    @pytest.mark.parametrize("kind, link",
                             data
                             )
    def test_external_link(self, image_snapshot, kind, link):

        logging.info("Link is %s: %s", kind, link)

        image_manager_url = f"{host_url}{link}"
        logging.info("IM url: %s", image_manager_url)

        file_name = re.sub(r'[^a-zA-Z0-9]', '_', link)

        response = check_response(image_manager_url)

        # make_screenshot(page, img_uuid=file_name, timeout=6000)
        compare_screenshot(response, image_snapshot, img_uuid=file_name, timeout=3000, diff=0.3)

    @allure.title('External link/key NEW')
    @pytest.mark.parametrize("kind, link",
                             data
                             )
    def test_external_link_new_api(self, image_snapshot, kind, link):

        logging.info("Link is %s: %s", kind, link)

        modified_link = str(link).replace('[', '').replace(']', '')
        modified_link = remove_prefix(modified_link, "%5B")
        modified_link = remove_suffix(modified_link, "%5D")

        image_manager_url = f"{host_url.replace('images/v4/', 'external/v1/')}{modified_link}"
        logging.info("IM url: %s", image_manager_url)

        file_name = re.sub(r'[^a-zA-Z0-9]', '_', link)

        response = check_response(image_manager_url)

        # make_screenshot(page, img_uuid=file_name, timeout=6000)
        compare_screenshot(response, image_snapshot, img_uuid=file_name, timeout=3000, diff=0.3)

    @allure.title('External link/key Invalid')
    @pytest.mark.parametrize("kind, link",
                             invalid_data
                             )
    def test_external_link_invalid(self, kind, link):
        logging.info("Link is %s: %s", kind, link)

        modified_link = str(link).replace('[', '').replace(']', '')
        image_manager_url = f"{host_url.replace('images/v4/', 'external/v1/')}{modified_link}"
        logging.info("IM url: %s", image_manager_url)

        check_response(image_manager_url)
        if check_response(image_manager_url).status_code == 400:
            pass
