import requests
import os
import zipfile
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

MODEL = os.getenv('MODEL')

MODEL = MODEL if MODEL in ["en", "en_large", "hi", "hi_large"] else "en_large"

current_file_path = Path(__file__).resolve()


current_file_directory = current_file_path.parent


models_links = {
    "en": ["https://haptik-website-images.haptik.ai/spello_models/en.pkl.zip", "84M", "ec55760a7e25846bafe90b0c9ce9b09f"],
    "en_large": ["https://haptik-website-images.haptik.ai/spello_models/en_large.pkl.zip", "284M", "9a4f5069b2395c9d5a1e8b9929e0c0a9"],
    "hi": ["https://haptik-website-images.haptik.ai/spello_models/hi.pkl.zip", "75M", "ad8681161932fdbb8b1368bb16b9644a"],
    "hi_large": ["https://haptik-website-images.haptik.ai/spello_models/hi_large.pkl.zip", "341M", "0cc73068f88a73612e7dd84434ad61e6"],
}


def download_file(url: str):
    local_filename = f"{current_file_directory}/{url.split('/')[-1]}"
    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        # Open local file with write-binary mode and write contents
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return url.split('/')[-1]


def unzip_file(zip_path: str, extract_to: str = current_file_directory):
    local_zip_path = f"{current_file_directory}/{zip_path}"
    if not os.path.exists(local_zip_path):
        print(f"File {local_zip_path} does not exist.")
        return
    with zipfile.ZipFile(local_zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted: {local_zip_path}")


def clean_up(filename: str):
    local_file_name = f"{current_file_directory}/{filename}"
    if os.path.exists(local_file_name):
        os.remove(local_file_name)
        print(f"Deleted: {local_file_name}")


def main(url: str):
    print(f"Downloading {url}")
    filename = download_file(url)
    print(f"Unzipping {filename}")
    unzip_file(filename)
    print(f"Cleaning up {filename}")
    clean_up(filename)


if __name__ == "__main__":
    main(url=models_links[MODEL][0])
