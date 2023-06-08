FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./nrg.ft .
COPY ./nrg.py .
COPY ./start.sh .

RUN chmod 775 *

EXPOSE ${NRG_PORT}

CMD ["sh", "./start.sh"]