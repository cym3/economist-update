from datetime import datetime
import re
from typing import Union
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from src.cpi.services.utils.months import min_months
from src.cpi.domain.requiredFields.cpi import DateCpi, Indicator


def fetchCpi(date: DateCpi, indicator: Indicator):
  region = indicator['web_name']
  url = f'http://www.ine.gov.mz/estatisticas/estatisticas-economicas/indice-de-preco-no-consumidor/quadros/{region}'

  old_year = date['year']
  old_month = date['month']
  years = [old_year, old_year + 1]

  file_path: Union[str, None] = None

  try:
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(url)

    links = driver.find_elements(by='xpath', value='//*[@id="content-core"]/table/tbody/tr/td[1]/a')
    link = links[0]
    name = link.text.lower()

    year = 0
    month = 0

    index = 0
    for m in min_months:
      monthMatch = re.search(m, name)

      if (monthMatch is not None):
        month = index + 1

      index += 1

    for y in years:
      strs_y = [x for x in str(y)]
      min_year = f'{strs_y[2]}{strs_y[3]}'

      yearMatch = re.search(min_year, name)

      if (yearMatch is not None):
        year = y

    old_date = datetime(old_year, old_month, 1)
    new_date = datetime(year, month, 1)

    if new_date > old_date:
      href = link.get_attribute('href')

      file_path = href.replace('/view', '', 1)

  except Exception as err:
    print(err)
    errorMessage = f'Could not fetch the {region}, the url is {url}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  if file_path is not None:
    return file_path
