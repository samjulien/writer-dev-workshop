import os
from writerai import Writer
import dotenv

dotenv.load_dotenv()

client = Writer()

def download_file_from_writer(file_id, filename, client):
    """
    Downloads a file from Writer and saves it to the specified filename.
    """
    file_bytes = client.files.download(file_id)
    # For text files
    # file_string = file_bytes.read().decode("utf-8")
    with open(filename, "wb") as file:
        file.write(file_bytes.read())

def main():
    file_id = os.getenv("FILE_ID")
    download_file_from_writer(file_id, "Writer-test.png", client)
    print(f"File downloaded with ID: {file_id}")

if __name__ == "__main__":
    main()