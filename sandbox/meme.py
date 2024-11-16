'''
flask app for displaying random memes from r/memes on reddit
'''
from flask import Flask, render_template #importing the flask library
import requests #importing the requests library in http and html version
import json  #importing json library

app = Flask(__name__)
def get_memes(): #defining function for getting memes using the request and json library
	url="https://meme-api.com/gimme"
	response= json.loads(requests.request("GET",url).text)
	meme_preview=response["preview"][-2]
	subreddit=response["subreddit"]
	return meme_preview,subreddit #return function
@app.route('/')
def index(): #defining function
	meme_pic,subreddit=get_memes()
	return render_template("memes.html",meme_pic=meme_pic,subreddit=subreddit)

app.run(host="127.0.0.1",port=5000, threaded=True,debug=True)
