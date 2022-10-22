from src.currentCurrencyTrades.infra.main import tradesInfra
from src.currentCurrencyTrades.aws.parse.tables import tablesParser
from src.currentCurrencyTrades.aws.extract.tables import extractTable
from src.currentCurrencyTrades.domain.requiredFields.page_validator import fileValidator
from src.currentCurrencyTrades.services.current_trades import currencyTradesService
from src.currentCurrencyTrades.domain.entities.save_current_trades import saveCurrentTradesDB
from src.currentCurrencyTrades.domain.entities.get_all_currencies import getAllCurrenciesDB
from src.currentCurrencyTrades.indicators import indicators

def currentCurrencyTradesUseCase():
    currenciesTrades = []
    
    for indicator in indicators:
        file_path = tradesInfra(indicator=indicator)

        if file_path:
            response = extractTable(documentPath=file_path, indicator=indicator)

            is_valid_page = fileValidator(response, indicator)

            if is_valid_page:
                tables = tablesParser(response)

                currencies = getAllCurrenciesDB(indicator)
                
                currenciesTrades = currencyTradesService(currencies, tables, indicator)

                saveCurrentTradesDB(currenciesTrades, indicator)

    return currenciesTrades
