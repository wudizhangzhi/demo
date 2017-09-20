From python:3.6 
WORKDIR /main/web
ADD ./web /main/web
RUN pip install -r web/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com && python manage.py collectstatic --noinput


