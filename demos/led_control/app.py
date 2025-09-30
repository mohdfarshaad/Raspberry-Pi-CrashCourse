from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# Setup GPIO
LED_PIN = 17  # GPIO17 (Pin 11)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/on")
def turn_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return render_template("index.html", message="LED is ON")

@app.route("/off")
def turn_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return render_template("index.html", message="LED is OFF")

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        GPIO.cleanup()
