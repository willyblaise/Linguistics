import requests
import json
import os

q = input("Enter Search Term: ")
apikey = os.getenv("NEWS_API_KEY")
url_template = "https://newsdata.io/api/1/news?apikey={}&q={}&language=en"
url = url_template.format(apikey, q)

def get_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        json_data = response.json()
        print(json.dumps(json_data, indent=2))  # Pretty print JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

if __name__ == "__main__":
    get_news(url)
