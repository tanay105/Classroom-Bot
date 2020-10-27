FROM python:3.7-alpine
COPY bot_server/ bot_server/
COPY lint.sh bot_server/lint.sh
WORKDIR /bot_server/
RUN pip install pycodestyle==2.6.0
RUN pip install pep8
RUN pip install flake8
CMD ["/bin/bash", "lint.sh"]
