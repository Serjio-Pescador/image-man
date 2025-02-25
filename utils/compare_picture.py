import pytest
from PIL import Image
import io
import logging
from utils.utils import allure_attach_image, compare_two_digital
from utils.file_name_maker import get_file_name


def compare_screenshot(self, image_snapshot, img_uuid, diff: float = 0.5,
                       src_path: str = 'screenshots/',
                       required_width: int = None,
                       required_height: int = None,
                       ):
    # for key in ('src_path', 'required_width', 'required_height', 'timeout'):
    #     if key in kwargs:
    #         setattr(self, key, kwargs[key])

    abs_file_path = get_file_name(src_path, img_uuid)
    picture = Image.open(io.BytesIO(self.content))

    try:
        # allure_attach_image(src_path=img_uuid,
        #                     img_uuid=f"{test_name}_{img_uuid}.png")
        image_snapshot(picture, f"{abs_file_path}", diff)
    except Exception as e:
        # logging.error("Image does not match the snapshot stored in screenshots.", e)
        logging.error("Image does not match the snapshot stored in screenshots.")
        allure_attach_image(src_path=f"{abs_file_path}",
                            img_uuid=f"{img_uuid}", suffix='.new')
        allure_attach_image(src_path=f"{abs_file_path}",
                            img_uuid=f"{img_uuid}", suffix='.diff')

        pytest.fail("Image does not match the snapshot stored in screenshots.", e)

    static_img_width, static_img_height = picture.size
    logging.info("static_img_width=%s, static_img_height=%s", static_img_width, static_img_height)

    if required_width:
        compare_two_digital(required_width, static_img_width, "width")
    if required_height:
        compare_two_digital(required_height, static_img_height, "height")
    return
