import os
from pathlib import Path

def getDriverPath():
  NODE_ENV = os.getenv('NODE_ENV')

  if NODE_ENV == 'production' :
    return str(Path(__file__).parent.joinpath('linux/chromedriver'))
    
  else:
    return str(Path(__file__).parent.joinpath('win/chromedriver'))

