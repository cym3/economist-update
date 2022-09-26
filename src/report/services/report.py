from datetime import datetime
from src.report.domain.requiredFields.report import Report

def reportService(tasks: list[Report]):
    r_tasks = []
    
    for task in tasks:
        isDone = task['isDone']
        if isDone == True:
            isDone = 'Yes'
        if isDone == False:
            isDone = 'No'

        created_at: datetime = task['created_at']
        date = created_at.strftime('%Y-%m-%d %H:%M:%S')
        task['date'] = date

        jobCode = task['jobCode']
        name = task['name']
        description = task['description']
        error = task['error']

        values = [jobCode, name, description, isDone, error, date]
        
        r_tasks.append(values)

    return r_tasks
