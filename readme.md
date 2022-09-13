[![GitHub license](https://img.shields.io/badge/implemented%20by-Andy-blue)](https://www.linkedin.com/in/andy-kiaka-76a983110/)

## Approach
it's just a test

1. Virtual environment
   
    Each developer has their preferences in choosing tools to 
    define a virtual environment, for this implementation I 
    chose to use pipenv which uses Pipfile instead of requirements.txt, 
    however a requirements.txt file will be provided to facilitate 
    other developers to use this Implementation.

## Prerequisites

1. Libraries
   
   As described in the Pipfile and requirements.txt files, 
   the libraries needed to run this implementation are:

    * django==3.2.8
    * djangorestframework==3.12.4
    * drf-yasg==1.20.0    
    * psycopg2-binary==2.9.1

## How to use

1. Build the images by running
    ```
    $ docker-compose up -d --build
    ```
2. Make the migrations
   The implementation comes with the app api migration done, the dev just needs to "migrate"
   ```
   $ docker-compose exec eye_web python manage.py migrate
   ``` 
3. Create a super user
   ```
   $ docker-compose exec eye_web python manage.py createsuperuser
   ```


### Endpoints

All available endpoints together with auto-generated documentation
can be consulted via the link

*   http://localhost:8000/swagger/

Access in the api has the following prefix : http://localhost:8000/api/...

Unusually for this implementation, I created a single dynamic 
endpoint that handles all expected use cases.

Exemplo:

* http://localhost:8000/api/

Tipo de dados:

The api only authorizes the insertion of data on the endpoint http://localhost:8000/api/ following the following example:
        
    {        
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "name": "pageview",
        "data": [
            {
                "host": "www.consumeraffairs.com",
                "path": "/"                
            }
        ],
        "timestamp": "2021-01-01T09:15:27.243860Z"
    }

      or

    {        
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "name": "pageview",
        "data": [
            {
                "host": "www.consumeraffairs.com",
                "path": "/",
                "element": "chat bubble"                
            }
        ],
        "timestamp": "2021-01-01T09:15:27.243860Z"
    }

        or

    {        
        "session_id": "d0ee6b24-e21c-46e5-882a-a48ff51da189",
        "category": "form interaction",
        "name": "submit",
        "data": [
            {
                "host": "www.consumeraffairs.com",
                "path": "/",                
                "form": [
                    {
                        "first_name": "John",
                        "last_name": "Doe"
                    }
                ]
            }
        ],
        "timestamp": "2021-10-13T04:16:44Z"
    }

NB: For all lists, the parser expect a dictionary inside it 
    (make sure to follow the pattern for the variables "data" and "form"). 

## Author ✒️

* **Andy Kiaka** - *Job Completo* - [detona115](https://github.com/detona115)

---
⌨️ com ❤️ por [detona115](https://github.com/detona115) 😊
