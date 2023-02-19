# Trading-Project



This project is a web application that allows a user to upload a CSV file containing financial data (specifically, candles with open, high, low, and close prices, as well as a date and an ID) and a timeframe in minutes. The uploaded file is stored on the Django server and the data is then read into a list of Candle objects. The list of candles is then converted into a new list of candles that represent the timeframe requested by the user. This conversion is done asynchronously to avoid blocking the main thread. The resulting converted data is then stored in a JSON file on the file system. Finally, the user is provided with an option to download the JSON file containing the converted data.

The Django project is named "TradingProject" and it contains a single Django app named "MainApp". The MainApp contains the views and models for the project. The views.py file defines the views that handle the user's interactions with the web application, such as accepting the uploaded file and rendering the response. The models.py file defines the database schema for the Candle object, which has fields for the open, high, low, close prices, date, and ID.

The project utilizes Django's built-in file handling and database capabilities to store and process the uploaded file and candle data. Asynchronous processing is achieved using the Django background task library. Finally, the converted data is stored in a JSON file using Python's built-in json library. The user interface is built using HTML templates and JavaScript to handle file uploading and downloading.




