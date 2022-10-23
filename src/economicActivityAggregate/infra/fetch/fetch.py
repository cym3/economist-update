from datetime import datetime
import re
from typing import Union
from src.economicActivityAggregate.domain.entities.create_tasks import createTaskDB
from src.economicActivityAggregate.domain.errors.create_error import createError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from src.economicActivityAggregate.services.utils.months import months
from src.economicActivityAggregate.domain.requiredFields.economic_activity import DateEconomicActivity, Indicator

url = 'http://www.ine.gov.mz/estatisticas/estatisticas-economicas/indice-de-actividades-economicas-iae'

def fetchEconomicActivity(date: DateEconomicActivity, indicator: Indicator):
  db_name = indicator['db_name']
  last_update_year = date['year']
  last_update_month = date['month']
  years = [last_update_year, last_update_year + 1]

  file_url: Union[str, None] = None

  try:
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(url)
    
    links = driver.find_elements(by='xpath', value='//*[@id="content-core"]/table/tbody/tr/td[1]/a')
    link = links[0]
    name = link.text.lower()

    # Check if is Índice de Actividades Económicas
    match1 = re.search('índice', name)
    match2 = re.search('actividade', name)
    match3 = re.search('económica', name)

    if (match1 is None) or (match2 is None) or (match3 is None):
      file_url = None
      return

    # Find EAI Month
    year = 0
    month = 0

    index = 0
    for m in months:
      monthMatch = re.search(m, name)

      if (monthMatch is not None):
        month = index + 1

      index += 1

    index = 0

    # Find EAI Year
    for y in years:
      strs_y = [x for x in str(y)]
      min_year = f'{strs_y[2]}{strs_y[3]}'

      yearMatch = re.search(min_year, name)

      if (yearMatch is not None):
        year = y

      index += 1

    last_update = datetime(last_update_year, last_update_month, 1)
    new_update = datetime(year, month, 1)

    if new_update > last_update:
      href = link.get_attribute('href')

      file_url = href.replace('/view', '', 1)

  except Exception as err:
    print(err)
    errorMessage = f'Could not fetch the {db_name}, the url is {url}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return file_url