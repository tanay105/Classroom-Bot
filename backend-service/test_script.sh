#!/bin/bash
python3 manage.py test api --with-coverage --cover-package=api --verbosity=1
bash <(curl -s https://codecov.io/env)
