From python:3.6 
WORKDIR /main/web
ADD . /main/web
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
COPY supervisor.conf /etc/supervisor/conf.d/
