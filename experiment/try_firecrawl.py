# Install with pip install firecrawl-py
from firecrawl import FirecrawlApp
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('FIRECRAWL_API_KEY')
if not api_key:
    raise ValueError("FIRECRAWL_API_KEY not found in environment variables")

try:
    app = FirecrawlApp(api_key=api_key)
    
    response = app.scrape_url(
        url='https://docs.firecrawl.dev/features/crawl',
        params={
            'formats': ['markdown'],
            'wait': True  # Wait for the crawl to complete
        }
    )
    
    print("Response status:", response.status_code)
    print("Response content:", response.text)
    
except Exception as e:
    print(f"Error occurred: {str(e)}")
    if hasattr(e, 'response'):
        print(f"Response status code: {e.response.status_code}")
        print(f"Response text: {e.response.text}")