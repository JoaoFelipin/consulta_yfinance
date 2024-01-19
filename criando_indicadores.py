from consulta_empresa import  select,print_medias_segmento_balance,print_medias_segmento_dre
import pandas as pd 


df = pd.DataFrame()
df_balance = pd.DataFrame(print_medias_segmento_balance('Comunicações',"Telecomunicações"))
df_dre = pd.DataFrame(print_medias_segmento_dre('Comunicações',"Telecomunicações"))

def create_indicators():
    df['margem_bruta'] = df_dre['Gross Profit']/df_dre['Net Income']
    df['margem_liquida']=1
    df['margem_ebitda'] = df_dre['EBITDA']/df_dre['Net Income']
    df['margem_ebit'] =1
    
    df['liquidez_imediata'] =1
    df['liquidez_geral']=1
    df['liquidez_seca']=1
    df['liquidez_corrente'] =1
    
    df['debt_ebitda'] = 1
    df['debt_equity'] = df_balance['Total Debt']/df_balance['Stockholders Equity']
    
    df['roe'] = df_dre['Net Income']/df_balance['Stockholders Equity']
    df['roa'] =1
    df['ebitda_interest'] = 1
   
    
    print(df.head())
    
create_indicators()