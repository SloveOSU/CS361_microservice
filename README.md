### Steven Love
 11/10/2022
 CS361 - Oregon State - Fall 2022


### Home Library Checkout Microservice Content:
 - About
 - Features
 - Technologies
 - Requirements
 - UML Sequence diagram
 - Usage
 - Endpoints
 - Test requests

### About:
This is a test microservice for a school assignment. This program is a pretend home library checkout service

### Features:
Maintain when loaned media assets are to be returned

### Technologies
Flask web framework
datetime library

### Requirements
- Decoding a JSON response

### UML Sequence Diagram
![Microservice UML 1 0](https://user-images.githubusercontent.com/86192388/201176391-86d69567-3f86-42d1-850b-5a28b9e6817b.png)

### Usage:
This microservice consists of a single endpoint that accepts a POST request containing a numeric value. 
A date object is then formated to represent today's date in a numeric value within range of 1 and 366.
Calculations are then performed to determine the return date and days until return is due.
The response object includes data for the return date and the days left until media is due for return.

### Endpoints:
#### /checkout POST
- Request: JSON {allowed_days_checkout : value}
- Response: JSON {date_due : value, days_left_until_return : value}

### Test requests:
Request: 
```
curl -X POST 127.0.0.1:47774/checkout -H 'Content-Type: application/json' -d '{"allowed_days_checkout":"5"}'
```
Response:
```
{
    "date_due": 319, 
    "days_left_until_return": 5
}
```

