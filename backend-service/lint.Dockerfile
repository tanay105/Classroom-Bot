FROM python:3.7-alpine
COPY bot_server/ bot_server/
WORKDIR /bot_server/
RUN pip install pycodestyle==2.6.0
RUN pip install pep8
RUN pip install flake8

CMD ["pycodestyle", "--max-line-length=150", "--exclude=.pyc", ".", "&&", "pep8", "."]
