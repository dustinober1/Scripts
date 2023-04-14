import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def download_image(url, output_dir, image_number):
    try:
        response = requests.get(url, stream=True, timeout=10)

        if response.status_code == 200:
            with open(os.path.join(output_dir, f'f22_image_{image_number}.jpg'), 'wb') as f:
                for chunk in response.iter_content(8192):
                    f.write(chunk)
            print(f'Successfully downloaded image {image_number}: {url}')
        else:
            print(f'Failed to download image {image_number}: {url}')

    except requests.exceptions.RequestException as e:
        print(f'Error downloading image {image_number}: {e}')

search_term = "F-22 site:images.google.com"
output_dir = 'f22_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_count = 10  # Number of images to download
image_number = 0

for url in search(search_term, num_results=image_count * 2, lang='en'):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img', {'class': 'rg_i'})

        for img_tag in img_tags:
            img_url = img_tag.get('src') or img_tag.get('data-src')
            if img_url:
                download_image(img_url, output_dir, image_number)
                image_number += 1
                if image_number >= image_count:
                    break

        if image_number >= image_count:
            break

    except Exception as e:
        print(f'Error processing URL "{url}": {e}')

if image_number < image_count:
    print(f'Only {image_number} images were downloaded.')
