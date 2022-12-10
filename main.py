import schedule
import time
from src.moneyPrinting.main import moneyPrintingUseCase
from src.moneyCirculation.main import moneyCirculationUseCase
from src.creditByActivitySector.main import creditByActivitySectorUseCase
from src.creditByPurpose.main import creditByPurposeUseCase
from src.economicActivityAggregate.main import economicActivityAggregateUseCase
from src.businessConfidenceAggregate.main import businessConfidenceAggregateUseCase
from src.businessConfidenceBySector.main import businessConfidenceBySectorUseCase
from src.cpi.main import cpiUseCase
from src.currentCurrencyTrades.main import currentCurrencyTradesUseCase
from src.interestRates.main import interestRatesUseCase
from src.report.main import reportUseCase
from src.core.mail.my_mail import sandMyMail
from dotenv import load_dotenv

load_dotenv()

schedule.every().day.at("02:00").do(economicActivityAggregateUseCase)
schedule.every().day.at("02:03").do(businessConfidenceAggregateUseCase)
schedule.every().day.at("02:06").do(businessConfidenceBySectorUseCase)
schedule.every().day.at("02:12").do(creditByActivitySectorUseCase)
schedule.every().day.at("02:15").do(creditByPurposeUseCase)
schedule.every().day.at("02:18").do(moneyCirculationUseCase)
schedule.every().day.at("02:21").do(moneyPrintingUseCase)

schedule.every().day.at("03:00").do(cpiUseCase)
schedule.every().day.at("04:00").do(sandMyMail)
schedule.every().day.at("04:00").do(reportUseCase)
schedule.every().day.at("08:00").do(interestRatesUseCase)

schedule.every().day.at("08:00").do(currentCurrencyTradesUseCase)
schedule.every().day.at("16:00").do(currentCurrencyTradesUseCase)

schedule.every(5).seconds.do(creditByPurposeUseCase)

while True:
    schedule.run_pending()
    time.sleep(1)
     