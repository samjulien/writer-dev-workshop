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
    model="palmyra-x-004", messages=messages, tools=tools, tool_choice="auto", stream=False
)
print(f"response: {response}")
response_message = response.choices[0].message
print(f"response_message: {response_message}")