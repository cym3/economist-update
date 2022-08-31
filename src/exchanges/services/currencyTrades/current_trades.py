from posixpath import splitext
import camelot

url = 'https://www.bancomoc.mz/Files/REFR/ZMMIREFR.pdf'

def currenctTradesService():
    table1 = camelot.read_pdf(url, flavor='stream', table_regions=['170,530,560,270'])[0] 

    table2 = camelot.read_pdf(url, flavor='stream', table_regions=['170,210,600,130'])[0] 

    df = table2.df
    data = df.values.tolist()
    
    return df