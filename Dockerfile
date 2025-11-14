FROM python:3.12-slim

RUN mkdir polygon_denet
WORKDIR /polygon_denet

COPY ./requirements.txt /polygon_denet

RUN pip3 install -r requirements.txt
    

COPY . .

CMD ["sh", "-c", "python3 main.py"]