FROM python:3

# Instalar dependências do sistema operacional
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential

COPY . /RobotzProject
WORKDIR /RobotzProject

# Instalar mysqlclient antes de instalar requirements.txt
RUN pip install mysqlclient

# Instalar dependências do projeto
RUN pip install -r requirements.txt

CMD python main.py