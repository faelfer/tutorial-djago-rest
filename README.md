# Bttr

![GitHub issue](https://img.shields.io/github/issues/faelfer/bttr-client-react)
![GitHub forks](https://img.shields.io/github/forks/faelfer/bttr-client-react)
![GitHub stars](https://img.shields.io/github/stars/faelfer/bttr-client-react)
![GitHub license](https://img.shields.io/github/license/faelfer/bttr-client-react)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)
[![Maintainability](https://api.codeclimate.com/v1/badges/0543d3fafe54ce417928/maintainability)](https://codeclimate.com/github/faelfer/bttr-client-react/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0543d3fafe54ce417928/test_coverage)](https://codeclimate.com/github/faelfer/bttr-client-react/test_coverage)
[![codecov](https://codecov.io/gh/faelfer/bttr-client-react/graph/badge.svg?token=NUBTDY3WWI)](https://codecov.io/gh/faelfer/bttr-client-react)
![Twitter Follow](https://img.shields.io/twitter/follow/fael_fer)

Server of the bttr project with Django.

## Run

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary libs and run the project.

```bash
source env/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py runserver
```

## Check Flake8

Use the [Flake8](https://flake8.pycqa.org/en/latest/index.html/) to find and fix problems in Python code.

```bash
flake8 .
```

## Check Black

Use the [Black](https://black.readthedocs.io/en/stable/) to find and fix problems in code formatter.

```bash
black --check
```

```bash
black .
```

## Testing with Jest

Use the [API Test Case](https://www.django-rest-framework.org/api-guide/testing/) to unit tests.

```bash
python manage.py test
```

## Run GitHub Actions locally with act

Use the [act](https://nektosact.com/beginner/index.html) to run GitHub Actions locally.

```bash
act
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
