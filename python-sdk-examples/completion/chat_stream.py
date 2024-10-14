from writerai import Writer
import dotenv

dotenv.load_dotenv()

client = Writer()

def main():
    try:
        chat = client.chat.chat(
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
            stream=True,
            logprobs=True,
            stream_options={
                "include_usage": True
            }
        )
        
        response_text=""
        for chunk in chat:
            if len(chunk.choices) > 0 and chunk.choices[0].delta.content is not None:
                response_text += chunk.choices[0].delta.content
        
        print(response_text)
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()