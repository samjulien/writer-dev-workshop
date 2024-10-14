from writerai import Writer
import dotenv

dotenv.load_dotenv()

client = Writer()

def main():
    try:
        completion = client.completions.create(
            model="palmyra-x-003-instruct",
            prompt="Tell me a joke about Python",
            temperature=0.7,
            stream=False
        )

        print(completion.choices[0].text)
        
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()