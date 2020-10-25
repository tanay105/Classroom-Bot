#!/bin/bash
python3 manage.py test api --with-coverage --cover-package=api --verbosity=1
echo "before running the code upload command"
bash <(curl -s https://codecov.io/env) -f .coverage
echo "after running the code upload command"
