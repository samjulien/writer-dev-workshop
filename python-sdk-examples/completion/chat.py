from writerai import Writer
import dotenv

dotenv.load_dotenv()

client = Writer()

def main():
    try:
        response = client.chat.chat(
            messages=[
                {
                    "role": "user",
                    "content": "You are an expert at writing concise product descriptions for an E-Commerce Retailer"
                },
                {
                    "role": "assistant",
                    "content": "Okay, great I can help write these descriptions. Do you have a specific product in mind?"
                },
                {
                    "role": "user",
                    "content": "Please write a one sentence product description for a cozy, stylish sweater suitable for both casual and formal occasions"
                }
            ],
            model="palmyra-x-004",
            stream=False
        )
        
        print(response)
        print(response.choices[0].message.content)
        
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()