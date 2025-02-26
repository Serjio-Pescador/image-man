if [[ "$OSTYPE" =~ ^msys ]]; then
    OS=Scripts
else
    OS=bin
fi &&

#source venv/$OS/activate
rm -r ./screenshots
python3 update_pytest_ini.py
python3 -m pytest --alluredir allure-results --clean-alluredir
python3 -m pytest tests/*.py --image-snapshot-save-diff --alluredir allure-results -n 6
python3 -m pytest tests/* --image-snapshot-save-diff --alluredir allure-results --lf -n 3
allure serve allure-results --port 9999
#deactivate