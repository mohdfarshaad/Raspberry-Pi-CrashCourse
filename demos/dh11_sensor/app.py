from flask import Flask, render_template
import Adafruit_DHT

app = Flask(__name__)

SENSOR = Adafruit_DHT.DHT11
PIN = 4  # GPIO4 (Pin 7)

@app.route("/")
def index():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    if humidity and temperature:
        data = f"Temp: {temperature:.1f}°C, Humidity: {humidity:.1f}%"
    else:
        data = "Sensor error. Try again."
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
