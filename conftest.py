import pytest
import os
from pathlib import Path


@pytest.fixture(scope="session")
def temp_dir(tmpdir):
    if not tmpdir:
        tmpdir = Path(__file__).parent.parent
    tmpdir.mkdir('screenshots/')
    return


# Clean up: Remove the temporary files after the tests
# @pytest.fixture(autouse=True)
# def cleanup_temp_files(temp_dir):
#     yield
#     for file in temp_dir.iterdir():
#         if file.is_file():
#             os.remove(file)
