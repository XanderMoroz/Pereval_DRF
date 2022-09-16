# Pereval-API

API мобильного приложения Федерации Спортивного Туризма России (ФСТР) с помощью Django Rest Framework.
Version: 0.1.0

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SubmitDataApi* | [**submit_data_create**](docs/SubmitDataApi.md#submit_data_create) | **POST** /submitData | Добавление перевала
*SubmitDataApi* | [**submit_data_partial_update**](docs/SubmitDataApi.md#submit_data_partial_update) | **PATCH** /submitData/{id}/ |  Редактирование перевала
*SubmitDataApi* | [**submit_data_retrieve**](docs/SubmitDataApi.md#submit_data_retrieve) | **GET** /submitData/{id}/ | Извлечение данных о перевале
*SubmitDataApi* | [**submit_data_user_email_list**](docs/SubmitDataApi.md#submit_data_user_email_list) | **GET** /submitData/user__email&#x3D;{email} | 

## Documentation For Models

 - [AllOfAuthEmailPerevalCoords](docs/AllOfAuthEmailPerevalCoords.md)
 - [AllOfPatchedPerevalDetailCoords](docs/AllOfPatchedPerevalDetailCoords.md)
 - [AllOfPatchedPerevalDetailUser](docs/AllOfPatchedPerevalDetailUser.md)
 - [AllOfPerevalDetailCoords](docs/AllOfPerevalDetailCoords.md)
 - [AllOfPerevalDetailUser](docs/AllOfPerevalDetailUser.md)
 - [AuthEmailPereval](docs/AuthEmailPereval.md)
 - [Nested](docs/Nested.md)
 - [PatchedPerevalDetail](docs/PatchedPerevalDetail.md)
 - [PerevalAdd](docs/PerevalAdd.md)
 - [PerevalDetail](docs/PerevalDetail.md)
 - [StatusEnum](docs/StatusEnum.md)

## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication

## cookieAuth

- **Type**: API key
- **API key parameter name**: sessionid
- **Location**: URL query string


## Author
XanderMoroz

