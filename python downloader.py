import os
import json
import requests


# Function to download a file from a given URL
def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filename = os.path.join(dest_folder, url.split('/')[-1])
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url}")


# Load URLs from the JSON file
def load_urls(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data['urls']


# Main function
def main():
    json_file = 'links.json'  # JSON file containing URLs
    dest_folder = '.'  # Destination folder for downloads

    urls = load_urls(json_file)
    for url in urls:
        download_file(url, dest_folder)


if __name__ == "__main__":
    main()
