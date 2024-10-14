import json
import dotenv
from writerai import Writer

dotenv.load_dotenv()

client = Writer()

def calculate_mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)

tools = [
    { 
        "type": "function",
        "function": {
            "name": "calculate_mean", 
            "description": "Calculate the mean (average) of a list of numbers.", 
            "parameters": { 
                "type": "object", 
                "properties": { 
                    "numbers": { 
                        "type": "array", 
                        "items": {"type": "number"}, 
                        "description": "List of numbers"
                    } 
                }, 
                "required": ["numbers"] 
            } 
        }
    }
]

messages = [{"role": "user", "content": "what is the mean of [1,3,5,7,9]?"}]

response = client.chat.chat(
    model="palmyra-x-004", 
    messages=messages, 
    tools=tools, 
    tool_choice="auto", 
    stream=False
)

response_message = response.choices[0].message
tool_calls = response_message.tool_calls
if tool_calls:
    tool_call = tool_calls[0]
    tool_call_id = tool_call.id
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)

    if function_name == "calculate_mean":
        function_response = calculate_mean(function_args["numbers"])

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call_id,
            "name": function_name,
            "content": str(function_response),
        })

final_response = client.chat.chat(
    model="palmyra-x-004", 
    messages=messages, 
    stream=False
 )

print(f"Final response: \n{final_response.choices[0].message.content}\n")
# Final response: "The mean is 5"