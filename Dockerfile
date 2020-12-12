FROM python
USER root
RUN mkdir -p /usr/app/FlaskAPI
RUN mkdir -p /usr/app/deploy
RUN chmod -R 777 /usr/app/deploy
WORKDIR /usr/app/FlaskAPI/
COPY . .
RUN pip3 install --no-cache-dir -r /usr/app/FlaskAPI/requirements.txt