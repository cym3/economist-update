import json
from src.creditByPurpose.infra.main import creditByPurposeInfra
from src.creditByPurpose.xlsx.read import readXlsx
from src.creditByPurpose.xlsx.parser import parseXlsx
from src.creditByPurpose.services.business_confidence import businessConfidenceService
from src.creditByPurpose.domain.entities.save_economic_activity import saveBusinessConfidenceDB
from src.creditByPurpose.domain.entities.get_last_update_date import getLastUpdateDateDB
from src.creditByPurpose.indicators import indicators
from src.creditByPurpose.formatter import creditByPurposeFormatter


def creditByPurposeUseCase():
    credit = []
    
    for indicator in indicators:
        db_name = indicator['db_name']

        # last_update_date_on_db = getLastUpdateDateDB(db_name)

        last_update_date_on_db = { 'year': 2020, 'month': 5 }

        file_path = creditByPurposeInfra(date=last_update_date_on_db, indicator=indicator)
        
        if file_path:
            response = readXlsx(documentPath=file_path)

            creditTable = parseXlsx(response)


            def filterCredit(row: list[int]):
                length = len(row) + 2
                x = slice(78,  length)

                return row[x]

            creditByPurposeLines = {
                'creditByPurposeLine4':  filterCredit(creditTable[3]),
                'creditByPurposeLine12': filterCredit(creditTable[11]),
                'creditByPurposeLine13': filterCredit(creditTable[12]),
                'creditByPurposeLine14': filterCredit(creditTable[13]),
                'creditByPurposeLine15': filterCredit(creditTable[14]),
                'creditByPurposeLine18': filterCredit(creditTable[17]),
                'creditByPurposeLine24': filterCredit(creditTable[23]),
                'creditByPurposeLine25': filterCredit(creditTable[24]),
                'creditByPurposeLine26': filterCredit(creditTable[25]),
                'creditByPurposeLine27': filterCredit(creditTable[26]),
                'creditByPurposeLine28': filterCredit(creditTable[27]),
                'creditByPurposeLine33': filterCredit(creditTable[32]),
                'creditByPurposeLine34': filterCredit(creditTable[33]),
                'creditByPurposeLine38': filterCredit(creditTable[37])
            }

            credit = creditByPurposeFormatter(creditByPurposeLines)

            json_object = json.dumps(list(credit), indent=4)

            with open(f'{db_name}.json', "w") as f:
                f.write(json_object)

            # businessConfidence = businessConfidenceService(
            #     table=tables[0],
            #     quarter=last_update_date_on_db,
            #     indicator=indicator
            # )

            # saveBusinessConfidenceDB(businessConfidence=businessConfidence, db_name=db_name)
            # print(db_name)

        else:
            print(f'No new {db_name} to update')

    return credit
