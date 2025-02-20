# Install with pip install firecrawl-py
from firecrawl import FirecrawlApp
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variables
api_key = os.getenv('FIRECRAWL_API_KEY')
if not api_key:
    raise ValueError("FIRECRAWL_API_KEY not found in environment variables")

try:
    app = FirecrawlApp(api_key=api_key)
    
    # Using the correct parameters as per documentation
    response = app.crawl_url(
        'https://docs.uniswap.org/contracts/v4/overview',
        params={
            'scrapeOptions': {'formats': ['markdown']},
            'limit': 100  # Optional: limit the number of pages to crawl
        }
    )
    
    print("Response:", response)
    
except Exception as e:
    print(f"Error occurred: {str(e)}")
    if hasattr(e, 'response'):
        print(f"Response status code: {e.response.status_code}")
        print(f"Response text: {e.response.text}")