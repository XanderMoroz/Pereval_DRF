Pereval-API body { font-family: Trebuchet MS, sans-serif; font-size: 15px; color: #444; margin-right: 24px; } h1 { font-size: 25px; } h2 { font-size: 20px; } h3 { font-size: 16px; font-weight: bold; } hr { height: 1px; border: 0; color: #ddd; background-color: #ddd; } .app-desc { clear: both; margin-left: 20px; } .param-name { width: 100%; } .license-info { margin-left: 20px; } .license-url { margin-left: 20px; } .model { margin: 0 0 0px 20px; } .method { margin-left: 20px; } .method-notes { margin: 10px 0 20px 0; font-size: 90%; color: #555; } pre { padding: 10px; margin-bottom: 2px; } .http-method { text-transform: uppercase; } pre.get { background-color: #0f6ab4; } pre.post { background-color: #10a54a; } pre.put { background-color: #c5862b; } pre.delete { background-color: #a41e22; } .huge { color: #fff; } pre.example { background-color: #f3f3f3; padding: 10px; border: 1px solid #ddd; } code { white-space: pre; } .nickname { font-weight: bold; } .method-path { font-size: 1.5em; background-color: #0f6ab4; } .up { float:right; } .parameter { width: 500px; } .param { width: 500px; padding: 10px 0 0 20px; font-weight: bold; } .param-desc { width: 700px; padding: 0 0 0 20px; color: #777; } .param-type { font-style: italic; } .param-enum-header { width: 700px; padding: 0 0 0 60px; color: #777; font-weight: bold; } .param-enum { width: 700px; padding: 0 0 0 80px; color: #777; font-style: italic; } .field-label { padding: 0; margin: 0; clear: both; } .field-items { padding: 0 0 15px 0; margin-bottom: 15px; } .return-type { clear: both; padding-bottom: 10px; } .param-header { font-weight: bold; } .method-tags { text-align: right; } .method-tag { background: none repeat scroll 0% 0% #24A600; border-radius: 3px; padding: 2px 10px; margin: 2px; color: #FFF; display: inline-block; text-decoration: none; }

Pereval-API
===========

API мобильного приложения Федерации Спортивного Туризма России (ФСТР) с помощью Django Rest Framework.

More information: [https://helloreverb.com](https://helloreverb.com)

Contact Info: [hello@helloreverb.com](hello@helloreverb.com)

Version: 0.1.0

All rights reserved

http://apache.org/licenses/LICENSE-2.0.html

Access
------

1.  HTTP Basic Authentication
2.  APIKey KeyParamName:sessionid KeyInQuery:true KeyInHeader:false

Methods
-------

\[ Jump to [Models](#__Models) \]

### Table of Contents

#### [Schema](#Schema)

*   [`get /schema/`](#schemaRetrieve)

#### [SubmitData](#SubmitData)

*   [`post /submitData`](#submitDataCreate)
*   [`patch /submitData/{id}/`](#submitDataPartialUpdate)
*   [`get /submitData/{id}/`](#submitDataRetrieve)
*   [`get /submitData/user__email={email}`](#submitDataUserEmail=List)

Schema
======

[Up](#__Methods)

    get /schema/

(schemaRetrieve)

OpenApi3 schema for this API. Format can be selected via content negotiation.

*   YAML: application/vnd.oai.openapi
*   JSON: application/vnd.oai.openapi+json

### Query parameters

format (optional)

Query Parameter —

lang (optional)

Query Parameter —

### Return type

map\[String, null\]

### Example data

Content-Type: application/json

    {
      "key" : ""
    }

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/vnd.oai.openapi`
*   `application/yaml`
*   `application/vnd.oai.openapi+json`
*   `application/json`

### Responses

#### 200

* * *

SubmitData
==========

[Up](#__Methods)

    post /submitData

(submitDataCreate)

Переопределение метода POST

### Consumes

This API call consumes the following media types via the Content-Type request header:

*   `application/json`
*   `application/x-www-form-urlencoded`
*   `multipart/form-data`

### Request body

body [PerevalAdd](#PerevalAdd) (required)

Body Parameter —

### Query parameters

### Form parameters

beauty\_title (required)

Form Parameter —

title (required)

Form Parameter —

other\_titles (required)

Form Parameter —

connect (required)

Form Parameter —

add\_time (required)

Form Parameter — format: date-time

user (required)

Form Parameter —

coords (required)

Form Parameter —

level\_winter (required)

Form Parameter —

level\_summer (required)

Form Parameter —

level\_autumn (required)

Form Parameter —

level\_spring (required)

Form Parameter —

beauty\_title (required)

Form Parameter —

title (required)

Form Parameter —

other\_titles (required)

Form Parameter —

connect (required)

Form Parameter —

add\_time (required)

Form Parameter — format: date-time

user (required)

Form Parameter —

coords (required)

Form Parameter —

level\_winter (required)

Form Parameter —

level\_summer (required)

Form Parameter —

level\_autumn (required)

Form Parameter —

level\_spring (required)

Form Parameter —

### Return type

[PerevalAdd](#PerevalAdd)

### Example data

Content-Type: application/json

    {
      "level_winter" : "level_winter",
      "level_autumn" : "level_autumn",
      "beauty_title" : "beauty_title",
      "other_titles" : "other_titles",
      "level_spring" : "level_spring",
      "title" : "title",
      "level_summer" : "level_summer",
      "add_time" : "2000-01-23T04:56:07.000+00:00",
      "user" : 0,
      "connect" : "connect",
      "coords" : 6
    }

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/json`

### Responses

#### 201

[PerevalAdd](#PerevalAdd)

* * *

[Up](#__Methods)

    patch /submitData/{id}/

(submitDataPartialUpdate)

Класс работы с БД для второго спринта: редактирование перевала

### Path parameters

id (required)

Path Parameter —

### Consumes

This API call consumes the following media types via the Content-Type request header:

*   `application/json`
*   `application/x-www-form-urlencoded`
*   `multipart/form-data`

### Request body

body [PatchedPerevalDetail](#PatchedPerevalDetail) (optional)

Body Parameter —

### Query parameters

### Form parameters

id (optional)

Form Parameter —

status (optional)

Form Parameter —

beauty\_title (optional)

Form Parameter —

title (optional)

Form Parameter —

other\_titles (optional)

Form Parameter —

connect (optional)

Form Parameter —

add\_time (optional)

Form Parameter — format: date-time

level\_spring (optional)

Form Parameter —

level\_summer (optional)

Form Parameter —

level\_autumn (optional)

Form Parameter —

level\_winter (optional)

Form Parameter —

user (optional)

Form Parameter —

coords (optional)

Form Parameter —

id (optional)

Form Parameter —

status (optional)

Form Parameter —

beauty\_title (optional)

Form Parameter —

title (optional)

Form Parameter —

other\_titles (optional)

Form Parameter —

connect (optional)

Form Parameter —

add\_time (optional)

Form Parameter — format: date-time

level\_spring (optional)

Form Parameter —

level\_summer (optional)

Form Parameter —

level\_autumn (optional)

Form Parameter —

level\_winter (optional)

Form Parameter —

user (optional)

Form Parameter —

coords (optional)

Form Parameter —

### Return type

[PerevalDetail](#PerevalDetail)

### Example data

Content-Type: application/json

    {
      "level_winter" : "level_winter",
      "other_titles" : "other_titles",
      "title" : "title",
      "level_autumn" : "level_autumn",
      "beauty_title" : "beauty_title",
      "level_spring" : "level_spring",
      "id" : 0,
      "level_summer" : "level_summer",
      "add_time" : "2000-01-23T04:56:07.000+00:00",
      "user" : "",
      "connect" : "connect",
      "coords" : "",
      "status" : "N"
    }

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/json`

### Responses

#### 200

[PerevalDetail](#PerevalDetail)

* * *

[Up](#__Methods)

    get /submitData/{id}/

(submitDataRetrieve)

Класс работы с БД для второго спринта: извлечение детальной информации о перевале

### Path parameters

id (required)

Path Parameter —

### Query parameters

### Return type

[PerevalDetail](#PerevalDetail)

### Example data

Content-Type: application/json

    {
      "level_winter" : "level_winter",
      "other_titles" : "other_titles",
      "title" : "title",
      "level_autumn" : "level_autumn",
      "beauty_title" : "beauty_title",
      "level_spring" : "level_spring",
      "id" : 0,
      "level_summer" : "level_summer",
      "add_time" : "2000-01-23T04:56:07.000+00:00",
      "user" : "",
      "connect" : "connect",
      "coords" : "",
      "status" : "N"
    }

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/json`

### Responses

#### 200

[PerevalDetail](#PerevalDetail)

* * *

[Up](#__Methods)

    get /submitData/user__email={email}

(submitDataUserEmail=List)

Класс работы с БД для второго спринта: вывод всех записей по email

### Path parameters

email (required)

Path Parameter —

### Query parameters

### Return type

array\[[AuthEmailPereval](#AuthEmailPereval)\]

### Example data

Content-Type: application/json

    [ {
      "level_winter" : "level_winter",
      "level_autumn" : "level_autumn",
      "beauty_title" : "beauty_title",
      "other_titles" : "other_titles",
      "level_spring" : "level_spring",
      "title" : "title",
      "level_summer" : "level_summer",
      "add_time" : "2000-01-23T04:56:07.000+00:00",
      "connect" : "connect",
      "coords" : ""
    }, {
      "level_winter" : "level_winter",
      "level_autumn" : "level_autumn",
      "beauty_title" : "beauty_title",
      "other_titles" : "other_titles",
      "level_spring" : "level_spring",
      "title" : "title",
      "level_summer" : "level_summer",
      "add_time" : "2000-01-23T04:56:07.000+00:00",
      "connect" : "connect",
      "coords" : ""
    } ]

### Produces

This API call produces the following media types according to the Accept request header; the media type will be conveyed by the Content-Type response header.

*   `application/json`

### Responses

#### 200

* * *

Models
------

\[ Jump to [Methods](#__Methods) \]

### Table of Contents

1.  [`AuthEmailPereval`](#AuthEmailPereval)
2.  [`Nested`](#Nested)
3.  [`PatchedPerevalDetail`](#PatchedPerevalDetail)
4.  [`PerevalAdd`](#PerevalAdd)
5.  [`PerevalDetail`](#PerevalDetail)
6.  [`StatusEnum`](#StatusEnum)

### `AuthEmailPereval` [Up](#__Models)

beauty\_title

[String](#string)

title

[String](#string)

other\_titles

[String](#string)

connect (optional)

[String](#string)

add\_time

[Date](#DateTime) format: date-time

coords

[](#)

level\_winter (optional)

[String](#string)

level\_summer (optional)

[String](#string)

level\_autumn (optional)

[String](#string)

level\_spring (optional)

[String](#string)

### `Nested` [Up](#__Models)

id

[Integer](#integer)

fam (optional)

[String](#string)

name (optional)

[String](#string)

email (optional)

[String](#string) format: email

otc

[String](#string)

phone

[String](#string)

user

[Integer](#integer)

### `PatchedPerevalDetail` [Up](#__Models)

Сериализатор перевала(детальный)

id (optional)

[Integer](#integer)

status (optional)

[StatusEnum](#StatusEnum)

beauty\_title (optional)

[String](#string)

title (optional)

[String](#string)

other\_titles (optional)

[String](#string)

connect (optional)

[String](#string)

add\_time (optional)

[Date](#DateTime) format: date-time

level\_spring (optional)

[String](#string)

level\_summer (optional)

[String](#string)

level\_autumn (optional)

[String](#string)

level\_winter (optional)

[String](#string)

user (optional)

[](#)

coords (optional)

[](#)

### `PerevalAdd` [Up](#__Models)

Сериализатор перевалов

beauty\_title

[String](#string)

title

[String](#string)

other\_titles

[String](#string)

connect (optional)

[String](#string)

add\_time

[Date](#DateTime) format: date-time

user

[Integer](#integer)

coords

[Integer](#integer)

level\_winter (optional)

[String](#string)

level\_summer (optional)

[String](#string)

level\_autumn (optional)

[String](#string)

level\_spring (optional)

[String](#string)

### `PerevalDetail` [Up](#__Models)

Сериализатор перевала(детальный)

id

[Integer](#integer)

status (optional)

[StatusEnum](#StatusEnum)

beauty\_title

[String](#string)

title

[String](#string)

other\_titles

[String](#string)

connect (optional)

[String](#string)

add\_time

[Date](#DateTime) format: date-time

level\_spring (optional)

[String](#string)

level\_summer (optional)

[String](#string)

level\_autumn (optional)

[String](#string)

level\_winter (optional)

[String](#string)

user

[](#)

coords

[](#)

### `StatusEnum` [Up](#__Models)
