import requests
from bs4 import BeautifulSoup


url = input("Could you please tell me what site you want the links from? ")
# Send an HTTP GET request to the URL you want to scrape

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now, you can extract data from the HTML using BeautifulSoup
    # Let's say you want to extract all the links on the page
    links = soup.find_all('a')
    
    for link in links:
        print(link.get('href'))

else:
    print('Failed to retrieve the web page. Status code:', response.status_code)