import allure
import pytest
import os
import re
from dotenv import load_dotenv
from utils.compare_picture import compare_screenshot
from utils.make_storage_picture import make_screenshot
from utils.utils_func import maker_of_test_data
from utils.receive_response import check_response
from utils.utils_func import remove_prefix, remove_suffix
from static.link_for_test import LinkData, LinkNotValid
from utils.app_logger import get_logger
from utils.utils_func import compare_two_string
from utils.utils_func import make_url_tail_in_alphabet_lower


logger = get_logger(__name__)

load_dotenv()

im_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")

data = maker_of_test_data(LinkData)
invalid_data = maker_of_test_data(LinkNotValid)


@allure.story('Внешние ссылки и ключи')
@allure.label('owner', "s.rybak@okko.tv")
@allure.severity(severity_level="Critical")
class TestExternalLinks:
    @allure.title('External link/key OLD')
    @pytest.mark.parametrize("kind, link",
                             data
                             )
    def test_external_link(self, image_snapshot, kind, link):

        logger.info("Link is %s: %s", kind, link)

        image_manager_url = make_url_tail_in_alphabet_lower(f"{im_url}{link}")
        logger.info("IM url: %s", image_manager_url)
        file_name = kind + "_" + re.sub(r'[^a-zA-Z0-9]', '_', link)[0::3]

        response_im = check_response(image_manager_url)
        make_screenshot(response_im, img_uuid=file_name)

        stat_img_url = f"{static_url}{link}"
        logger.info("static url: %s", stat_img_url)
        response_static = check_response(stat_img_url)

        compare_two_string(response_im.headers.get('etag'), response_static.headers.get('etag'), "ETAG")
        compare_screenshot(response_static, image_snapshot, img_uuid=file_name, diff=0.3)

    if __name__ == "__main__":
        test_external_link()

    @allure.title('External link/key NEW')
    @pytest.mark.parametrize("kind, link",
                             data
                             )
    def test_external_link_new_api(self, image_snapshot, kind, link):

        logger.info("Link is %s: %s", kind, link)

        modified_link = str(link).replace('[', '').replace(']', '')
        modified_link = remove_prefix(modified_link, "%5B")
        modified_link = remove_suffix(modified_link, "%5D")

        image_manager_url = make_url_tail_in_alphabet_lower(f"{im_url.replace('images/v4/', 'external/v1/')}{modified_link}")
        logger.info("IM url: %s", image_manager_url)

        file_name = re.sub(r'[^a-zA-Z0-9]', '_v1_', link)

        response_im = check_response(image_manager_url)
        make_screenshot(response_im, img_uuid=file_name)

        stat_img_url = f"{static_url.replace('images/v4/', 'external/v1/')}{modified_link}"
        logger.info("static url: %s", stat_img_url)
        response_static = check_response(stat_img_url)

        compare_two_string(response_im.headers.get('etag'), response_static.headers.get('etag'), "ETAG")
        compare_screenshot(response_static, image_snapshot, img_uuid=file_name, diff=0.3)

    if __name__ == "__main__":
        test_external_link_new_api()

    @allure.title('External link/key Invalid')
    @pytest.mark.parametrize("kind, link",
                             invalid_data
                             )
    def test_external_link_invalid(self, kind, link):
        logger.info("Link is %s: %s", kind, link)

        modified_link = str(link).replace('[', '').replace(']', '')
        image_manager_url = make_url_tail_in_alphabet_lower(f"{im_url.replace('images/v4/', 'external/v1/')}{modified_link}")
        logger.info("IM url: %s", image_manager_url)

        response_im = check_response(image_manager_url)

        with allure.step("Проверка доступности контента в IM"):
            if response_im.status_code in [400, 403]:
                pass
            else:
                pytest.fail("Link is valid! I can open it!!!")

        stat_img_url = f"{static_url.replace('images/v4/', 'external/v1/')}{modified_link}"
        logger.info("static url: %s", stat_img_url)

        response_static = check_response(stat_img_url)

        with allure.step("Проверка доступности контента в статике"):
            if response_static.status_code in [400, 403]:
                pass
            else:
                pytest.fail("Link is valid! I can open it!!!")

    if __name__ == "__main__":
        test_external_link_invalid()
