FROM debian
RUN apt update && apt install nano -y && install vim -y
WORKDIR /usr/src/app/
