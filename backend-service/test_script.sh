#!/bin/bash
python3 manage.py test api --with-coverage --cover-package=api --verbosity=1
echo "before running the code upload command"
curl -s https://codecov.io/bash > .codecov
chmod +x .codecov
./.codecov -f .coverage
echo "after running the code upload command"
