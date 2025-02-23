# image-man
Autotests image-manager




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
python3 -m pytest --alluredir allure-results --clean-alluredir
pytest --alluredir allure-results --clean-alluredir

allure serve allure-results  


### Docker
docker build -t tests .
docker run -d tests --mount source=screenshots,target=./screenshots --name=pytest 
docker run -d tests --mount source=screenshots,target=./screenshots pytest   
