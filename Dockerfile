# Usa python3 como base
FROM python:3-slim-stretch
 
RUN apt-get update -y && apt-get install -y build-essential
RUN pip install --upgrade pip
 
COPY api_bemol.py /app/
COPY customer_segment.csv /app/
COPY requirements.txt /app/
 
WORKDIR /app/
 
# Instala dependencias
RUN pip install -r requirements.txt
 
# Porta de exposicao
EXPOSE 8081
 
# Excuta a aplicacao
CMD ["python", "api_bemol.py"] 
