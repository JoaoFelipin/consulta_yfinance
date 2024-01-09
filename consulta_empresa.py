import yfinance as yf
import numpy as np 

select = {
    'Petróleo, Gás e Biocombustíveis':
        {'Exploração, Refino e Distribuição':["CSAN3.SA", "ENAT3.SA", "PETR3.SA", "PRIO3.SA", "RECV3.SA", "RPMG3.SA", "RRRP3.SA", "UGPA3.SA", "VBBR3.SA"],
         'Equipamentos':['LUPA3.SA','OPCT3.SA',"OSXB3.SA"]
        },
    'Materiais Básicos':
        {
            'Minerais Metálicos':['BRAP3.SA','CBAV3.SA','CMIN3.SA','VALE3.SA'],
            'Siderurgia':['CSNA3.SA','FESA3.SA','GGBR3.SA','GOAU3.SA','USIM3.SA'],
            'Artefatos de Ferro e Aço':[],
            'Artefatos de Cobre':[],
            'Petroquimicos':[],
            'Fertilizantes e Defensivos':[],
            'Químicos Diversos':[],
            'Madeira':[],
            'Papel e Celulose':[],
            'Embalagens':[],
            'Materiais Diversos':[]
        }

    
    
    
}



def media_balance_sheet(setor,segmento,alvo):
    target_tickers = [] 
    ticker_list = select[setor][segmento]
    for tik in ticker_list:
        target_tickers.append(tik)

    print(target_tickers)

    for i in target_tickers:
        media = []
        tick = yf.Ticker(i)
        media.append(tick.balance_sheet.loc[alvo].iloc[0])
#retorna a média para o setor do indicador inserido em alvo
    return np.mean(media)

print(media_balance_sheet('Petróleo, Gás e Biocombustíveis',"Exploração, Refino e Distribuição",'Total Debt'))
