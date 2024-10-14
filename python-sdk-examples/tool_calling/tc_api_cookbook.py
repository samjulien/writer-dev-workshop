from geopy.geocoders import Nominatim
from writerai import Writer
import requests
import dotenv

dotenv.load_dotenv()

client = Writer()

def get_location_from_ip():
    response = requests.get("https://ipinfo.io")
    if response.status_code == 200:
        data = response.json()
        return {
            "city"    : data.get("city", "Unknown"), 
            "region"  : data.get("region", "Unknown"), 
            "country" : data.get("country", "Unknown"),
        }
    else:
        return {
            "city"    : "Unknown", 
            "region"  : "Unknown", 
            "country" : "Unknown",
        }
        
def get_weather_at_location(location_name, use_metric_units=False):

    WEATHER_CODE_TABLE = {
        0:  "clear sky",
        1:  "mainly clear", 
        2:  "partly cloudy",
        3:  "overcast",
        45: "fog",
        48: "depositing rime fog",
        51: "light drizzle",
        53: "moderate drizzle",
        55: "dense drizzle",
        56: "light freezing drizzle",
        57: "dense freezing drizzle",
        61: "slight rain",
        63: "moderate rain",
        65: "heavy rain",
        66: "light freezing rain",
        67: "heavy freezing rain",
        71: "slight snow",
        73: "moderate snow",
        75: "heavy snow",
        77: "snow grains",
        80: "light rain showers",
        81: "moderate rain showers",
        82: "violent rain showers",
        85: "slight snow showers",
        86: "heavy snow showers",
        95: "thunderstorm",
        96: "thunderstorm with slight hail",
        99: "thunderstorm with heavy hail",
    }

    def location_name_to_latlong(location_name):
        geolocator = Nominatim(user_agent="Writer.com tool calling demo notebook")
        location = geolocator.geocode(location_name)
        return (location.latitude, location.longitude)

    def celsius_to_fahrenheit(degrees_celsius):
        return (degrees_celsius * 1.8) + 32

    def kmh_to_mph(kmh):
        return kmh * 0.621371

    latitude, longitude = location_name_to_latlong(location_name)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relativehumidity_2m,weathercode,cloudcover,wind_speed_10m"
    response = requests.get(url)
    data = response.json()
    return {
        "weather"     : WEATHER_CODE_TABLE.get(data["current"]["weathercode"], "unknown"),
        "cloud_cover" : f"{data['current']['cloudcover']}%",
        "temperature" : (f"{data['current']['temperature_2m']:.1f} degrees C" if use_metric_units 
                         else f"{celsius_to_fahrenheit(data['current']['temperature_2m']):.1f} degrees F"),
        "wind_speed"  : (f"{data['current']['wind_speed_10m']:.1f} km/h" if use_metric_units
                         else f"{kmh_to_mph(data['current']['wind_speed_10m']):.1f} mph"),
        "humidity"    : f"{data['current']['relativehumidity_2m']}%",
    }

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_location_from_ip",
            "description": "Get the user's location based on their IP address. If the user asks where they are or says they're lost, use this.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather_at_location",
            "description": "Get the current weather for a given location, which may be a street address, the name of a building, landmark, or destination, or a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "A location, such as an address, a city and province or state with country, or even the name of a reasonably well-known place."
                    }
                },
                "required": [
                    "location"
                ]
            }
        }
    }
]
user_prompt_count = 1
initial_system_message = {
    "role": "system",
    "content": "You are a helpful assistant. Respond concisely and politely to user queries. Use clear, simple language. When asked for technical explanations, provide detailed and accurate information, but avoid jargon. If the user asks for assistance with a task, offer step-by-step guidance."
}
messages = [initial_system_message]

print("""
Sample multi-turn chat completion app
featuring tool calling
=====================================
""")
temperature = float(input("Enter a temperature (0.0 - 2.0) for the chat, or just press 'Enter' for 1.0: ").strip() or 1.0)

while True:
    user_prompt = input(f"[{user_prompt_count}]\nEnter a prompt: ").strip()
    if not user_prompt:
        break

    if user_prompt == "!messages":
        print(f"\nContents of `messages` (this will not be included as part of the conversation):")
        print("-------------------------------------------------------------------------------")
        print(f"{messages}\n\n")
        continue

    user_prompt_count +=1
    user_message = {
        "role": "user",
        "content": user_prompt
    }
    messages.append(user_message)

    # Make initial call to chat() function
    # TODO: Replace this with the production SDK call
    initial_response = client.chat.chat(
        model="palmyra-x-004", 
        messages=messages,
        temperature=temperature,
        tools=tools, 
        tool_choice="auto"
    )
    initial_response_message = initial_response.choices[0].message
    messages.append(initial_response_message)

    # Make secondary call to chat() function
    # if Palmyra decides that it needs to call a tool
    tool_calls = initial_response_message.tool_calls
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.function.name == "get_weather_at_location":
                location = eval(tool_call.function.arguments)["location"]
                function_response = get_weather_at_location(location)
            if tool_call.function.name == "get_location_from_ip":
                function_response = get_location_from_ip()
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": str(function_response),
            })

        final_response = client.chat.chat( 
            messages=messages,
            temperature=temperature,
            model="palmyra-x-004"
        )
        final_response_message = {
            "role": final_response.choices[0].message.role,
            "content": final_response.choices[0].message.content
        }
        messages.append(final_response_message)
        print(f"\n{final_response.choices[0].message.content}\n")
    else:
        print(f"\n{final_response.choices[0].message.content}\n")