from consulta_empresa import  select,print_medias_segmento
import pandas as pd 


df = pd.DataFrame(print_medias_segmento('Comunicações',"Telecomunicações"))

def create_indicators():
    df['debt_equity'] = df['Total Debt']/df['Stockholders Equity']
    
    print(df['debt_equity'])
    
create_indicators()