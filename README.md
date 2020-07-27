# Position REST API

OpenAPI specification 2.0 were used to create this REST API.
Python "Connexion" library is used to generate routes end endpoints.

## Project dev environment setup

1. Handle environment variable:
```
export APP_SETTINGS=development
```
*NB: "APP_SETTINGS" values can be 'development', 'testing' or 'production'.*

2. Create virtual environment:
```
python3 -m venv venv
```

3. Activate virtual environment:
```
source venv/bin/activate
```
*NB: Use `deactivate` command to deactivate virtual environment.*

4. Install requirements in virtual environment:
```
pip install -r requirements.txt
```

## Other useful commands

Run tests
```
export APP_SETTINGS=testing
python3 -m unittest
```

Run api (dev server)
```
python3 main.py
```
*NB: SwaggerUI can be accessed here: http://0.0.0.0:8000/api/ui*

Build Docker image
```
docker build -t position_api .
```

Run app in a Docker container
```
docker run -e "APP_SETTINGS=development" -p "8000:8000" position_api
```
*NB: SwaggerUI can be accessed here: http://0.0.0.0:8000/api/ui*
