#! /bin/bash

RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
BLUE="\033[0;34m"
PURPLE="\033[0;35m"
ENDCOLOR="\033[0m"


if [[ $1 ]]; then
  REPEATFAILED=true
else
  REPEATFAILED=false
fi

re='^[0-9]+$'

if [[ $2 ]]; then
  if ! [[ $2 =~ $re ]] ; then
    echo -e "${RED}ERROR: Not a number for WORKERS!${ENDCOLOR}" >&2; exit 1
  else
    WORKERS=$2
  fi
else
    WORKERS=4
fi


echo -e "${YELLOW}Remove directory ./screenshots${ENDCOLOR}"
rm -r ./screenshots

echo -e "${GREEN}Update log file date...${ENDCOLOR}"
python3 update_pytest_ini.py

echo -e "${YELLOW}Clean allure report folder${ENDCOLOR}"
#python3 -m pytest --alluredir allure-results --clean-alluredir
rm -r ./allure-results/*

echo -e "${GREEN}--->  START TESTs  <---${ENDCOLOR}"
python3 -m pytest tests/* -n ${WORKERS} --image-snapshot-save-diff --alluredir allure-results
echo -e "${GREEN}First iteration complete!${ENDCOLOR}"

echo -e "${GREEN}Update log file date...${ENDCOLOR}"
python3 update_pytest_ini.py

if ${REPEATFAILED}; then
  echo -e "${BLUE}START SECOND TESTs ITERATION${ENDCOLOR}"
  python3 -m pytest tests/* -n ${WORKERS} --lf --image-snapshot-save-diff --alluredir allure-results
  echo -e "${GREEN}Second iteration complete!${ENDCOLOR}"
fi

echo -e "${YELLOW}-------------------------------${ENDCOLOR}"
echo -e "${YELLOW}|   Open allure-report        |${ENDCOLOR}"
echo -e "${YELLOW}-------------------------------${ENDCOLOR}"
