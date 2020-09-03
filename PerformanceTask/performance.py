"""This module is retrieving the data for duration of performance for the given objects"""
import json
import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def main():
    """Return the pathname of the KOS root directory."""
    # initialize the chrome capabilities
    capabilities = DesiredCapabilities.CHROME
    capabilities['logingPrefs'] = {'performance': 'ALL'}

    # initialize the Chrome driver
    driver = webdriver.Chrome()

    # go to url
    driver.get('https://en.wikipedia.org/wiki/Software_metric')

    # execute command in the console
    logs = driver.execute_script('return window.performance.getEntries();')

    # initialize result string
    result = 'Succesfully retrieved data in '

    # create a txt file and retrieve the data
    with open('performance.txt', 'w') as out:
        json.dump(logs, out, indent=4, sort_keys=True)

    # initialize txt_format variable
    txt = 'txt, '

    # create a json file and retrieve the data
    with open('performance.json', 'w') as out:
        json.dump(logs, out, indent=4, sort_keys=True)

    # initialize json_format variable
    json_format = 'json, '

    # create a csv file and retrieve the data
    with open('performance.csv', 'w') as out:
        out.write('URL,Duration\n')
        for row in logs:
            out.write('%s,%s\n' % (row['name'], str(row['duration'])))

    # initialize csv_format variable
    csv_format = 'and csv format'

    # take a screenshot of the page
    driver.save_screenshot('page_screenshot.png')

    # close the browser
    driver.quit()

    # initialize log file name
    log = 'log_file.log'

    # initialize format
    asctime = '%(asctime)s %(message)s'

    # initialize loggin type
    info = logging.INFO

    # initialize date format
    date = '%m/%d/%Y %I:%M:%S %p'

    # set basic config variables
    logging.basicConfig(filename=log, format=asctime, level=info, datefmt=date)
    logging.info(result + txt + json_format+ csv_format)
    return


if __name__ == '__main__':
    main()
