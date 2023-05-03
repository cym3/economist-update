from src.utils.date.index import CreateDateUTC
import re
from typing import Union
from src.businessConfidenceBySector.domain.requiredFields.business_confidence import Indicator, Quarter
from src.businessConfidenceBySector.domain.entities.create_tasks import createTaskDB
from src.businessConfidenceBySector.domain.errors.create_error import createError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from src.businessConfidenceBySector.services.utils.months import quarters

url = 'http://www.ine.gov.mz/estatisticas/estatisticas-economicas/icce'

def fetchBusinessConfidence(quarter: Quarter, indicator: Indicator):
  db_name = indicator['db_name']
  last_update_year = quarter['year']
  last_update_month = quarter['fromMonth']
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
    # Check if is Indicadores de Confiança e de Clima Económico (ICCE) I Trimestre 2022
    match1 = re.search('indicador', name)
    match2 = re.search('confiança', name)
    match3 = re.search('clima económico', name)
    match4 = re.search('icce', name)

    if (match1 is None) or (match2 is None) or (match3 is None) or (match4 is None):
      file_url = None
      return

    # Find Business Confidence Year
    year = 0
    for y in years:
      strs_y = [x for x in str(y)]
      min_year = f'{strs_y[2]}{strs_y[3]}'

      yearMatch = re.search(min_year, name)

      if (yearMatch is not None):
        year = y

    # Find Business Confidence Quarter
    newQuarter: Union[Quarter, None] = None

    for q in quarters:
      sign = q['sign']['pt'].lower()
      quarterMatch = re.search(f'{sign} trimestre', name)

      if (quarterMatch is not None):
        q['year'] = year
        newQuarter = q

    last_update = CreateDateUTC(last_update_year, last_update_month, 1).date
    year = newQuarter['year']
    month = newQuarter['fromMonth']
    new_update = CreateDateUTC(year, month, 1).date

    if new_update > last_update:
      href = link.get_attribute('href')

      file_url = href.replace('/view', '', 1)

  except Exception as err:
    print(err)
    errorMessage = f'Could not fetch the {db_name}, the url is {url}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return file_url
