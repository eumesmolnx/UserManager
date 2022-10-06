# User Manager Software

A Python-Django project API to manage Users with authentication and roles.

**Technologies**:

 - Python 3.10.1
 - Django 4.0.4
 - PostgreSQL 13.5
 - Docker Compose 3.3

## How to Run
1. Build Docker Image
`docker-compose build`
2. Run Docker Container
`docker-compose up`
3. Docker will init **usermgr_app** (Python envoriment) and **usermgr_db** (Postgres database) containers. Python Django access is mapped to **http://localhost:8000**

## Authentication

This API uses JWT Authentication (Access Token) to protect changes (Create, Update and Delete - POST/PUT/DELETE) endpoints only to ADMIN role. User List and Single User endpoints (GET) is accessible to ADMIN and COMMON roles.

## Validations

1. CPF is being validated for valid digits only.
2. Name, Role and Password are Required.
3. Only ADMIN or COMMON roles are valid.
4. Password neeed to be send as plain-text and will be encrypted.

If an error occurs, a 400 response with error information will be displayed.

## Endpoints

1. Login

**Request**

> [POST] /auth/login/

**Body**

>**Type:** form-data
cpf
password

**Response**
>{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NTExODc3OSwiaWF0IjoxNjY1MDMyMzc5LCJqdGkiOiJkMDgwNTY4ZDg5YjQ0MTcyYjRjOThmZDQ3MDU3ZGE2MCIsInVzZXJfaWQiOiI1MGU3ZWY3ZS0zZGZlLTRhMmMtYTg4Yy1iNTVlMGE5YjU0MWMiLCJjcGYiOiIzNjkzODQxOTg1MCJ9.91kzMpgAt_1dHfmrGbQt-Th_HEDNUIk2t7s0HKTsBCA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MDMyNjc5LCJpYXQiOjE2NjUwMzIzNzksImp0aSI6ImFlMDhhMDJlOTllMTRmYjlhNTZlMmRlMjVmYTRhOGMzIiwidXNlcl9pZCI6IjUwZTdlZjdlLTNkZmUtNGEyYy1hODhjLWI1NWUwYTliNTQxYyIsImNwZiI6IjM2OTM4NDE5ODUwIn0.OZpwSkKibclS3D1MzzShTg6CoB7ctgEgl5Od0ouuGPk"
}

The access token need to be used in all changes endpoints as a Bearer Token authentication.

## Usage
1. List All Users

**Request**

> [GET] /user

**Response (200)**
>[  
    {  
        "id": "50e7ef7e-3dfe-4a2c-a88c-b55e0a9b541c",
        "name":  "João Silva"
        "cpf":  "03732936074"
        "role" : "ADMIN"
    },
    {  
        "id": "ba4c07e6-7a7d-4ecf-9778-83465e8c05ad",
        "name":  "Rafael Martins"
        "cpf":  "51764198409"
        "role" : "COMMON"
    },
    ...
]

2. List Single User

**Parameters**
>**id** - User Id (UUID)

**Request**
> [GET] /user/[id]

**Response (200)**
>{  
    "id": "50e7ef7e-3dfe-4a2c-a88c-b55e0a9b541c",
    "name":  "João Silva"
    "cpf":  "03732936074"
    "role" : "ADMIN"
}

3. Register New User

**Request**

> [POST] /user/

**Headers**
>**Access Token:** Bearer

**Body**
>**Type:** application/json

>{
"id": "ba4c07e6-7a7d-4ecf-9778-83465e8c05ad",
"name": "Ricardo Gusman",
"cpf": "96463501190",
"password" : "xxxxxxxx",
"role" : "ADMIN"
}

**Response (200)**
>{ "id": "ba4c07e6-7a7d-4ecf-9778-83465e8c05ad", "name": "Ricardo Gusman", "cpf": "96463501190", "role": "ADMIN" }

4. Update User

**Parameters**
>**id** - User Id (UUID)

**Request**
> [PUT] /user/[id]

**Headers**
>**Access Token:** Bearer

**Body**
>**Type:** application/json

>{
"id": "ba4c07e6-7a7d-4ecf-9778-83465e8c05ad",
"name": "Ricardo Gusman",
"cpf": "96463501190",
"password" : "xxxxxxxx",
"role" : "ADMIN"
}

**Response (200)**
>{ "id": "ba4c07e6-7a7d-4ecf-9778-83465e8c05ad", "name": "Ricardo Gusman", "cpf": "96463501190", "role": "ADMIN" }

5. Delete User

**Request**
> [DELETE] /user/[id]

**Headers**
>**Access Token:** Bearer

>     
**Parameters**
>**id** - User Id (UUID)

**Response**
`200 OK`
