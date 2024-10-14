from writerai import Writer
import math
import dotenv

dotenv.load_dotenv()

client = Writer()

# Define the math functions
def calculate_square_root(number):
    return math.sqrt(number)

def calculate_factorial(number):
    return math.factorial(number)

# Define the tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_square_root",
            "description": "Calculate the square root of a number",
            "parameters": {
                "type": "object",
                "properties": {
                    "number": {"type": "number", "description": "The number to calculate the square root of"}
                },
                "required": ["number"]
            }
        }
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

# Set up the conversation
messages = [{"role": "user", "content": "What's the square root of 16 and the factorial of 5?"}]

response = client.chat.chat(
    model="palmyra-x-004", messages=messages, tools=tools, tool_choice="auto", stream=False
)

response_message = response.choices[0].message
messages.append(response_message)

print(f"Tool call response message object:\n{response_message}\n")

# Process the response and handle tool calls
tool_calls = response_message.tool_calls
for tool_call in tool_calls:
    if tool_call.function.name == "calculate_square_root":
        number = eval(tool_call.function.arguments)["number"]
        function_response = calculate_square_root(number)
    elif tool_call.function.name == "calculate_factorial":
        number = eval(tool_call.function.arguments)["number"]
        function_response = calculate_factorial(number)
    
    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": str(function_response),
        }
    )

final_response = client.chat.chat(
    model="palmyra-x-004", messages=messages, stream=False
)

print(f"final_response: {final_response.choices[0].message.content}")