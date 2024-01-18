import yfinance as yf
import numpy as np 
import pandas as pd 

select = {
    'Petróleo, Gás e Biocombustíveis':
        {'Exploração, Refino e Distribuição':["CSAN3.SA", "ENAT3.SA", "PETR3.SA", "PRIO3.SA", "RECV3.SA", "RPMG3.SA", "RRRP3.SA", "UGPA3.SA", "VBBR3.SA"],
         'Equipamentos':['LUPA3.SA','OPCT3.SA',"OSXB3.SA"]
        },
    'Materiais Básicos':
        {
            'Minerais Metálicos':['BRAP3.SA','CBAV3.SA','CMIN3.SA','VALE3.SA'],
            'Siderurgia':['CSNA3.SA','FESA3.SA','GGBR3.SA','GOAU3.SA','USIM3.SA'],
            'Artefatos de Ferro e Aço':['MGEL3.SA','PATI3.SA','TKNO3.SA'],
            'Artefatos de Cobre':['PMAM3.SA'],
            'Petroquimicos':['BRKM3.SA','DEXP3.SA'],
            'Fertilizantes e Defensivos':['FHER3.SA','NUTR3.SA','VITT3.SA'],
            'Químicos Diversos':['CRPG3.SA','UNIP3.SA'],
            'Madeira':['DXCO3.SA','EUCA3.SA'],
            'Papel e Celulose':['KLBN3.SA','MSPA3.SA','NEMO3.SA',"SUZB3.SA"],
            'Embalagens':['RANI3.SA'],
            'Materiais Diversos':['SNSY3.SA']
        },

    'Bens Industriais':
        {
            'Produtos para Construção':['ETER3.SA','HAGA3.SA','PTBL3.SA'],
            'Construção Pesada':['AZEV3.SA'],
            'Engenharia Consultiva':['SOND3.SA'],
            'Material Aeronáutico e de Defesa':['EMBR3.SA'],
            'Material Rodoviário':['FRAS3.SA','MWET3.SA','POMO3.SA','RAPT3.SA','RCSL3.SA','RSUL3.SA','TUPY3.SA'],
            'Motores, Compressores e Outros':['SHUL3.SA','WEGE3.SA'],
            'Máq. e Equip. Industriais':['AERI3.SA','ARML3.SA','BDLL3.SA','EALT3.SA','FRIO3.SA','INEP3.SA','KEPL3.SA','MILS3.SA','NORD3.SA','PTCA3.SA','ROMI3.SA'],
            'Máq. e Equip. Construção e Agrícolas':['MTSA3.SA'],
            'Armas e Munições':['TASA3.SA'],
            'Linhas Aéreas de Passageiros':['AZUL4.SA','GOLL4.SA'],
            'Transporte Ferroviário':['RAIL3.SA','VSPT3.SA'],
            'Transporte Hidroviário':['HBSA3.SA','LOGN3.SA','LUXM3.SA'],
            'Transporte Rodoviário':['JSLG3.SA','TGMA3.SA'],
            'Exploração de Rodovias':['CCRO3.SA','ECOR3.SA','TPIS3.SA'],
            'Serviços de Apoio e Armazenagem':['PORT3.SA',"STBP3.SA"],
            'Serviços Diversos':['ALPK3.SA','ATMP3.SA','BBML3.SA','DTCY3.SA','GGPS3.SA','PRNR3.SA','SEQL3.SA','VLID3.SA'],
            'Material de Transporte':['EPAR3.SA','MMAQ3.SA','WLMM3.SA']
            
        },
    'Consumo não Ciclico':
        {
            'Agricultura':['AGRO3.SA','AGXY3.SA','APTI3.SA','CTCA3.SA','FRTA3.SA','GRAO3.SA','LAND3.SA','SLCE3.SA','SOJA3.SA','TTEN3.SA'],
            'Açucar e Alcool':['JALL3.SA','SMTO3.SA'],
            'Carnes e Derivados':['BEEF3.SA','BRFS3.SA','JBSS3.SA','MNPR3.SA','MRFG3.SA'],
            'Alimentos Diversos':['CAML3.SA','JOPA3.SA','MDIA3.SA'],
            'Cervejas e Refrigerantes':['ABEV3.SA'],
            'Produtos de Cuidado Pessoal':['NTCO3.SA'],
            'Produtos de Limpeza':['BOBR3.SA'],
            'Alimentos':['ASAI3.SA','CRFB3.SA','GMAT3.SA','PCAR3.SA']
        },
    
    'Consumo Cíclico':
        {
            'Incorporações':['AVLL3.SA','CALI3.SA','CURY3.SA','CYRE3.SA','DIRR3.SA','EVEN3.SA','EZTC3.SA','FIEI3.SA','GFSA3.SA','HBOR3.SA','INNT3.SA','JFEN3.SA','JHSF3.SA','LAVV3.SA','MDNE3.SA','MELK3.SA','MRVE3.SA','MTRE3.SA','PDGR3.SA','PLPL3.SA','RDNI3.SA','RSID3.SA','TCSA3.SA','TEND3.SA','TRIS3.SA','VIVR3.SA'],
            'Fios e Tecidos':['CATA3.SA','CEDO3.SA','CTKA3.SA','CTNM3.SA','CTSA3.SA','DOHL3.SA','PTNT3.SA','SGPS3.SA','TEKA3.SA','TXRX3.SA'],
            'Vestuário':['AMAR3.SA','ARZZ3.SA','CEAB3.SA','CGRA3.SA','GUAR3.SA','LREN3.SA','SOMA3.SA','VSTE3.SA'],
            'Calçados':['ALPA3.SA','CAMB3.SA','GRND3.SA','VULC3.SA'],
            'Acessórios':['MNDL3.SA','TECN3.SA','VIVA3.SA'],
            'Eletrodomésticos':['ALLD3.SA','BHIA3.SA','MGLU3.SA','WHRL3.SA'],
            'Móveis':['MBLY3.SA','UCAS3.SA','WEST3.SA'],
            'Utensílios Domésticos':['HETA3.SA'],
            'Automóveis e Motocicletas':['LEVE3.SA','MYPK3.SA','PLAS3.SA'],
            'Hotelaria':['HOOT3.SA'],
            'Restaurante e Similares':['MEAL3.SA','ZAMP3.SA'],
            'Bicicletas':['BMKS3.SA'],
            'Brinquedos e Jogos':['ESTR3.SA'],
            'Produção de Eventos e Shows':['AHEB3.SA','SHOW3.SA'],
            'Viagens e Turismo':['CVCB3.SA'],
            'Atividades Esportivas':['SMFT3.SA'],
            'Serviços Educacionais':['ANIM3.SA','BAHI3.SA','COGN3.sA','CSED3.SA','SEER3.SA','YDUQ3.SA'],
            'Aluguel de Carros':['MOVI3.SA','MSRO3.SA','RENT3.SA','VAMO3.SA'],
            'Programas de Fidelização':['DOTZ3'],
            'Tecidos, Vestuário e Calçados':['AMAR3.SA','ARZZ3.SA','CEAB3.SA','CGRA3.SA','GUAR3.SA','LREN3.SA','SOMA3.SA','VSTE3.SA'],
            'Produtos Diversos':['AMER3.SA','ESPA3.SA','LJQQ3.SA','PETZ3.SA','SBFG3.SA']
        },
    
    'Saúde':
        {
            'Medicamentos e Outros':['BIOM3.SA','BLAU3.SA','DMVF3.SA','HYPE3.SA','NRTQ3.SA','OFSA3.SA','PFRM3.SA','PGMN3.SA','PNVL3.SA','RADL3.SA','VVEO3.SA'],
            'Serviços Médicos - Hospitalares':['AALR3.SA','DASA3.SA','FLRY3.SA','HAPV3.SA','KRSA3.SA','MATD3.SA','ODPV3.SA','ONCO3.SA','QUAL3.SA','RDOR3.SA'],
            'Equipamentos':['BALM3.SA']
        },
    'Tecnologia da Informação':
        {
            'Computadores e Equipamentos':['INTB3.SA','MLAS3.SA','POSI3.SA'],
            'Programas e Serviços':['BMOB3.SA','BRQB3.SA','CASH3.SA','ENJU3.SA','IFCM3.SA','LVTC3.SA','LWSA3.SA','NGRD3.SA','NINJ3.SA','PDTC3.SA','QUSW3.SA','SQIA3.SA','TOTS3.SA','TRAD3.SA']
        },
    'Comunicações':
        {
            'Telecomunicações':['BRIT3.SA','DESK3.SA','FIQE3.SA','OIBR3.SA','TELB3.SA','TIMS3.SA','VIVT3.SA'],
            'Publicidade e Propaganda':['ELMD3.SA']
        },
    'Utilidade Pública':
        {
           'Energia Elétrica':['AESB3.SA','AFLT3.SA','ALUP3.SA','AURE3.SA','CBEE3.SA','CEBR3.SA','CEEB3.SA','CEED3.SA','CLSC3.SA','CMIG3.SA','COCE3.SA','CPFE3.SA','CPLE3.SA','CPRE3.SA','CSRN3.SA','EGIE3.SA','EKTR3.SA','ELET3.SA','EMAE3.SA','ENEV3.SA','ENGI3.SA','ENMT3.SA','EQPA3.SA','EQTL3.SA','GEPA3.SA','GPAR3.SA','LIGT3.SA','LIPR3.SA','MEGA3.SA','NEOE3.SA','REDE3.SA','RNEW3.SA','STKF3.SA','TAEE3.SA','TRPL3.SA'],
           'Água e Saneamento':['AMBP3.SA','CASN3.SA','CSMG3.SA','IGSN3.SA','ORVR3.SA','SAPR3.SA','SBSP3.SA'],
           'Gás':['CEGR3.SA','CGAS3.SA']
        },
    'Financeiro':
        {
            'Bancos':['BAZA3.SA','BBAS3.SA','BBDC3.SA','BEES3.SA','BGIP3.SA','BMEB3.SA','BMIN3.SA','BNBR3.SA','BPAC3.SA','BPAR3.SA','BRBI3.SA','BRIV3.SA','BRSR3.SA','BSLI3.SA','ITUB3.SA','PINE3.SA','RPAD3.SA','SANB3.SA'],
            'Soc. Crédito e Financiamento':['CRIV3.SA','MERC3.SA'],
            'Soc. Arrendamento Mercantil':[],
            'Securitizadoras de Recebíveis':[],
            'Gestão de Recursos e Investimentos':[],
            'Serviços Financeiros Diversos':['B3SA3.SA','CIEL3.SA','CLSA3.SA','CSUD3.SA'],
            'Seguradoras':['BBSE3.SA','BRGE3.SA','CSAB3.SA','CXSE3.SA','PSSA3.SA'],
            'Resseguradoras':['IRBR3.SA'],
            'Corretoras de Seguros e Resseguros':['APER3.SA','WIZC3.SA'],
            'Exploração de Imóveis':["MULT3.SA", "SCAR3.SA", "ALOS3.SA", "BRPR3.SA", "AVLL3.SA", "HBTS5.SA", "EMCC3.SA", "IGTI3.SA", "SYNE3.SA", "NEXP3.SA", "GSHP3.SA", "LOGG3.SA", "IGBR3.SA"],
            'Intermediação Imobiliária':['LPSB3.SA','NEXP3.SA'],
            'Holdings Diversificadas':['ITSA3.SA','MOAR3.SA','SIMH3.SA'],
            'Outros Títulos':[]
        },
    'Outros':
        {
            'Outros':['ATOM3.SA','CMSA3.SA','FIGE3.SA','MAPT3.SA','PPAR3.SA']
        }
}



def media_balance_sheet(setor,segmento,alvo):
    target_tickers = [] 
    media = []
    ticker_list = select[setor][segmento]
    for tik in ticker_list:
        target_tickers.append(tik)

    #print(target_tickers)

    for i in target_tickers:
        
        tick = yf.Ticker(i)
        media.append(tick.balance_sheet.loc[alvo].iloc[0])
#retorna a média para o setor do indicador inserido em alvo
    return round(np.mean(media),2)

indicadores = ['Ordinary Shares Number', 'Share Issued', 'Total Debt',
       'Tangible Book Value', 'Invested Capital', 'Working Capital',
       'Net Tangible Assets', 'Capital Lease Obligations',
       'Common Stock Equity', 'Total Capitalization',
       'Total Equity Gross Minority Interest', 'Minority Interest',
       'Stockholders Equity', 'Gains Losses Not Affecting Retained Earnings',
       'Other Equity Adjustments', 'Retained Earnings',
       'Additional Paid In Capital', 'Capital Stock', 'Common Stock',
       'Preferred Stock', 'Total Liabilities Net Minority Interest',
       'Total Non Current Liabilities Net Minority Interest',
       'Other Non Current Liabilities',
       'Preferred Securities Outside Stock Equity',
       'Non Current Accrued Expenses', 'Non Current Deferred Liabilities',
       'Non Current Deferred Revenue',
       'Non Current Deferred Taxes Liabilities',
       'Long Term Debt And Capital Lease Obligation',
       'Long Term Capital Lease Obligation', 'Long Term Debt',
       'Long Term Provisions', 'Current Liabilities',
       'Other Current Liabilities', 'Current Deferred Liabilities',
       'Current Deferred Revenue', 'Current Debt And Capital Lease Obligation',
       'Current Capital Lease Obligation', 'Current Debt',
       'Other Current Borrowings', 'Current Provisions',
       'Payables And Accrued Expenses', 'Current Accrued Expenses',
       'Interest Payable', 'Payables', 'Total Tax Payable', 'Accounts Payable',
       'Total Assets', 'Total Non Current Assets', 'Other Non Current Assets',
       'Goodwill And Other Intangible Assets', 'Other Intangible Assets',
       'Goodwill', 'Net PPE', 'Accumulated Depreciation', 'Gross PPE',
       'Leases', 'Construction In Progress', 'Other Properties',
       'Machinery Furniture Equipment', 'Land And Improvements', 'Properties',
       'Current Assets', 'Other Current Assets', 'Prepaid Assets', 'Inventory',
       'Other Inventories', 'Finished Goods', 'Work In Process',
       'Raw Materials', 'Receivables', 'Accounts Receivable',
       'Cash Cash Equivalents And Short Term Investments',
       'Other Short Term Investments', 'Cash And Cash Equivalents']

def print_medias_segmento(setor,segmento):  
    resultados = {}
    for i in indicadores:
        try:
            #print(i)
            #print(media_balance_sheet(setor, segmento, i))
            resultados[i]=[media_balance_sheet(setor, segmento, i)]   
        except: 
            resultados[i] = 0
            continue
    return resultados



dict = print_medias_segmento('Comunicações',"Telecomunicações")
df = pd.DataFrame(dict)
print(df.head())
df.to_excel('teste.xlsx')

