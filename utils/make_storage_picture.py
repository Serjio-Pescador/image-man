from PIL import Image
import io
from utils.utils_func import allure_attach_image, compare_two_digital
from utils.file_name_maker import get_file_name
from utils.app_logger import get_logger

logger = get_logger(__name__)


def make_screenshot(self, img_uuid,
                    src_path: str = 'screenshots/',
                    required_width: int = None,
                    required_height: int = None,
                    ):
    abs_file_path = get_file_name(src_path, img_uuid)

    img_obj = Image.open(io.BytesIO(self.content))
    img_obj.save(abs_file_path)

    image_manager_img_width, image_manager_img_height = img_obj.size
    logger.info("image_manager_img_width=%s, image_manager_img_height=%s", image_manager_img_width,
                image_manager_img_height)

    allure_attach_image(abs_file_path, img_uuid)
    # compare_two_digital(required_width, image_manager_img_width, "WIDTH")
    # compare_two_digital(required_height, image_manager_img_height, "HEIGHT")

    return
