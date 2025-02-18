# image-man
Autotests image-manager




### pytest

pytest tests/letterspacing.py --image-snapshot-update
python3 -m pytest tests/letterspacing.py --image-snapshot-update   

pytest tests/letterspacing.py --image-snapshot-save-diff --alluredir allure-results  
pytest tests/letterspacing.py --image-snapshot-save-diff -v --alluredir allure-results  
pytest tests/letterspacing.py --image-snapshot-save-diff -vv --alluredir allure-results  

python3 -m pytest tests/letterspacing.py -n 6 --image-snapshot-save-diff --alluredir allure-results -v



### Allure
python3 -m pytest --alluredir allure-results --clean-alluredir
pytest --alluredir allure-results --clean-alluredir

allure serve allure-results  

### Типовые размеры картинок
303, 606, 360, 720, ~~317, 634~~, ~~319~~, 637, 350, 700
