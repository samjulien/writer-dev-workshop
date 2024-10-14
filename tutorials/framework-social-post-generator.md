# Framework quickstart: social post generator

In this guide, we'll create a simple yet powerful social media post generator using the Writer Framework. This project helps you generate social media posts and tags automatically based on your input. If you're new to the Writer Framework, don’t worry—we'll take it step by step\!

## What you will learn

By following this guide, you will learn:

- How to set up a Writer Framework application.  
- How to use Python to interact with the Writer API for generating social media content.  
- How to build a user interface using Writer Framework’s drag-and-drop tools.  
- How to deploy your application to the Writer cloud.

## Prerequisites

Before starting, ensure you have:

- **Python 3.7+**: Install from [python.org](https://www.python.org/downloads/).  
- **pip**: Comes with Python, used for installing packages.  
- **Basic Python Understanding**: Familiarity with Python will help, but we’ll explain each step as we go.  
- **Writer Account**: Create a free account at [writer.com](https://writer.com).

### Finished social post generator app

Here's what the final app will look like, including a preview of the UI and generated posts.

\[Insert image of finished application here\]

   
For your convenience, you can find the complete code \[here\]. If you prefer, you can also use the provided ui.json to quickly build the UI. 

## Step 1: get Writer Framework API key

First, grab your API Key to connect with the Writer Framework. This is different from the Writer SDK API Key—it’s specific to the Writer Framework.

If you already have an API Key, you can skip this section.

### Steps to get your API key

1. **Create a New App**: On the Writer home screen, click **"Build an app"**.  
2. **Select Framework**: Choose **"Framework"** as the app type.  
3. **Get Your API Key**: Under **"Authenticate with an API key"**, click **"Reveal"** to copy your API key.

(Optional) You can rename your app by clicking on the app name at the top left, making it easier to find, and remember.

## Step 2: set up the environment

Next, we’ll set up our Writer Framework environment locally by creating a directory for the project, installing dependencies, and creating the application using a template.

### Steps to set up the environment

1. **Create the Project Directory**: Run the following in your terminal:

```
mkdir social-generator-app
cd social-generator-app
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
writer create social-generator --template=ai-starter
```

   This command sets up a new project called "social-generator" using a starter template.

## Step 3: build the user interface (UI)

With the app set up, let’s create the UI. The Writer Framework's drag-and-drop capabilities make it easy—even if you haven’t done much UI work before\!

**Open the Project Editor by typing**

```
writer edit social-generator
```

This will open the Writer editor on port 3006\. Access it in your browser at localhost:3006. 

You can drag and drop components from the left sidebar onto the canvas, and then alter their settings in the right sidebar. Let's explore building out our frontend using this visual builder.\\

Certainly\! I'll focus solely on improving the UI building instructions from the given starting point. Here's an enhanced version of the "Step 3: Build the user interface (UI)" section:

## Step 3: Build the user interface (UI)

With the app set up, let's create the UI. The Writer Framework's drag-and-drop capabilities make it easy—even if you haven't done much UI work before\!

Open the Project Editor by typing:

```
writer edit social-generator
```

This will open the Writer editor on port 3006\. Access it in your browser at localhost:3006.

You'll see a canvas in the center, a component library on the left, and a properties panel on the right. Let's build our UI step by step:

### Designing the input UI

1. **Text Input:**  
     
   - From the left sidebar, drag a Text Input component onto the top of the canvas.  
   - In the right sidebar under "Component Settings":  
     - Set "Label" to "Topic for social posts".  
     - (Optional) Adjust the "Placeholder" text if desired.

   

2. **Button:**  
     
   - Drag a Button component from the left sidebar and place it directly below the Text Input.  
   - In the Component Settings:  
     - Set "Text" to "Generate posts".  
     - Under "Icon", select "arrow\_forward" from the dropdown.  
     - (Optional) Adjust "Variant" or "Size" as needed.

   

3. **Message:**  
     
   - Drag a `Message` component from the left sidebar and position it below the Button.  
   - In the Component Settings:  
     - Set "Loading Color" to RGB(212,255,242).  
     - (Optional) Adjust "Type" or other settings as desired.

### Designing the output UI

1. **Section:**  
     
   - Drag a Section component from the left sidebar and place it below the Messages component.  
   - In the Component Settings:  
     - Delete the text in "Title" to remove the default title.  
     - Set "Container Background Color" to RGB(246,239,253).  
     - (Optional) Adjust padding or other layout settings as needed.

   

2. **Separator:**  
     
   - Drag a Separator component from the left sidebar and position it at the top inside the new Section.  
   - (Optional) Adjust the separator style in Component Settings if desired.

   

3. **Tags:**  
     
   - Drag a Tags component from the left sidebar and place it below the Separator within the Section.  
   - (Optional) In Component Settings, you can adjust the tag style, size, or other properties.

   

4. **Text:**  
     
   - Finally, drag a Text component from the left sidebar and position it below the Tags component.  
   - This will display the generated posts, so you may want to:  
     - Increase the "Font Size" in Component Settings.  
     - Enable "Allow Markdown" if you want to support formatted text.

## Step 4: Add backend logic

Now, let’s add the logic to generate posts by modifying `main.py`.

### Setting up imports and loading API key

In `main.py`, add:

```py
import writer as wf  # already included in template
import writer.ai  # already included in template

# Add these
from dotenv import load_dotenv
import os
import re  # for working with hashtags

load_dotenv()
writer_api_key = os.getenv("WRITER_API_KEY")
```

### Initialize application state

Set the app title and initial state:

```py
wf.init_state({
    "my_app": {
        "title": "Social Posts Generator"
    },
    "posts": "",
    "topic": "writing",
    "message": "",
    "tags": {}
})
```

### Handling button clicks

Add a function to handle button clicks:

```py
def handle_button_click(state):
    state["message"] = "% Loading up expert social media posts..."

    # Generate social posts
    prompt = f"You are a social media expert. Generate 5 engaging social media posts about {state['topic']}. Include emojis."
    state["posts"] = writer.ai.complete(prompt)

    # Generate hashtags
    prompt = f"You are a social media expert. Generate 5 hashtags about {state['topic']}, delimited by spaces. For example, #dogs #cats #ducks #elephants #badgers"
    pattern = r'#\w+'
    hashtags = re.findall(pattern, writer.ai.complete(prompt))
    state["tags"] = {item: item for item in hashtags}

    state["message"] = ""
```

### Final code in `main.py`

Here’s what the final code should look like in `main.py`:

```py
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

# Initialize the state
wf.init_state({
    "my_app": {
        "title": "Social Posts Generator"
    },
    "posts": "",
    "topic": "writing",
    "message": "",
    "tags": {} 
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
```

## Step 5: bind the UI

Now, let's connect the UI components we created to the application logic. This step is where we make the front-end components interact with the backend logic, ensuring that user inputs trigger the appropriate functions and display results. We'll link the UI elements to specific pieces of application state and event handlers.

- **Text Input Component:** Bind to `Topic`   
  - **How**: Set "State\_element" to `@topic` in the **Component Settings** of the Text Input.  
- **Button Component:** Bind to`handle_button_click`   
  - **How**: Set `wf-click` to `handle_button_click` in the **Component Settings** of the Button.  
- **Message Component:** Bind to `message`    
  - **How**: Set "Text" to `@{message}`. Set "Visible" to `@{message}`.  
- **Tags Component:** Bind to `tags`    
  - **How**: Set "JSON" to `@{tags}`.  
- **Text Component for Posts:**   Bind to `posts`    
  - **How**: Set "Text" to `@{posts}`. Enable "Markdown" option.  
- **Section for Tags and Posts: Set Visibility**  
  - Ensure the section containing tags and posts is only visible when posts are available.  
  - **How**: Set "Visible" to `@{posts}`.

## Step 6: Run the application

To run the app locally, ensure you have the Writer editor open and use your browser to access `localhost:3006` to test the functionality.

## Step 7: Deploy the application (optional)

To deploy the app, either terminate your current Writer process or use a new terminal:

```
writer deploy social-generator
```

The command will provide the URL of your live application.

## Conclusion

And that's it—you've built a functional social post generator using the Writer Framework\! You can now extend this project to add more features or explore other capabilities of the platform. For more, check out the Writer Framework and API documentation.  
