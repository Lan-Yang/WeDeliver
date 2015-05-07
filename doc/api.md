
`Order`
---------------

### Search for orders
 ***example: GET /v1/order?pickupaddress=Columbia&pickuptime=&offset=...***
 
 **what is this:**
Query and Pagination

 
**Request**

| Parameter  | type   | value (format)   | default|    Note |
|:----------:|:------:|:-------:|:------:|:--------:|
|   pickupaddress|  String    |Columbia|       |      |
|   stopaddress|  String    |NYU|       |      |
|   pickuptime|  String |2011-11-03 18:21:26|    |  |
|cargosize     |  int    | 333| |  |
|   offset |  int    |  1/2/3...|    1   |   used for pagination       |
|   limit  |  int    |     10   |    10  |  used for pagination |


**Response**

***succeed***
```json
{
  "status": 200,
  "data"  : [
            {
              "oid": 1,
              "pickupaddr": "Columbia",
              "pickuptime": "2011-11-03 18:21:26",
              "did": 3,
              "cargosize": 1,
              "trucksize": 800,
              "basefee":333,
              "closefee":333,
              "status":"D",
              "drivername":"XiDaDa",
              "driverphone":"12893012809"
            },
            {
              "oid": 1,
              "pickupaddr": "Columbia",
              "pickuptime": "2011-11-03 18:21:26",
              "did": 3,
              "cargosize": 1,
              "trucksize": 800,
              "basefee":333,
              "closefee":333,
              "status":"D",
              "drivername":"XiDaDa",
              "driverphone":"12893012809"
            }
			...
          ],
  "links":[
            {"ref":"pre","href":"/v1/order?pickupaddress=Columbia&pickuptime=&offset=4&limit=2"},
            {"ref":"next","href":"/v1/order?pickupaddress=Columbia&pickuptime=&limit=2"},
            {"ref":"first","href":"/v1/order?pickupaddress=Columbia&pickuptime=&limit=2"},
            {"ref":"last","href":"/v1/order?pickupaddress=Columbia&pickuptime=&limit＝2"}
         ]
}
```
***fail***
```json
{
  "status":404,
  "data": "Error message"
}

```

### Show one order according to the oid
 ***example: GET /v1/order/329***
 
 **what is this:**
show detail of one specific order

 
**Request**

| Parameter  | type   | value (format)   | default|    Note |
|:----------:|:------:|:-------:|:------:|:--------:|
|   oid |  int|33|       |      |


**Response**

***succeed***
```json
{
  "status": 200,
  "data"  : [
            {
              "oid": 1,
              "pickupaddr": "Columbia",
              "pickuptime": "2011-11-03 18:21:26",
              "did": 3,
              "cargosize": 1,
              "trucksize": 800,
              "basefee":333,
              "closefee":333,
              "status":"D",
              "drivername":"XiDaDa",
              "driverphone":"12893012809"
            }
          ]
}
```
***fail***
```json
{
  "status":404,
  "data": "Error message"
}

```

### Add order
***example: <br>POST /v1/order<br>pickupaddr=Columbia&pickuptime =2011-11-03 18:21:26...***
 
 **what is this:**
add a new order

 
**Request**

| Parameter  | type   | value (format)   | default|    Note |
|:----------:|:------:|:-------:|:------:|:--------:|
|   pickupaddr|  String|Columbia|       |      |
|   pickuptime |  String|2011-11-03 18:21:26|       |      |
|   did |  int|33|       |      |
|   cargosize |  int|33|       |      |
|   trucksize |  int|333|       |      |
|   totalfee |  float|33.33|       |      |
|   basefee |  float|40.0|       |      |
|   closefee |  float|3.5|       |      |
|   status |  String|D|       |      |
|   drivername |  String|Obama|       |      |
|   driverphone |  String|3284733|       |      |


**Response**

***succeed***
```json
{
  "status":201,
  "data": "order creation succeeds"
}
```
***fail***
```json
{
  "status":404,
  "data": "Error message"
}

```

`OrderRecord`
---------------
### Search for OrderRecord given a shipper id
 ***example: GET /v1/orderRecord?sid=33&offset=11&limit=20***
 
 **what is this:**
Get all the OrderRecord of one specific user

 
**Request**

| Parameter  | type   | value (format)   | default|    Note |
|:----------:|:------:|:-------:|:------:|:--------:|
|   sid |  int|33|       |      |
|   offset |  int    |  1/2/3...|    1   |   used for pagination       |
|   limit  |  int    |     10   |    10  |  used for pagination |


**Response**

***succeed***
```json
{
  "status": 200,
  "data"  : [
            {
              "oid": 1,
              "sid": 3,
              "did": 33,
              "stopaddress": "Columbia",
              "delivertime": "2011-11-03 18:21:26",
              "cargosize": 3,
              "fee": 34.5,
              "acceptedtime": "2011-11-03 18:21:26",
              "status": "D",
              "grade": 5.0,
              "commet": "WTF!"
            },
            {
              "oid": 2,
              "sid": 23,
              "did": 33,
              "stopaddress": "Columbia",
              "delivertime": "2011-11-03 18:21:26",
              "cargosize": 3,
              "fee": 34.5,
              "acceptedtime": "2011-11-03 18:21:26",
              "status": "D",
              "grade": 5.0,
              "commet": "WTF!"
            }
			...
          ],
  "links":[
            {"ref":"pre","href":"/v1/orderRecord?sid=33&offset=1&limit=20"},
            {"ref":"next","href":"/v1/orderRecord?sid=33&offset=31&limit=20"},
            {"ref":"first","href":"/v1/orderRecord?sid=33&offset=1&limit=20"},
            {"ref":"last","href":"/v1/orderRecord?sid=33&offset=44&limit=20"}
         ]
}
```
***fail***
```json
{
  "status":404,
  "data": "Error message"
}

```

### Add OrderRecord
***example: <br>POST /v1/orderRecord<br>oid=2&sid=23...***
 
 **what is this:**
add a new order

 
**Request**

| Parameter  | type   | value (format)   | default|    Note |
|:----------:|:------:|:-------:|:------:|:--------:|
|   oid|  int|2|       |      |
|   sid|  int|23|       |      |
|   did |  int|33|       |      |
|   stopaddress|  String|33|       |      |
|   delivertime|  String|2011-11-03 18:21:26|       |      |
|   cargosize|  int|3|       |      |
|   fee|  float|40.0|       |      |
|   acceptedtime|  String|2011-11-03 18:21:26|       |      |
|   status|  String|D|       |      |
|   grade|  float|4.5|       |      |
|   comment|  String|"This is amazing!"|       |      |


**Response**

***succeed***
```json
{
  "status":201,
  "data": "OrderRecord creation succeeds"
}
```
***fail***
```json
{
  "status":404,
  "data": "Error message"
}

```
