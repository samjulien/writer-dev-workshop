import os
from writerai import Writer
import dotenv

dotenv.load_dotenv()

client = Writer()

def upload_file_to_writer(file_path, client):
    """
    Uploads a single file to Writer (specified by pathname)
    and returns its id.
    """

    # Open and read the file's contents
    with open(file_path, 'rb') as file_obj:
        file_contents = file_obj.read()

    # Upload the file
    file = client.files.upload(
        content=file_contents,
        content_disposition=f"attachment; filename={os.path.basename(file_path)}",
        content_type="image/png",
    )

    return file.id

def main():
    file_id = upload_file_to_writer("Writer.png", client)
    print(f"File uploaded with ID: {file_id}")

if __name__ == "__main__":
    main()