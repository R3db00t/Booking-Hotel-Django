FROM python:3.10.4
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --upgrade pip
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN python manage.py collectstatic --noinput --clear
RUN python manage.py migrate