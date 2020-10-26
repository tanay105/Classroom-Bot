#!/bin/bash
python3 manage.py test api --with-coverage --cover-package=api --verbosity=1
echo "before running the code upload command"
curl -s https://codecov.io/bash > .codecov
chmod +x .codecov
./.codecov -t a85a0034-2212-4d8a-95f4-5b96615080e8 -f .coverage
echo "after running the code upload command"
cp .coverage /shared/
echo "ls in bot_server folder\n"
ls -lha /bot_server/
echo "ls in shared folder\n"
ls -lha /shared/

