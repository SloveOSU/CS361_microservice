# Steven Love
 11/10/2022
 CS361 - Oregon State - Fall 2022


# Library Checkout Microservice Content:
 - About
 - Endpoints


# About:
 This endpoint accepts a POST request containing a numeric value representing checkout length
 A date object is then formated to represent today's date in a numeric value within range of 1 and 366.
 Calculations are then performed to determine the return date and days until return is due


# /checkout POST
 Request: JSON {allowed_days_checkout : value}
 Response: JSON {date_due : value, days_left_until_return : value}
