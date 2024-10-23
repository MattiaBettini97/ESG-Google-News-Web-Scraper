import time
import ssl
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import random



def news(link):
    
    user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51', # this one is the one used
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
    ]
    
    headers = {'User-Agent': random.choice(user_agents)}
    req = Request(link, headers=headers)
    context = ssl._create_unverified_context()  # Use this if you want to bypass SSL verification
    retries = 0
    max_retries = 5
    while retries < max_retries:
        try:
            # Attempt to open the URL
            response = urlopen(req, context=context)
            webpage = response.read()
            soup = BeautifulSoup(webpage, 'html5lib')
            #print("Page successfully loaded")

            # Process the webpage content...
            # Break the loop if the request was successful
            return soup
        
        except (URLError, ssl.SSLError) as e:
            retries += 1
            # Check for the Retry-After header if present (in case of rate-limiting)
            retry_after = response.headers.get('Retry-After') if 'response' in locals() else None
            if retry_after:
                print(f"Retry-After header detected. Waiting for {retry_after} seconds before retrying...")
                time.sleep(int(retry_after))
            print(f"Error encountered: {e}. Retrying in 10 seconds...")
            time.sleep(10)  # Pause for 10 seconds before retrying
    print("Max retries exceeded. Skipping this request.")
    return None