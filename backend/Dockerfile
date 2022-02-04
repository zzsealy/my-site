FROM python:3.7.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app -p
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt -i  https://mirrors.aliyun.com/pypi/simple/
# CMD python manage.py runserver 0.0.0.0:3000
