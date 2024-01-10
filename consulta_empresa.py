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
            'Construção Pesada':[],
            'Engenharia Consultiva':[],
            'Material Aeronáutico e de Defesa':[],
            'Material Rodoviário':[],
            'Motores, Compressores e Outros':[],
            'Máq. e Equip. Industriais':[],
            'Máq. e Equip. Construção e Agrícolas':[],
            'Armas e Munições':[],
            'Linhas Aéreas de Passageiros':[],
            'Transporte Ferroviário':[],
            'Transporte Hidroviário':[],
            'Transporte Rodoviário':[],
            'Exploração de Rodovias':[],
            'Serviços de Apoio e Armazenagem':[],
            'Serviços Diversos':[],
            'Material de Transporte':[]
            
        },
    'Consumo não Ciclico':
        {
            'Agricultura':[],
            'Açucar e Alcool':[],
            'Carnes e Derivados':[],
            'Alimentos Diversos':[],
            'Cervejas e Refrigerantes':[],
            'Produtos de Cuidado Pessoal':[],
            'Produtos de Limpeza':[],
            'Alimentos':[]
        },
    
    'Consumo Cíclico':
        {
            'Incorporações':[],
            'Fios e Tecidos':[],
            'Vestuário':[],
            'Calçados':[],
            'Acessórios':[],
            'Eletrodomésticos':[],
            'Móveis':[],
            'Utensílios Domésticos':[],
            'Automóveis e Motocicletas':[],
            'Hotelaria':[],
            'Restaurante e Similares':[],
            'Bicicletas':[],
            'Brinquedos e Jogos':[],
            'Produção de Eventos e Shows':[],
            'Viagens e Turismo':[],
            'Atividades Esportivas':[],
            'Serviços Educacionais':[],
            'Aluguel de Carros':[],
            'Programas de Fidelização':[],
            'Tecidos, Vestuário e Calçados':[],
            'Produtos Diversos':[]
        },
    
    'Saúde':
        {
            'Medicamentos e Outros':[],
            'Serviços Médicos - Hospitalares':[],
            'Equipamentos':['BALM3.SA']
        },
    'Tecnologia da Informação':
        {
            'Computadores e Equipamentos':[],
            'Programas e Serviços':[]
        },
    'Comunicações':
        {
            'Telecomunicações':[],
            'Publicidade e Propaganda':[]
        },
    'Utilidade Pública':
        {
           'Energia Elétrica':[],
           'Água e Saneamento':[],
           'Gás':[]
        },
    'Financeiro':
        {
            'Bancos':[],
            'Soc. Crédito e Financiamento':[],
            'Soc. Arrendamento Mercantil':[],
            'Securitizadoras de Recebíveis':[],
            'Gestão de Recursos e Investimentos':[],
            'Serviços Financeiros Diversos':[],
            'Seguradoras':[],
            'Resseguradoras':[],
            'Corretoras de Seguros e Resseguros':[],
            'Exploração de Imóveis':[],
            'Intermediação Imobiliária':[],
            'Holdings Diversificadas':[],
            'Outros Títulos':[]
        },
    'Outros':
        {
            'Outros':[]
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
print(media_balance_sheet('Saúde',"Equipamentos",'Working Capital'))