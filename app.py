from flask import Flask, jsonify, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__)  # Ensure the Flask instance is named 'app'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/candles/<interval>')
def get_candles(interval):
    # Dummy data for now (replace with TraderMade API later)
    data = [
        {"timestamp": "2025-03-17 01:55", "open": 2991.15, "high": 3000.20, "low": 2987.17, "close": 2998.77, "rsi": 51.52}
    ] * 24  # Simulate 24 hours
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
