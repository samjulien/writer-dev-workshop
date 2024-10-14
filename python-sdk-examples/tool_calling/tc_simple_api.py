import json
import requests
import os
from writerai import Writer
import dotenv

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
    }
]
print("question: what is the revenue for interstellar?")
messages = [{"role": "user", "content": "what is the revenue for interstellar?"}]
print("-"*100)

response = client.chat.chat(
    model="palmyra-x-004", messages=messages, tools=tools, tool_choice="auto", stream=False
)

response_message = response.choices[0].message
messages.append(response_message)

print(f"Tool calls response: {response_message}\n")
print("-"*100)

tool_calls = response_message.tool_calls
if tool_calls:
    tool_call = tool_calls[0]
    tool_call_id = tool_call.id
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)

    # call api function
    if function_name == "get_movie_info":
        function_response = get_movie_info(function_args["title"])
        print(f"Response from API:\n{function_response}")
        print("-"*100)

        # add the function response to messages
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call_id,
                "name": function_name,
                "content": function_response,
            }
        )

        # get the final response from model
        final_response = client.chat.chat(
            model="palmyra-x-004", messages=messages, stream=False
        )
        print(f"Final response:\n{final_response.choices[0].message.content}\n")
    else:
        print(f"Error: function {function_name} not found")
else:
    # if no function call, just print the response from model
    print(response_message.content)