import requests

url = "https://api.nasa.gov/planetary/apod"  # url for NASA planetary data api
params = {
    "api_key": "aFDopeewTYcb45medLtkipu6mHCdbFrv4L0017aT",
}


response = requests.get(url, params=params, timeout=15)
response.raise_for_status()
data = response.json()


title = data.get("title", "N/A")
date = data.get("date", "N/A")
explanation = data.get("explanation", "N/A")

image_url = data.get("url")

print("Title:", title)
print("Date:", date)
print("Explanation:", (explanation[:200] + "...") if isinstance(explanation, str) else explanation)
print("Image URL:" if image_url else "Resource URL:", image_url or "Not available")
