Issues:
1. url string vs integer
2. ampersands not rendering properly (used auto escape off)
3. json upload and added to database without duplicating

Possible Issues:
There is no validation to check if the POST data in the upload field is json data. Since this application would not be made public
and only used by the company, no validation would be necessary to protect the database from a possible security breach. Unless
it was deemed necessary just in case there is some sort of disgruntled employee.

I left debug mode set to True just in case you need to see what's happening