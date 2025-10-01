from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    welcome_message = "Welcome to my weather app"
    html_content = f"""
    <p>{welcome_message}</p>
    <p>Click below to enter get-city route</p>
    <form action="/get-city">
        <button type="submit">Go</button>
    </form>
    """
    return html_content

@app.route("/get-city")
def get_city():
    html_content = """
        <form action="/city-weather" method="get">
            <p>Please enter a longitude?</p>
            <input type="int" name="longitude" required>
            <p>Please enter a latitude</p>
            <input type="int" name="latitude" required>
            <button type="submit">Submit</button>
        </form>
    """
    return html_content

@app.route("/city-weather")
def city_weather():
    latitude = request.args.get("latitude", "42")
    longitude = request.args.get("longitude", "17")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    html_content = f"""
        <p>{data}</p>
        <p>Click below to go back home</p>
        <form action="/">
            <button type="submit">Go Home</button>
        </form>
    """
    return html_content

if __name__ == "__main__":
    app.run()