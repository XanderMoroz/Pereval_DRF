# home-iot-api
The API for the EatBacon IOT project

## Version: 1.0.0

### /devices

#### GET
##### Description:

returns all registered devices

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| skip | query | number of records to skip | No | integer |
| limit | query | max number of records to return | No | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | All the devices |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | successfully registered device |

### /lighting/dimmers/{deviceId}/{value}

#### POST
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| deviceId | path |  | Yes | string |
| value | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | response |

### /lighting/dimmers/{deviceId}/{value}/timer/{timeunit}

#### POST
##### Description:

sets a dimmer to a specific value on a timer

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| deviceId | path |  | Yes | string |
| value | path |  | Yes | integer |
| timeunit | path |  | Yes | integer |
| units | query |  | No | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | response |

### /lighting/switches/{deviceId}

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| deviceId | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | response |

### /lighting/switches/{deviceId}/{value}

#### POST
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| deviceId | path |  | Yes | string |
| value | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | response |

### /lighting/switches/{deviceId}/{value}/timer/{minutes}

#### POST
##### Description:

sets a switch to a specific value on a timer

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| deviceId | path |  | Yes | string |
| value | path |  | Yes | string |
| minutes | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | response |

### /lightingSummary

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | ok |

### /temperature

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | ok |

### /temperature/forecast/{days}

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| days | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | the forecast |

### /temperature/{zoneId}

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| zoneId | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Zone temperature |

### /temperature/{zoneId}/heater

#### GET
##### Description:

gets the state of the heater

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| zoneId | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | heater state |

### /temperature/{zoneId}/heater/{state}

#### POST
##### Description:

turns the heater on or off

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| zoneId | path |  | Yes | string |
| state | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Status of the operation |

### /zones

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | ok |

### /zones/{zoneId}/quiet

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| zoneId | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | ok |
