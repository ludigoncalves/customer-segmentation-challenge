# -*- coding: utf-8 -*-

import json
from flask import Flask, request, Response
from http import HTTPStatus

import pandas as pd # biblioteca para processamento dos dados

rfm_dict = dict()

# initializing and setup
app = Flask(__name__)

# routes

# aggregate API entry
@app.route('/fetch', methods=["GET"])
def fetch():
    """
    Processa chamada pra funcao
    """
    result_list = list()
    
    customer_ids = request.args['ids'].split(',')
    
    for i in customer_ids:
        ans = fetch_customer_segment(int(i))
        
        result = dict()
        result = {'Customer': None, 'Segment': None}
          
        result['Customer'] = ans[0]
        result['Segment'] = ans[1]
        
        result_list.append(result)
    
    # creating response
    response = Response(
        json.dumps(result_list),
        content_type = "application/json; charset=utf-8")
    
    code=200
    return response, code

def fetch_customer_segment(customer_id):
    if customer_id in rfm_dict:

        return (customer_id, rfm_dict[customer_id])
    else:

        return (customer_id, -1)

# 
def load_data():
    global rfm_dict
    # Carrega a tabela rfm salva
    rfm = pd.read_csv("rfm_table_no_outlier.csv", index_col=['CustomerID'])
    
    # Constroi dicionario para consulta rapida
    rfm_dict = rfm['RFM'].to_dict()
    
# starting server
if __name__ == "__main__":
    load_data()

    app.run(host='localhost', debug=True, port=8081)
