from consulta_empresa import  select

for main_key, sub_dict in select.items():
    for sub_key, value in sub_dict.items():
        print(f"Chave: {sub_key}, Valor: {value}")