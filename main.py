from flask import Flask, request
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return 'Welcome to DFScrawl, the crawling app that produces very accurate fanduel player projections'

app.run()
