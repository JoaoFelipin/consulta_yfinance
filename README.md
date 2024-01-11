# Função de Cálculo de Média do Balanço Patrimonial

## Descrição
A função `media_balance_sheet(setor, segmento, alvo)` calcula a média de um indicador específico para um setor e segmento específicos.

## Parâmetros
- `setor`: O setor para o qual você deseja calcular a média.
- `segmento`: O segmento dentro do setor para o qual você deseja calcular a média.
- `alvo`: O indicador específico que você deseja calcular a média.

## Funcionamento
1. A função primeiro seleciona a lista de tickers para o setor e segmento fornecidos.
2. Em seguida, para cada ticker na lista, a função recupera o balanço patrimonial usando a biblioteca `yfinance`.
3. A função extrai o valor do indicador alvo do balanço patrimonial e adiciona à lista `media`.
4. Finalmente, a função retorna a média dos valores na lista `media`.

## Retorno
A função retorna a média do indicador alvo para o setor e segmento fornecidos.

## Exemplo de Uso
```python
media = media_balance_sheet('Tecnologia', 'Software', 'Total Assets')
print(media)
