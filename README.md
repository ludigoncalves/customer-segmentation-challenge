# bemol-challenge
Este projeto foi construído para o desafio para a vaga de AI Engineer na Bemol.

Mais informações sobre o projeto podem ser encontradas nos notebooks `preprocessamento.ipynb` e `segmentacao.ipynb`.

## Notebooks
1. `preprocessamento.ipynb` - notebook usado para preprocessamento da base de dados Online Retail
2. `segmentacao.ipynp` - notebook usado para aplicação de abordagens de segmentação: 1) A segmentação conhecida como RFM (Recency, Frequency and Monetary agrupadas), famosa no meio do Marketing e 2) A segmentação feita pelo método não supervisioado de aprendizado de maquina K-Means, com base nas métricas geradas para a classificação do RFM.

## Artefatos Gerados
1. `customer_segment.csv` - arquivo gerado com segmentos para cada cliente gerado a partir do notebook `segmentacao.ipynp.
2. `uk_preprocessed_data.csv` - base de dados preprocessada relativa ao país Reino Unido (utilizado na análise). Gerado a partir do notebook `preprocessamento.ipynp


## Requerimentos
* Este programa executa em python 3.7.4 e necessita das seguintes bibliotecas:
***Para executar localmente***
  1. Flask - `pip install flask`
  2. Pandas - `pip install pandas`
  3. Executar API - `python api_bemol.py`
 
* Instruções para execução do Docker
***Para executar em um container Docker***
  1. Criar a imagem do container - `docker build --tag bemol_api .`
  2. Executar o container com a API - `docker run -p 8081:8081 bemol_api`

 
## Como Executar Testes
* Para executar testes no browser, substituir o valor de ids por um ou mais ids separados por vírgula - `http://localhost:8081/fetch?ids=14467,112`
* Para executar testes no terminal - `curl http://localhost:8081/fetch?ids=14467,112`
  - Saída para o exemplo citado: `[{"Customer": 14467, "Segment": 123}, {"Customer": 112, "Segment": -1}]`



