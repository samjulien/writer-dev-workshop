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
    stream=True
)

streaming_content = ""
function_calls = []

for chunk in response:
    choice = chunk.choices[0]

    if choice.delta:
        # Check for tool calls
        if choice.delta.tool_calls:
            for tool_call in choice.delta.tool_calls:
                if tool_call.id:
                    # Append an empty dictionary to the function_calls list with the tool call ID
                    function_calls.append(
                        {"name": "", "arguments": "", "call_id": tool_call.id}
                    )
                if tool_call.function:
                    # Append function name and arguments to the last dictionary in the function_calls list
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
        # Handle non-tool-call content
        elif choice.delta.content:
            streaming_content += choice.delta.content

        # A finish reason of stop means the model has finished generating the response
        if choice.finish_reason == "stop":
            messages.append({"role": "assistant", "content": streaming_content})

        # A finish reason of tool_calls means the model has finished deciding which tools to call
        elif choice.finish_reason == "tool_calls":
            for function_call in function_calls:
                if function_call["name"] == "calculate_mean":
                    arguments_dict = json.loads(function_call["arguments"])
                    function_response = calculate_mean(arguments_dict["numbers"])

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

                print(final_streaming_content)
                # The mean is 5
