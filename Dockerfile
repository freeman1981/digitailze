FROM ubuntu
RUN apt update && apt install nano -y && apt install vim -y
WORKDIR /usr/src/app/
