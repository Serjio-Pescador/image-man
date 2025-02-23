import os
from utils.utils import get_project_root


def get_file_name(src_path, img_uuid):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-1].split('[')[0]

    folder = os.path.join(get_project_root(), src_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    rel_path = f"{test_name}_{img_uuid}.png"
    abs_file_path = os.path.join(folder, rel_path)
    return abs_file_path
