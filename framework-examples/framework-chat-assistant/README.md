# Framework quickstart: Chat assistant

In this guide, we'll create a simple yet powerful chat assistant using the Writer Framework. This project helps you build an AI-powered chatbot that can engage in conversations on various topics. If you're new to the Writer Framework, don't worry—we'll take it step by step!

![](images/chat_assistant_1.png)

## What you will learn

By following this guide, you will learn:

- How to set up a Writer Framework application.
- How to use Python to interact with the Writer API for creating a chat assistant.
- How to build a user interface using Writer Framework's drag-and-drop tools.
- How to deploy your application to the Writer cloud.

## Prerequisites

Before starting, ensure you have:

- **Python 3.7+**: Install from [python.org](https://www.python.org/downloads/).
- **pip**: Comes with Python, used for installing packages.
- **Basic Python Understanding**: Familiarity with Python will help, but we'll explain each step as we go.
- **Writer Account**: Create a free account at [writer.com](https://writer.com).

### Finished chat assistant app

Here's what the final app will look like, including a preview of the UI and chat interface.

![Finished chat assistant project](images/chat_assistant_1.png)

## Step 1: Get Writer Framework API key

First, grab your API Key to connect with the Writer Framework. This is different from the Writer SDK API Key—it's specific to the Writer Framework.

If you already have an API Key, you can skip this section.

### Steps to get your API key

1. **Create a New App**: On the Writer home screen, click **"Build an app"**.
2. **Select Framework**: Choose **"Framework"** as the app type.
3. **Get Your API Key**: Under **"Authenticate with an API key"**, click **"Reveal"** to copy your API key.

![](images/chat_assistant_2.png)

![](images/chat_assistant_3.png)

(Optional) You can rename your app by clicking on the app name at the top left, making it easier to find and remember.

## Step 2: Set up the environment

Next, we'll set up our Writer Framework environment locally by creating a directory for the project, installing dependencies, and creating the application using a template.

### Steps to set up the environment

1. **Create the Project Directory**: Run the following in your terminal:

```
mkdir chat-assistant-app
cd chat-assistant-app
```

2. **Install dependencies**: Install `writer` and `python-dotenv`:

```
pip install writer python-dotenv
```

   We use `python-dotenv` to manage environment variables easily by loading them from a `.env` file.

3. **Create a .env File**: Create a `.env` file in your project directory and add your API key:

```
WRITER_API_KEY=[your_api_key]
```

4. **Create the application**: Use the Writer Framework template to create the application:

```
writer create chat-assistant --template=ai-starter
```

   This command sets up a new project called "chat-assistant" using a starter template.

## Step 3: Build the user interface (UI)

With the app set up, let's create the UI. The Writer Framework's drag-and-drop capabilities make it easy—even if you haven't done much UI work before!

Open the Project Editor by typing:

```
writer edit chat-assistant
```

This will open the Writer editor on port 3006. Access it in your browser at localhost:3006.

You'll see a canvas in the center, a component library on the left, and a properties panel on the right. Let's build our UI step by step:

1. **Header:**
   - The Header component should already be present. We'll update its title in the code later.

2. **Section:**
   - Click on the existing Section component.
   - In the Component Settings, clear out the default title.

3. **Text:**
   - Drag a Text component into the Section.
   - In the Component Settings, set the content to provide instructions or context for your chat assistant. For example: "Welcome to the Chat Assistant. Ask me anything!"

4. **Chatbot:**
   - Drag a Chatbot component into the Section beneath the Text box.

Your UI should now look similar to this:

![Initial UI with text and chatbot](images/chat_assistant_4.png)

## Step 4: Add backend logic

Now, let's add the logic to power our chat assistant by modifying `main.py`.

### Setting up imports and loading API key

In `main.py`, add:

```python
import os
from dotenv import load_dotenv
import writer as wf
import writer.ai

# Load environment variables from .env file
load_dotenv()

# Set the API key
wf.api_key = os.getenv('WRITER_API_KEY')
```

### Initialize application state

Set the app title and initial state:

```python
wf.init_state({
    "conversation": writer.ai.Conversation(),
    "my_app": {
        "title": "CHAT ASSISTANT"
    },
})
```

### Handling chat messages

Add a function to handle incoming chat messages:

```python
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
```

### Final code in `main.py`

Here's what the final code should look like in `main.py`:

```python
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
        "title": "CHAT ASSISTANT"
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
```

## Step 5: Bind the UI

Now, let's connect the UI components we created to the application logic.

- **Chatbot Component:** Bind to `conversation`
  - **How**: Set "Conversation Object" to `@{conversation}` in the **Component Settings** of the Chatbot.
  - You can also update properties such as the assistant's initials, the user's initials, and whether the chat uses markdown.
![](images/chat_assistant_5.png)

- **Chatbot Event Handler:** Bind to `handle_simple_message`
  - **How**: In the **Events** section of the Component Settings, set `wf-chatbot-message` to `handle_simple_message`.

    ![](images/chat_assistant_6.png)

## Step 6: Run the application

To run the app locally, use the following command:

```
writer run chat-assistant
```

This will start your application on port 3005. You can access it in your browser at localhost:3005 to test the functionality.

![](images/chat_assistant_7.png)

## Step 7: Deploy the application (optional)

To deploy the app, either terminate your current Writer process or use a new terminal:

```
writer deploy chat-assistant
```

The command will provide the URL of your live application.

## Conclusion

And that's it—you've built a functional chat assistant using the Writer Framework! You can now extend this project to add more features or explore other capabilities of the platform. For more, check out the Writer Framework and API documentation.