import os
from dotenv import load_dotenv
import writer as wf
import writer.ai
import re

# Welcome to Writer Framework! 
# This template is a starting point for your AI apps.
# More documentation is available at https://dev.writer.com/framework

# Load environment variables from .env file
load_dotenv()

# Set the API key
wf.api_key = os.getenv('WRITER_API_KEY')

# Initialise the state
wf.init_state({
    "my_app": {
        "title": "Social Posts Generator"
    },
    "posts": "",
    "topic": "writing",
    "message": "",
    "tags":{} # this was missing in the tutorial
})

def handle_button_click(state):
    state["message"] = "% Loading up expert social media posts..."
    
    prompt = f"You are a social media expert. Generate 5 engaging social media posts about {state['topic']}. Include emojis."
    state["posts"] = writer.ai.complete(prompt)

    prompt = f"You are a social media expert. Generate 5 hashtags about {state['topic']}, delimited by spaces. For example, #dogs #cats #ducks #elephants #badgers"
    pattern = r'#\w+'
    hashtags = re.findall(pattern, writer.ai.complete(prompt))
    state["tags"] = {item: item for item in hashtags}
    
    state["message"] = ""

def hello_world():
    print("hello world")