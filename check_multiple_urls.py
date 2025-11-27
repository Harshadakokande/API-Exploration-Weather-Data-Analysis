import requests
import emoji

# Function to check the status of a single URL
def check_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f'{url} : {response.status_code} {emoji.emojize(":thumbs_up:")} - OK')
        else:
            print(f'{url} : {response.status_code} {emoji.emojize(":thumbs_down:")} - {response.reason}')
    except requests.exceptions.RequestException as e:
        print(f'{url} : Error {emoji.emojize(":thumbs_down:")} - {e.__class__.__name__}: {e}')

# Accepting multiple URLs from user input
