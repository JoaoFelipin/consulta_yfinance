from consulta_empresa import  select,print_medias_segmento_balance,print_medias_segmento_dre
import pandas as pd 


df = pd.DataFrame()
df_balance = pd.DataFrame(print_medias_segmento_balance('Materiais Básicos',"Minerais Metálicos"))
df_dre = pd.DataFrame(print_medias_segmento_dre('Materiais Básicos',"Minerais Metálicos"))

def create_indicators():
    df['margem_bruta'] = df_dre['Gross Profit']/df_dre['Net Income']
    df['margem_liquida']=df_dre['Net Income Common Stockholders']/df_dre['Net Income']
    df['margem_ebitda'] = df_dre['EBITDA']/df_dre['Net Income']
    df['margem_ebit'] =df_dre['EBIT']/df_dre['Net Income']
    
    df['liquidez_imediata'] =(df_balance['Current Assets']-df_balance['Inventory']-df_balance['Accounts Receivable'])/df_balance['Current Liabilities']
    df['liquidez_geral']=(df_balance['Current Assets']-df_balance['Long Term Provisions'])/(df_balance['Total Liabilities Net Minority Interest'])
    df['liquidez_seca']=(df_balance['Current Assets']-df_balance['Inventory'])/df_balance['Current Liabilities']
    df['liquidez_corrente'] =df_balance['Current Assets']/df_balance['Current Liabilities']
    
    df['debt_ebitda'] = df_balance['Total Debt']/df_dre['EBITDA']
    df['debt_equity'] = df_balance['Total Debt']/df_balance['Stockholders Equity']
    
    df['roe'] = df_dre['Net Income']/df_balance['Stockholders Equity']
    df['roa'] =df_dre['Net Income']/df_balance['Total Assets']
    df['ebitda_interest'] = df_dre['EBITDA']/df_dre['Interest Expense']
   
    
    return print(df.head())
    
create_indicators()