FROM python:3.7.9-stretch

RUN mkdir /bot_server
COPY bot_server/ bot_server/
COPY execute.sh /bot_server/execute.sh
COPY test_script.sh /bot_server/test_script.sh
WORKDIR /bot_server
RUN mkdir ./static/
RUN chmod +x execute.sh
RUN pip3 install -r requirements.txt
CMD ["/bin/bash", "test_script.sh"]
