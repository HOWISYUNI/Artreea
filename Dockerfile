FROM ubuntu:18.04

MAINTAINER DEV-GO

RUN apt-get update -y && \
    apt-get install -y \
    nginx \
    python3-dev \
    python3-pip

RUN pip3 install django uwsgi mysqlclient

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/sites-enabled/default
COPY mysite_nginx.conf /etc/nginx/sites-enabled/mysite_nginx.conf

COPY . /mysite/
WORKDIR /mysite/

RUN chmod +x /mysite/docker_start.sh # give permission
CMD /mysite/docker_start.sh

expose 80

# FROM ubuntu:18.04 : DockerHub에는 미리 다양항 설정을 완료한 이미지 들이 공개되어 있으나, 처음 접하는 입장에서 다른사람들이 셋팅해놓은 이미지를 활용하기도 어렵고, 원리도 이해가 가지 않기 때문에 여기서는 기본 ubuntu만 설치되어 있는 이미지를 이용 합니다.

# RUN apt-get ... : 필수적인 리눅스 패키지 들을 설치 합니다. apt-get update를 수행해야 apt-get이 패키지 리스트를 업데이트 하여 우리가 원하는 패키지를 설치할 수 있습니다. python, nginx, pip 를 설치하였습니다.

# RUN pip3 install ... : 필요한 파이썬 패키지를 설치 합니다. django와 서버 구동시 필요한 uwsgi를 설치합니다.

# RUN echo "deamon off;" ... : nginx를 데몬으로 실행시 동작이 멈춘다고 합니다(참조)

# RUN rm -rf ... : nginx의 기본 설정을 제거 합니다.

# COPY mysite_nginx.conf ... : 앞장에서 준비해 준 nginx 설정 파일을 docker 이미지의 nginx 설정파일의 위치에 복사 합니다.

# COPY . /mysite/ : 현재위치(프로젝트 폴더, dockerfile이 존재하는 폴더) 의 내용을 docker 이미지의 /mysite/로 복사 합니다.

# WORKDIR /mysite/ : CMD로 인한 명령은 /mysite/의 위치에서 동작합니다.

# RUN chmod +x ... : 앞장에서 준비한 docker_start.sh을 실행할 수 있도록 권한을 부여합니다.

# CMD /mysite/docker_start.sh : docker_start.sh를 실행시켜 nginx 와 uwsgi를 동작시켜 서버를 구동시킵니다.

# EXPOSE 80 : 컨테이너의 80번 포트를 개방 합니다.