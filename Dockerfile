FROM ubuntu
RUN apt update && apt install nano vim tmux less -y
WORKDIR /usr/src/app/
