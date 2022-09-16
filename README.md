
<!doctype html>
<html>
  <head>
    <title>Pereval-API</title>
    <style type="text/css">
      body {
      	font-family: Trebuchet MS, sans-serif;
      	font-size: 15px;
      	color: #444;
      	margin-right: 24px;
      }
      
      h1	{
      	font-size: 25px;
      }
      h2	{
      	font-size: 20px;
      }
      h3	{
      	font-size: 16px;
      	font-weight: bold;
      }
      hr	{
      	height: 1px;
      	border: 0;
      	color: #ddd;
      	background-color: #ddd;
      }
      
      .app-desc {
        clear: both;
        margin-left: 20px;
      }
      .param-name {
        width: 100%;
      }
      .license-info {
        margin-left: 20px;
      }
      
      .license-url {
        margin-left: 20px;
      }
      
      .model {
        margin: 0 0 0px 20px;
      }
      
      .method {
        margin-left: 20px;
      }
      
      .method-notes	{
      	margin: 10px 0 20px 0;
      	font-size: 90%;
      	color: #555;
      }
      
      pre {
        padding: 10px;
        margin-bottom: 2px;
      }
      
      .http-method {
       text-transform: uppercase;
      }
      
      pre.get {
        background-color: #0f6ab4;
      }
      
      pre.post {
        background-color: #10a54a;
      }
      
      pre.put {
        background-color: #c5862b;
      }
      
      pre.delete {
        background-color: #a41e22;
      }
      
      .huge	{
      	color: #fff;
      }
      
      pre.example {
        background-color: #f3f3f3;
        padding: 10px;
        border: 1px solid #ddd;
      }
      
      code {
        white-space: pre;
      }
      
      .nickname {
        font-weight: bold;
      }
      
      .method-path {
        font-size: 1.5em;
        background-color: #0f6ab4;
      }
      
      .up {
        float:right;
      }
      
      .parameter {
        width: 500px;
      }
      
      .param {
        width: 500px;
        padding: 10px 0 0 20px;
        font-weight: bold;
      }
      
      .param-desc {
        width: 700px;
        padding: 0 0 0 20px;
        color: #777;
      }
      
      .param-type {
        font-style: italic;
      }
      
      .param-enum-header {
      width: 700px;
      padding: 0 0 0 60px;
      color: #777;
      font-weight: bold;
      }
      
      .param-enum {
      width: 700px;
      padding: 0 0 0 80px;
      color: #777;
      font-style: italic;
      }
      
      .field-label {
        padding: 0;
        margin: 0;
        clear: both;
      }
      
      .field-items	{
      	padding: 0 0 15px 0;
      	margin-bottom: 15px;
      }
      
      .return-type {
        clear: both;
        padding-bottom: 10px;
      }
      
      .param-header {
        font-weight: bold;
      }
      
      .method-tags {
        text-align: right;
      }
      
      .method-tag {
        background: none repeat scroll 0% 0% #24A600;
        border-radius: 3px;
        padding: 2px 10px;
        margin: 2px;
        color: #FFF;
        display: inline-block;
        text-decoration: none;
      }
    </style>
  </head>
  <body>
  <h1>Pereval-API</h1>
    <div class="app-desc">API мобильного приложения Федерации Спортивного Туризма России (ФСТР) с помощью Django Rest Framework.</div>
    <div class="app-desc">More information: <a href="https://helloreverb.com">https://helloreverb.com</a></div>
    <div class="app-desc">Contact Info: <a href="hello@helloreverb.com">hello@helloreverb.com</a></div>
    <div class="app-desc">Version: 0.1.0</div>
    
    <div class="license-info">All rights reserved</div>
    <div class="license-url">http://apache.org/licenses/LICENSE-2.0.html</div>
  <h2>Access</h2>
    <ol>
      <li>HTTP Basic Authentication</li>
      <li>APIKey KeyParamName:sessionid KeyInQuery:true KeyInHeader:false</li>
    </ol>

  <h2><a name="__Methods">Methods</a></h2>
  [ Jump to <a href="#__Models">Models</a> ]

  <h3>Table of Contents </h3>
  <div class="method-summary"></div>
  <h4><a href="#Schema">Schema</a></h4>
  <ul>
  <li><a href="#schemaRetrieve"><code><span class="http-method">get</span> /schema/</code></a></li>
  </ul>
  <h4><a href="#SubmitData">SubmitData</a></h4>
  <ul>
  <li><a href="#submitDataCreate"><code><span class="http-method">post</span> /submitData</code></a></li>
  <li><a href="#submitDataPartialUpdate"><code><span class="http-method">patch</span> /submitData/{id}/</code></a></li>
  <li><a href="#submitDataRetrieve"><code><span class="http-method">get</span> /submitData/{id}/</code></a></li>
  <li><a href="#submitDataUserEmail&#x3D;List"><code><span class="http-method">get</span> /submitData/user__email&#x3D;{email}</code></a></li>
  </ul>

  <h1><a name="Schema">Schema</a></h1>
  <div class="method"><a name="schemaRetrieve"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="get"><code class="huge"><span class="http-method">get</span> /schema/</code></pre></div>
    <div class="method-summary"> (<span class="nickname">schemaRetrieve</span>)</div>
    <div class="method-notes"><p>OpenApi3 schema for this API. Format can be selected via content negotiation.</p>
<ul>
<li>YAML: application/vnd.oai.openapi</li>
<li>JSON: application/vnd.oai.openapi+json</li>
</ul>
</div>





    <h3 class="field-label">Query parameters</h3>
    <div class="field-items">
      <div class="param">format (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash;  </div>      <div class="param">lang (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash;  </div>    </div>  <!-- field-items -->


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      
      map[String, null]
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>{
  "key" : ""
}</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/vnd.oai.openapi</code></li>
      <li><code>application/yaml</code></li>
      <li><code>application/vnd.oai.openapi+json</code></li>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    
        
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

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#PerevalAdd">PerevalAdd</a> (required)</div>
      
            <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash;  </div>
                </div>  <!-- field-items -->


    <h3 class="field-label">Query parameters</h3>
    <div class="field-items">
    </div>  <!-- field-items -->

    <h3 class="field-label">Form parameters</h3>
    <div class="field-items">
      <div class="param">beauty_title (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">title (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">other_titles (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">connect (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">add_time (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  format: date-time</div>      <div class="param">user (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">coords (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_winter (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_summer (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_autumn (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_spring (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">beauty_title (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">title (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">other_titles (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">connect (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">add_time (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  format: date-time</div>      <div class="param">user (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">coords (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_winter (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_summer (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_autumn (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_spring (required)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>    </div>  <!-- field-items -->

    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      <a href="#PerevalAdd">PerevalAdd</a>
      
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
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

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">201</h4>
    
        <a href="#PerevalAdd">PerevalAdd</a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="submitDataPartialUpdate"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="patch"><code class="huge"><span class="http-method">patch</span> /submitData/{id}/</code></pre></div>
    <div class="method-summary"> (<span class="nickname">submitDataPartialUpdate</span>)</div>
    <div class="method-notes">Класс работы с БД для второго спринта: редактирование перевала</div>

    <h3 class="field-label">Path parameters</h3>
    <div class="field-items">
      <div class="param">id (required)</div>
      
            <div class="param-desc"><span class="param-type">Path Parameter</span> &mdash;  </div>    </div>  <!-- field-items -->

    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
      <li><code>application/x-www-form-urlencoded</code></li>
      <li><code>multipart/form-data</code></li>
    </ul>

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#PatchedPerevalDetail">PatchedPerevalDetail</a> (optional)</div>
      
            <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash;  </div>
                </div>  <!-- field-items -->


    <h3 class="field-label">Query parameters</h3>
    <div class="field-items">
    </div>  <!-- field-items -->

    <h3 class="field-label">Form parameters</h3>
    <div class="field-items">
      <div class="param">id (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">status (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">beauty_title (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">title (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">other_titles (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">connect (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">add_time (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  format: date-time</div>      <div class="param">level_spring (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_summer (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_autumn (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_winter (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">user (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">coords (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">id (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">status (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">beauty_title (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">title (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">other_titles (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">connect (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">add_time (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  format: date-time</div>      <div class="param">level_spring (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_summer (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_autumn (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">level_winter (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">user (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">coords (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>    </div>  <!-- field-items -->

    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      <a href="#PerevalDetail">PerevalDetail</a>
      
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>{
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
}</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    
        <a href="#PerevalDetail">PerevalDetail</a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="submitDataRetrieve"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="get"><code class="huge"><span class="http-method">get</span> /submitData/{id}/</code></pre></div>
    <div class="method-summary"> (<span class="nickname">submitDataRetrieve</span>)</div>
    <div class="method-notes">Класс работы с БД для второго спринта: извлечение детальной информации о перевале</div>

    <h3 class="field-label">Path parameters</h3>
    <div class="field-items">
      <div class="param">id (required)</div>
      
            <div class="param-desc"><span class="param-type">Path Parameter</span> &mdash;  </div>    </div>  <!-- field-items -->




    <h3 class="field-label">Query parameters</h3>
    <div class="field-items">
    </div>  <!-- field-items -->


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      <a href="#PerevalDetail">PerevalDetail</a>
      
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>{
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
}</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    
        <a href="#PerevalDetail">PerevalDetail</a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="submitDataUserEmail&#x3D;List"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="get"><code class="huge"><span class="http-method">get</span> /submitData/user__email&#x3D;{email}</code></pre></div>
    <div class="method-summary"> (<span class="nickname">submitDataUserEmail&#x3D;List</span>)</div>
    <div class="method-notes">Класс работы с БД для второго спринта: вывод всех записей по email</div>

    <h3 class="field-label">Path parameters</h3>
    <div class="field-items">
      <div class="param">email (required)</div>
      
            <div class="param-desc"><span class="param-type">Path Parameter</span> &mdash;  </div>    </div>  <!-- field-items -->




    <h3 class="field-label">Query parameters</h3>
    <div class="field-items">
    </div>  <!-- field-items -->


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      array[<a href="#AuthEmailPereval">AuthEmailPereval</a>]
      
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>[ {
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
} ]</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    
        
  </div> <!-- method -->
  <hr/>

  <h2><a name="__Models">Models</a></h2>
  [ Jump to <a href="#__Methods">Methods</a> ]

  <h3>Table of Contents</h3>
  <ol>
    <li><a href="#AuthEmailPereval"><code>AuthEmailPereval</code></a></li>
    <li><a href="#Nested"><code>Nested</code></a></li>
    <li><a href="#PatchedPerevalDetail"><code>PatchedPerevalDetail</code></a></li>
    <li><a href="#PerevalAdd"><code>PerevalAdd</code></a></li>
    <li><a href="#PerevalDetail"><code>PerevalDetail</code></a></li>
    <li><a href="#StatusEnum"><code>StatusEnum</code></a></li>
  </ol>

  <div class="model">
    <h3><a name="AuthEmailPereval"><code>AuthEmailPereval</code></a> <a class="up" href="#__Models">Up</a></h3>
    
    <div class="field-items">
      <div class="param">beauty_title </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">title </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">other_titles </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">connect (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">add_time </div><div class="param-desc"><span class="param-type"><a href="#DateTime">Date</a></span>  format: date-time</div>
<div class="param">coords </div><div class="param-desc"><span class="param-type"><a href="#"></a></span>  </div>
<div class="param">level_winter (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_summer (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_autumn (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_spring (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="Nested"><code>Nested</code></a> <a class="up" href="#__Models">Up</a></h3>
    
    <div class="field-items">
      <div class="param">id </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
<div class="param">fam (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">name (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">email (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  format: email</div>
<div class="param">otc </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">phone </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">user </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="PatchedPerevalDetail"><code>PatchedPerevalDetail</code></a> <a class="up" href="#__Models">Up</a></h3>
    <div class='model-description'>Сериализатор перевала(детальный)</div>
    <div class="field-items">
      <div class="param">id (optional)</div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
<div class="param">status (optional)</div><div class="param-desc"><span class="param-type"><a href="#StatusEnum">StatusEnum</a></span>  </div>
<div class="param">beauty_title (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">title (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">other_titles (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">connect (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">add_time (optional)</div><div class="param-desc"><span class="param-type"><a href="#DateTime">Date</a></span>  format: date-time</div>
<div class="param">level_spring (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_summer (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_autumn (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_winter (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">user (optional)</div><div class="param-desc"><span class="param-type"><a href="#"></a></span>  </div>
<div class="param">coords (optional)</div><div class="param-desc"><span class="param-type"><a href="#"></a></span>  </div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="PerevalAdd"><code>PerevalAdd</code></a> <a class="up" href="#__Models">Up</a></h3>
    <div class='model-description'>Сериализатор перевалов</div>
    <div class="field-items">
      <div class="param">beauty_title </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">title </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">other_titles </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">connect (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">add_time </div><div class="param-desc"><span class="param-type"><a href="#DateTime">Date</a></span>  format: date-time</div>
<div class="param">user </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
<div class="param">coords </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
<div class="param">level_winter (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_summer (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_autumn (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_spring (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="PerevalDetail"><code>PerevalDetail</code></a> <a class="up" href="#__Models">Up</a></h3>
    <div class='model-description'>Сериализатор перевала(детальный)</div>
    <div class="field-items">
      <div class="param">id </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
<div class="param">status (optional)</div><div class="param-desc"><span class="param-type"><a href="#StatusEnum">StatusEnum</a></span>  </div>
<div class="param">beauty_title </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">title </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">other_titles </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">connect (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">add_time </div><div class="param-desc"><span class="param-type"><a href="#DateTime">Date</a></span>  format: date-time</div>
<div class="param">level_spring (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_summer (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_autumn (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">level_winter (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
<div class="param">user </div><div class="param-desc"><span class="param-type"><a href="#"></a></span>  </div>
<div class="param">coords </div><div class="param-desc"><span class="param-type"><a href="#"></a></span>  </div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="StatusEnum"><code>StatusEnum</code></a> <a class="up" href="#__Models">Up</a></h3>
    
    <div class="field-items">
          </div>  <!-- field-items -->
  </div>
  </body>
</html>
