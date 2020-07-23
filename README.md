# bemol-challenge
Este projeto foi construído para o desafio para a vaga de AI Engineer na Bemol.

Mais informações sobre o projeto podem ser encontradas no notebook `eda_e_segmentacao.ipynb`.

## Requerimentos
Este programa executa em python 3.7.4 e necessita das seguintes bibliotecas:
 1. Flask - `pip install flask`
 2. Pandas - `pip install pandas`
 
## Como executar
* Para iniciar a API - `python api_bemol.py`
* Para executar testes no browser, substituir o valor de ids por um ou mais ids separados por vírgula - `http://localhost:8081/fetch?ids=14467,112`
* Para executar testes no terminal - `curl http://localhost:8081/fetch?ids=14467,112`



