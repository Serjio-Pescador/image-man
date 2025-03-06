from PIL import Image
import io
import pytest
import allure
from utils.utils_func import allure_attach_image, compare_two_digital
from utils.file_name_maker import get_file_name
from utils.app_logger import get_logger, handler


logger = get_logger(__name__)
# logger.addHandler(handler)


def make_screenshot(self, img_uuid,
                    src_path: str = 'screenshots/',
                    required_width: int = None,
                    required_height: int = None,
                    ):
    abs_file_path = get_file_name(src_path, img_uuid)

    if self.content:
        img_obj = Image.open(io.BytesIO(self.content))
    else:
        logger.error("Content-legnth: 0")
        pytest.fail("Content-legnth: 0")

    img_obj.save(abs_file_path)

    image_manager_img_width, image_manager_img_height = img_obj.size
    logger.info("image_manager_img_width=%s, image_manager_img_height=%s", image_manager_img_width,
                image_manager_img_height)

    with allure.step("Изображение из ИМ"):
        allure_attach_image(abs_file_path, img_uuid)
    assert compare_two_digital(required_width, image_manager_img_width, "WIDTH"), "Different WIDTH"
    assert compare_two_digital(required_height, image_manager_img_height, "HEIGHT"), "Different HEIGHT"
    return
