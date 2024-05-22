import requests
from bs4 import BeautifulSoup

# Dictionary to store script titles and URLs
scripts = {}

# Function to scrape the scripts
def update_scripts():
    url = 'https://thescriptlab.com/screenwriting-101/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # This will vary based on the actual HTML structure
    for script in soup.find_all('a', class_='script-download-link'):
        title = script.text.strip().lower()
        link = script['href']
        scripts[title] = link

# Call the function to update the script list initially
update_scripts()
