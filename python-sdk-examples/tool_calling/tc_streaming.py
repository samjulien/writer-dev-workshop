import json
import requests
from writerai import Writer
import dotenv
import os
import math
dotenv.load_dotenv()

client = Writer()

def get_movie_info(title):
    omdb_api_key = os.getenv("OMDB_API_KEY")
    url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={title}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return f"Failed to retrieve movie info. Status code: {response.status_code}"

def calculate_factorial(number):
    return math.factorial(number)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_movie_info",
            "description": "Get information about a movie by its title",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the movie to retrieve information for",
                    }
                },
                "required": ["title"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_factorial",
            "description": "Calculate the factorial of a number",
            "parameters": {
                "type": "object",
                "properties": {
                    "number": {"type": "integer", "description": "The number to calculate the factorial of"}
                },
                "required": ["number"]
            }
        }
    }
]
print("question: what is the revenue for interstellar and what is the factorial of 5?")
messages = [{"role": "user", "content": "What's the revenue for interstellar and what is the factorial of 5?"}]
# print("question: what is the fastest way to get to the moon?")
# messages = [{"role": "user", "content": "What's the fastest way to get to the moon?"}]
print("-"*100)

response = client.chat.chat(
    model="palmyra-x-004", 
    messages=messages, 
    tools=tools, 
    tool_choice="auto",
    stream=True
)

streaming_content = ""
function_calls = []

for chunk in response:
    choice = chunk.choices[0]

    if choice.delta:
        if choice.delta.tool_calls:
            for tool_call in choice.delta.tool_calls:
                if tool_call.id:
                    function_calls.append(
                        {"name": "", "arguments": "", "call_id": tool_call.id}
                    )
                if tool_call.function:
                    function_calls[-1]["name"] += (
                        tool_call.function.name
                        if tool_call.function.name
                        else ""
                    )
                    function_calls[-1]["arguments"] += (
                        tool_call.function.arguments
                        if tool_call.function.arguments
                        else ""
                    )
        elif choice.delta.content:
            streaming_content += choice.delta.content
            print(choice.delta.content, end="", flush=True)

        # A finish reason of stop means the model has finished generating the response
        if choice.finish_reason == "stop":
            messages.append({"role": "assistant", "content": streaming_content})
        
        # A finish reason of tool_calls means the model has finished deciding which tools to call
        elif choice.finish_reason == "tool_calls":
            print(f"collated function_calls: {function_calls}")
            for function_call in function_calls:
                if function_call["name"] == "get_movie_info":
                    arguments_dict = json.loads(function_call["arguments"])
                    function_response = get_movie_info(arguments_dict["title"])
                    print(f"Response from API:\n{function_response}")
                    print("-"*100)
                    messages.append(
                        {
                        "role": "tool",
                        "content": function_response,
                        "tool_call_id": function_call["call_id"],
                        "name": function_call["name"],
                    }
                )
                elif function_call["name"] == "calculate_factorial":
                    arguments_dict = json.loads(function_call["arguments"])
                    function_response = calculate_factorial(arguments_dict["number"])
                    print(f"Response from factorial:\n{function_response}")
                    print("-"*100)
                    messages.append(
                        {
                        "role": "tool",
                        "content": str(function_response),
                        "tool_call_id": function_call["call_id"],
                        "name": function_call["name"],
                    }
                )
            final_response = client.chat.chat(
                model="palmyra-x-004", messages=messages, stream=True
            )
            final_streaming_content = ""
            for chunk in final_response:
                choice = chunk.choices[0]
                if choice.delta and choice.delta.content:
                    final_streaming_content += choice.delta.content
                    print(choice.delta.content, end="", flush=True)
            # print(final_streaming_content)