import requests
import random
from PIL import Image
from io import BytesIO

# Make a GET request to the Unsplash API
response = requests.get('https://api.unsplash.com/photos/random', headers={'Authorization': 'Client-ID YOUR_ACCESS_KEY'})

# Get the URL of the random image
image_url = response.json()['urls']['regular']

# Make a GET request to the image URL
image_response = requests.get(image_url)

# Open the image using PIL
image = Image.open(BytesIO(image_response.content))
image.show()
