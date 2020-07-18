
## Requirements

    python 3.8
    docker
    docker-composer

## Run

    docker-compose build
    docker-compose up
    

## Using

Sign in:

    curl -X POST \
      http://localhost/fetch-stock-data-api/auth/register \
      -H 'cache-control: no-cache' \
      -H 'content-type: application/json' \
      -d '{
      "first_name": "Felipe",
      "last_name": "Rodrigues",
      "login": "felipernx",
      "password": "123456",
      "email": "rodrigues882007@gmail.com"
      
    }'
    
Sign up:

    curl -X POST \
      http://localhost/fetch-stock-data-api/auth/login \
      -H 'cache-control: no-cache' \
      -H 'content-type: application/json' \
      -d '{
      "login": "felipernx",
      "password": "123456"
    }'     

Call stock information endpoint:

    curl -X GET \
      http://localhost/fetch-stock-data-api/stock/<STOCK_ID> \
      -H 'Authorization: Basic {{JWT TOKEN}} \
      -H 'cache-control: no-cache' \
      -H 'content-type: application/json'
    
## Tests
Run unit tests

    python3 -m unittest