from flask import Flask, request, jsonify, render_template, url_for
import csv, tweepy, os
from textblob import TextBlob
import subprocess as sp
from tweetscraper_test import tweetscraper
from analysis import compute
from gdrive import drive_save_public

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('detect.html')

@app.route('/home')
def home():
    return render_template('detect.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/analyze', methods=["GET","POST"])
def analyze():
    
    #Fetching the user's desired query search
    query = request.form['q']

    #Fetching the required filename
    filename = request.form['text']

    #Calling the Tweetscraper 
    tweetscraper(query, filename)

    #Calling the percentage computation function
    return_list = compute(query)

    #Saving the new csv file to the drive public folder
    drive_save_public(query)
    
    return render_template('analysis.html', a=(return_list[0]), b=(return_list[1]), c=(return_list[2]))

     

if __name__ == '__main__':
    app.run(debug=True)
