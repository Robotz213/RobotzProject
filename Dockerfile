FROM python:3

COPY . /RobotzProject
WORKDIR /RobotzProject

RUN pip install -r requirements.txt

CMD python main.py