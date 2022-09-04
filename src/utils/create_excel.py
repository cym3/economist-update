import xlsxwriter

async def createExcelFile(body: list[list[str]], title: str, header: list[str], path: str): 
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet('report')

    titleFormat = workbook.add_format({
        'bold': True,
        'font_size': 24
    })

    redFormat = workbook.add_format({
        'bg_color': '#dc2626',
        'font_color': '#ffffff'
    })

    greenFormat = workbook.add_format({
        'bg_color': '#16a34a',
        'font_color': '#ffffff'
    })
    
    headerFormat = workbook.add_format({
        'bold': True,
        'bg_color': '#0284C7',
        'border': 1,
        'border_color': '#ffffff',
        'font_color': '#ffffff',
        'center_across': True,
    })
    
    #                   row, column, Data, Format
    worksheet.write_row(0, 1, [title], titleFormat)
    worksheet.write_row(2, 1, header, headerFormat)

    index = 0
    for line in body: 
        row = index + 3
        worksheet.write_row(row, 1, line)
                
        index = index + 1

    worksheet.conditional_format(
        3,
        0,
        len(body) + 3,
        len(body[0]),
        {
            'type':'cell',
            'criteria': 'equal to',
            'value': '"No"',
            'format': redFormat
        }
    )

    worksheet.conditional_format(
        3,
        0,
        len(body) + 3,
        len(body[0]),
        {
            'type':'cell',
            'criteria': 'equal to',
            'value': '"Yes"',
            'format': greenFormat
        }
    )

    worksheet.set_row(0, 20)
    worksheet.set_row(1, 20)
    worksheet.set_row(2, 25)

    workbook.close()   
        
    return path