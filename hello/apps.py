from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Trading Website (Setting Up Candle Data Soon)"

if __name__ == '__main__':
    app.run(debug=True)
