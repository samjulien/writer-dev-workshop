from writerai import Writer
import dotenv
import os
dotenv.load_dotenv()

client = Writer()

tools = [
    {
        "type": "graph",
        "function": {
            "description": "product descriptions",
            "graph_ids": [
                os.getenv("GRAPH_ID")
            ],
            "subqueries": True
        }
    }
]

print("KG Question FC: Which of our products contain either food coloring or chocolate?")
messages = [{"role": "user", "content": "Which of our products contain either food coloring or chocolate?"}]

response = client.chat.chat(
    model="palmyra-x-004", 
    messages=messages, 
    tools=tools, 
    tool_choice="auto", 
    stream=True
)

print(f"response: {response}")

response_text=""
for chunk in response:
    if chunk.choices[0].delta.content is not None:
        response_text += chunk.choices[0].delta.content
        print(chunk.choices[0].delta.content, end="", flush=True)

print(response_text)