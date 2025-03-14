# image-man
FAST Autocheck for **image-manager**


### pytest

pytest tests/letterspacing.py --image-snapshot-update

python3 -m pytest tests/letterspacing.py --image-snapshot-update   

pytest tests/letterspacing.py --image-snapshot-save-diff --alluredir allure-results

pytest tests/letterspacing.py --image-snapshot-save-diff -v --alluredir allure-results 

pytest tests/letterspacing.py --image-snapshot-save-diff -vv --alluredir allure-results  

python3 -m pytest tests/letterspacing.py -n 6 --image-snapshot-save-diff --alluredir allure-results -v

python3 -m pytest tests/tv_channels.py -n 4 --image-snapshot-save-diff --alluredir allure-results

python3 -m pytest tests/* --image-snapshot-save-diff --alluredir allure-results -n 4   


### Allure

#### очистка отчета результатов

$ python3 -m pytest --alluredir allure-results --clean-alluredir

$ pytest --alluredir allure-results --clean-alluredir

#### генерация отчета и открытие
$ allure generate allure-results  && allure open 
$ allure generate ./ && allure open 

#### открытие отчета результатов

$ allure serve allure-results  


### Docker

$ docker build -t tests .

$ docker run -d --env-file .env tests --mount source=screenshots,target=./screenshots
 

---------

### **START in DOCKER TESTS and ALLURE-REPORT**

$ docker compose build

$ docker compose --env-file .env up -d

