FROM python:3.6

RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# run server
RUN chmod 755 /app/entrypoint.sh
CMD [ "/app/entrypoint.sh" ]