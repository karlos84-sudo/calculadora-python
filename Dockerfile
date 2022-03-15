# FROM python:3.9.6-alpine3.13
# #WORKDIR D:\Backup_Ericsson_20210708\Documents\Globant\CursoDevOps\Tareas\Docker\Calculadora
# WORKDIR /Calculadora
# COPY . .
# RUN apk update
# RUN python -m pip install
# RUN python -m pip install --upgrade pi
# RUN pip install -r requirements.txt
# RUN pip install flask
# EXPOSE 9080
# CMD [ "python", "pf_flask_calculadora_api.py" ]

FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
RUN pip install flask

EXPOSE 9080
CMD ["python", "/app/pf_flask_calculadora_api.py"]
