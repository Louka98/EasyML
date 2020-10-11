# Poetry
## install
- linux: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
- windows (powershell): `(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -`

## first usage
- poetry install
- poetry shell (in vs code you can add it as default interpreter)

## usage
activate env:
- poetry shell
installing a package:
- poetry add package_name_here
uninstall:
- poetry remove package_name