# Pereval-API

API мобильного приложения Федерации Спортивного Туризма России (ФСТР) с помощью Django Rest Framework.
Version: 0.1.0

подробнее https://app.swaggerhub.com/apis/MOROZ070688/Pereval_API/0.0.0

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SubmitDataApi* | [**submit_data_create**](docs/SubmitDataApi.md#submit_data_create) | **POST** /submitData | Добавление перевала
*SubmitDataApi* | [**submit_data_partial_update**](docs/SubmitDataApi.md#submit_data_partial_update) | **PATCH** /submitData/{id}/ |  Редактирование перевала
*SubmitDataApi* | [**submit_data_retrieve**](docs/SubmitDataApi.md#submit_data_retrieve) | **GET** /submitData/{id}/ | Извлечение данных о перевале
*SubmitDataApi* | [**submit_data_user_email_list**](docs/SubmitDataApi.md#submit_data_user_email_list) | **GET** /submitData/user__email&#x3D;{email} | Извлечение списка перевалов пользователя

</div> <!-- method -->
  <hr/>
  <h1><a name="SubmitData">SubmitData</a></h1>
  <div class="method"><a name="submitDataCreate"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="post"><code class="huge"><span class="http-method">post</span> /submitData</code></pre></div>
    <div class="method-summary"> (<span class="nickname">submitDataCreate</span>)</div>
    <div class="method-notes">Переопределение метода POST</div>


    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
      <li><code>application/x-www-form-urlencoded</code></li>
      <li><code>multipart/form-data</code></li>
    </ul>
 <!--Todo: process Response Object and its headers, schema, examples -->
    <h3 class="field-label">Request body example data</h3>
  
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>{
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
}</code></pre>
