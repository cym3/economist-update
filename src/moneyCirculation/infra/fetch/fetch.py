import os
import time
from typing import Union
from src.moneyCirculation.infra.fetch.is_new_file import isNewFile
from src.moneyCirculation.domain.requiredFields.main import MoneyCirculation, Indicator
from src.moneyCirculation.domain.entities.create_tasks import createTaskDB
from src.moneyCirculation.domain.errors.create_error import createError
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from rapidfuzz.fuzz import partial_ratio

url = 'https://www.bancomoc.mz/fm_pgLink.aspx?id=223'

def fetchMoneyCirculation(date: MoneyCirculation, folder_path: Path, indicator: Indicator):
  db_name = indicator['db_name']
  file_folder = str(folder_path)
  documentPath: Union[Path, None] = None

  prefs = { 'download.default_directory': file_folder }

  try:
    options = Options()
    options.headless = True
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(url)
    
    link = driver.find_element(by='xpath', value='//*[@id="ContentPlaceHolder1_BMlnk_565_223"]')
    name = link.accessible_name
    link.click()
    time.sleep(5)    
    driver.close()

    pattern = 'pt_12_NMCs'

    for root, dirs, files in os.walk(file_folder):
      for file in files:
        match_score = partial_ratio(pattern, file)
        if (match_score > 95):
          documentPath = folder_path.joinpath(file)

    is_new = isNewFile(date, name)

    if is_new is False:
      documentPath.unlink()
      return None
    
  except Exception as err:
    print(err)
    errorMessage = f'Could not fetch the {db_name}, the url is {url}'

    createTaskDB(isDone=False, indicator=indicator, error=errorMessage)

    createError(errorMessage, indicator)

  return documentPath
