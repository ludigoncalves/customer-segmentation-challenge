# bemol-challenge
Este projeto foi construído para o desafio para a vaga de AI Engineer na Bemol.

Mais informações sobre o projeto podem ser encontradas nos notebooks `preprocessamento.ipynb` e `segmentacao.ipynb`.


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



