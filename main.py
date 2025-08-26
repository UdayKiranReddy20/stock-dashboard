from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/history")
def history():
    symbol = request.args.get("symbol", "TATAMOTORS")
    now = datetime.datetime.now()
    
    # Mock OHLCV data (last 30 minutes, 1-min interval)
    data = []
    price = 450
    for i in range(30):
        ts = now - datetime.timedelta(minutes=(30 - i))
        open_p = price + random.uniform(-2, 2)
        close_p = open_p + random.uniform(-2, 2)
        high_p = max(open_p, close_p) + random.uniform(0, 1)
        low_p = min(open_p, close_p) - random.uniform(0, 1)
        volume = random.randint(1000, 5000)
        price = close_p
        data.append({
            "time": ts.strftime("%H:%M"),
            "open": round(open_p, 2),
            "high": round(high_p, 2),
            "low": round(low_p, 2),
            "close": round(close_p, 2),
            "volume": volume
        })

    return jsonify({"symbol": symbol, "data": data})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
