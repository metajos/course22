import requests
import zipfile
import os
import sys


def download_file_from_dropbox(dropbox_url, local_file_path):
    """
    Download a file from a Dropbox direct link.
    """
    if "dl=0" in dropbox_url:
        dropbox_url = dropbox_url.replace("dl=0", "dl=1")

    response = requests.get(dropbox_url, stream=True)
    content_type = response.headers.get("Content-Type")
    print(f"Content-Type of the downloaded file: {content_type}")

    if response.status_code == 200:
        with open(local_file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded file size: {os.path.getsize(local_file_path)} bytes")
        return True
    else:
        print(f"Failed to download: {response.status_code}")
        return False


def extract_zip(zip_path, extract_to):
    """
    Extract a ZIP file to a specified directory.
    """
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Files extracted to: {extract_to}")
    except zipfile.BadZipFile:
        print("Error: Bad ZIP file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    local_zip_path = "downloaded_file.zip"  # Temporary ZIP file name
    dropbox_link = "https://www.dropbox.com/scl/fo/425zzgdlh7bypklujm0so/h?rlkey=50noat4zhmpn4mnugminqk7vu&dl=0"
    folder_name = os.getcwd()  # Current directory

    if download_file_from_dropbox(dropbox_link, local_zip_path):
        if zipfile.is_zipfile(local_zip_path):
            extract_zip(local_zip_path, folder_name)
        else:
            print("The downloaded file is not a ZIP archive.")
    else:
        print("Failed to download the file.")


if __name__ == "__main__":
        main()
