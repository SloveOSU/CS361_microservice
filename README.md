### Steven Love
 11/10/2022
 CS361 - Oregon State - Fall 2022


### Home Library Checkout Microservice Content:
 - About
 - Features
 - Technologies
 - Requirements
 - Usage

### About:
This is a test microservice for a school assignment. This program is a pretend home library checkout service

### Features:
Maintain when loaned media assets are to be returned

### Technologies
Flask web framework
datetime library

### Usage:
This microservice consists of a single endpoint that accepts a POST request containing a numeric value 
A date object is then formated to represent today's date in a numeric value within range of 1 and 366.
Calculations are then performed to determine the return date and days until return is due


#### /checkout POST
Request: JSON {allowed_days_checkout : value}
Response: JSON {date_due : value, days_left_until_return : value}
