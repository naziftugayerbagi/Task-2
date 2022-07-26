# Task-2
This project only takes the data from the provided URL page
The function called `fetch_data`is doing every webscrapping part.
Under this functions Headers are provided so that it can be seen on different browsers.
In order to get the data properly BeaautifulSoup and requests are used.
This algorithm search the product names and prices under their class.
try and except part is written in order to avoid some blank spaces (there were 2 blank price)
Flask gets the data and dumps it as json

API RUN

ın order to run the api
In order to run the script, execute the following commands under the directory of the script on the terminal:
`set FLASK_APP=task-2.py`
`flask run`

go to a browser and type following url in order to see data that has been scraped
`http://localhost:5000/items`
