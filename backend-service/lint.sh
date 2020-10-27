#!/bin/bash
pycodestyle --max-line-length=150 --exclude=.pyc .
pep8 .
flake8 .
