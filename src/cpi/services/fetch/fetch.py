from pathlib import Path
import re
from typing import Union
from src.cpi.domain.entities.create_tasks import createTaskDB
from src.cpi.domain.errors.create_error import createError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from src.cpi.services.utils.months import months
from src.cpi.domain.requiredFields.cpi import DateCpi


async def fetchCpi(date: DateCpi, region: str):
  url = f'http://www.ine.gov.mz/estatisticas/estatisticas-economicas/indice-de-preco-no-consumidor/quadros/{region}'

  driver_path = str(Path(__file__).parents[4].joinpath('driver/chromedriver'))

  month = months[date['month'] - 1]
  strs = [x for x in str(date['year'])]

  year = f'{strs[2]}{strs[3]}.xls'


  file_path: Union[str, None] = None
  
  try:
    options = Options()
    options.headless = True

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    links = driver.find_elements(by='xpath', value='//*[@id="content-core"]/table/tbody/tr/td[1]/a')

    for link in links:
      name = link.text.lower()

      monthMatch = re.search(month, name)
      yearMatch = re.search(year, name)

      if (monthMatch is not None) and (yearMatch is not None):
        href = link.get_attribute('href')

        file_path = href.replace('/view', '', 1)

  except Exception as err:
    print(err)
    errorMessage = f'Could not fetch the {region} CPI, the url is {url}'

    await createTaskDB(isDone=False, error=errorMessage)

    await createError(errorMessage)

  return file_path