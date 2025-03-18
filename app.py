from flask import Flask, jsonify, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/candles/<interval>')
def get_candles(interval):
    data = [
        {"timestamp": "2025-03-17 01:55", "open": 2991.15
