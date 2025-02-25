import configparser
from datetime import datetime

# Overwrite log_file filename in pytest.ini with datetime
curr_datetime = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

test_config = configparser.ConfigParser()
test_config.read('pytest.ini')
# Update the string at log_file to with latest datetime
test_config.set('pytest', 'log_file', 'logs/pytest-{}-logs.log'.format(curr_datetime))

with open('pytest.ini', 'w') as configfile:
    test_config.write(configfile)