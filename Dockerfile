FROM ubuntu
RUN apt update && apt install nano vim tmux less tree sudo -y \
    && adduser --disabled-password --gecos "" sterx \
    && adduser --disabled-password --gecos "" some_user \
    && usermod -aG root sterx

WORKDIR /usr/src/app/

# RUN mkdir -p lesson{1..4}  # TODO разобраться - не работает
RUN mkdir lesson4

# lesson4.29.3
RUN cd lesson4 \
    && mkdir -p something/one/two \
    && touch something/one/two/somefile \
    && chmod 777 something \
    && chown sterx:sterx something/one \
    && chmod u=rw,go=rx something/one \
    && chown sterx:sterx something/one/two \
    && chmod u=rwx,go=rx something/one/two \
    && chown sterx:sterx something/one/two/somefile \
    && chmod ugo=rwx something/one/two/somefile
