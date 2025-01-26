# image-man
Autotests image-manager


### pytest

pytest tests/letterspacing.py --image-snapshot-update  
pytest tests/letterspacing.py --image-snapshot-save-diff --alluredir allure-results  
pytest tests/letterspacing.py --image-snapshot-save-diff -v --alluredir allure-results  
pytest tests/letterspacing.py --image-snapshot-save-diff -vv --alluredir allure-results  



### Allure
python3 -m pytest --alluredir allure-results --clean-alluredir
or
pytest --alluredir allure-results --clean-alluredir
