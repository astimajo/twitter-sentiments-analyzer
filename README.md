**CS50 Final Project - Swish.io Tweets Sentiment Analyzer**

This project is a web application where users can input a certain topic in twitter
like a Hashtag, username, or a specific event going on, and the application will 
perform sentiments analysis on the Tweets that were scraped. I built this project 
as I am an aspiring Data Scientist and handling tons of data is one of my primary 
exercises, I also want to largely expand my knowledge of Python and be able to use
Data Analysis tool therefore I practiced heavily using APIs like Twitter API, 
Google Cloud API and experimented with a few others like Quandl API, Yahoo Finance API
and a few others.

The Tweetscraper can gather around 900 tweets but I limited the web app to scrape 100
for the meantime as the internet in my country is quite slower than average and scraping
900 tweets as I have tried took significantly long times. So for the purpose of demonstration
the app will scrape around 100 tweets, perform sentiments analysis, save the csv locally then 
automatically save them a Public Gdrive page where the csv contains more detailed
information on the tweets such as metadata and etc.

**information rows contained in the csv:**

tweet.text, tweet.user.screen_name, tweet.created_at, tweet.user.location, 
tweet.retweet_count, tweet.favorite_count, sentiment, language


**VERY Important Requirements:**
- Twitter Developer Account (approved Dev access and API credentials) to be filled inside tweetscraper_test.py. 
- Google Cloud Platform Account (Gdrive API key) in client_secrets.json.
- Linux OS is preferred to avoid runtime errors (to be dockerized in future iteration to avoid such issue).

**Technologies used to Implement the Project:**
- Python3
- Flask
- Tweepy
- TextBlob
- PyDrive
- HTML/CSS/Javascript
- Heavily W3.css


**How it Works?**
Put a filename with a .csv extension, then input your desired topic or subject matter
then wait for the web page to process the request (can take a bit of time as this requires
a lot of backend processing with APIs and etc and Internet speed).

**Flask Routing**
Each Route in app.py is mainly used for rendering html files and their respective css and js
dependencies. the most specialized portion within is the Analysis html route which contains
all the necessary functions for the scraping, analysis, file writing and storage to work.

**Senstitive Information**
The tweets contained in the csv file contains very sensitive information data, and requires
a pinch of salt when handling. all tweets csv files are stored in a gdrive page and locally 
for only relevant purposes, in this purpose: Demonstration only.

**Future Improvements**
- More Machine learning frameworks like tensorflow and sklearn to be applied for more advanced apps
- Making the API key change available on the UI to make the app more user-friendly.
- Deployment to Docker to make sure of uniform runtime on all systems and configs.
- launching the web app to a hosting service for easy access/on the go use.
- renaming some variables in jinja2 and python to improve readability.

**How to launch the Application**
1. install pip3 if none (sudo apt install python3-pip -y).
2. Clone the repository (git clone https://github.com/astimajo/swishio-tweetsentimentanalyzer.git).
3. run (pip3 install -r requirements.txt) to install all required packages.
4. go to the directory where the clone is stored using cd command.
5. run (flask run) or (python3 app.py) and a browser window will appear.

**Citations and Credits:**

- Tweetscraper script by A. Ablazo, © 2017 (inside tweetscraper_test.py with modifications by Angelo Timajo (me)).
- Web Design look and ideas from Joselle Collado (css design trend).
- DevOps and Tech stack consultation from Mr. Adamson Dela Cruz. 

