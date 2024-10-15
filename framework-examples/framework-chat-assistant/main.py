import os
from dotenv import load_dotenv
import writer as wf
import writer.ai

# Welcome to Writer Framework! 
# This template is a starting point for your AI apps.
# More documentation is available at https://dev.writer.com/framework

# Load environment variables from .env file
load_dotenv()

# Set the API key
wf.api_key = os.getenv('WRITER_API_KEY')

# Initialise the state
wf.init_state({
    "conversation": writer.ai.Conversation(),
    "my_app": {
        "title": "Chat Assistant"
    },
})

def handle_simple_message(state, payload):
  print("Payload received:", payload)
  state["conversation"] += payload

  try: 
    for chunk in state["conversation"].stream_complete():
        print(chunk)
        if not chunk.get("content"):
           chunk["content"] = ""
        state["conversation"] += chunk
  except Exception as e:
    print("Error during stream_complete:", e)