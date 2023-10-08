FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt || echo "Failed to install requirements."

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "--host=0.0.0.0" ]
