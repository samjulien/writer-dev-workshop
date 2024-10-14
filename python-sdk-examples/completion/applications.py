from writerai import Writer
import dotenv
import os
dotenv.load_dotenv()

client = Writer()

def main():
    try:
        application_generate_content_response = client.applications.generate_content(
            application_id=os.getenv("APPLICATION_ID"),
            inputs=[
            {
                "id": "Product description",
                "value": [
                    "Terra running shoe"
                ]
            }
        ],
        )
        print(application_generate_content_response)
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()