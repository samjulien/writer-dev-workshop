# Writer Developer Workshop Resources
A collection of resources for developers to learn about Writer.

## Get Started with Writer

Welcome to Writer\! Writer is the full-stack generative AI platform for enterprises. You can quickly and easily build and deploy AI apps using our suite of developer tools, which fully integrate with our LLMs, graph-based Retrieval Augmented Generation (RAG), AI guardrails, and more.

## What you can do with Writer

With Writer, you can:

- Build AI digital assistants for various content needs  
- Perform text generation and summarization  
- Conduct data analysis and enhance writing quality

## Three ways to build with Writer

You have three options for building AI tools with Writer, designed for different skill levels and needs:

1. **No-code builder** - A visual, point-and-click tool where you add components like text boxes, file uploads, and more for creating AI writing applications without any coding.  
2. **Writer framework** - An open-source tool for building advanced web-based apps using a combination of visual components and Python code.  
3. **Writer RESTful APIs and SDKs** - Full flexibility to integrate Writer's AI into any application, with support for custom knowledge graphs and function calling.

Each option offers different levels of coding and customization, so you can choose what fits your project best.

| Feature | No-code builder | Writer framework | Writer API/SDK |
| :---- | :---- | :---- | :---- |
| Coding required | None \- Get started fast with zero coding | Intermediate to Advanced \- Customize with Python (flexible for advanced users) | Advanced \- Full flexibility, integrate in any codebase |
| Customization scope | Easy, and flexible customization – Chain prompts, set outputs, and adjust variables with ease. | Extensive \- Custom components, HTML, iFrame, pages. | Unlimited \- Full API access, complete customization for any app |
| Best for | Text generation and chat apps | Web-based custom apps, ideal for Python developers | Embedding AI into existing tech stacks or new languages |

- **Choose No-code builder if:** You want to create AI writing tools without coding.  
- **Choose Writer framework if:** You're a Python developer wanting to build custom web-based AI apps.  
- **Choose Writer API/SDK if:** You need to integrate Writer's AI into existing applications or workflows, or build new applications in the language of your choice.

💡 **Note:** Whatever option you choose, you get access to Writer's Palmyra AI models, offering a range of capabilities for content generation, editing, and automation. See [https://dev.writer.com/home/models](https://dev.writer.com/home/models#models)

Let’s take a closer look at each option, along with what you can accomplish using them.

---

## **Overview of building options**

### Option 1: No-code builder

**Best for:** Business users who want to build AI tools without any coding.

**With the No-code builder, you can:**

- Build AI applications using a visual editor  
- Build content generation or editing applications  
- Create internal tools for content teams  
- Create chat assistants that can also connect to a Knowledge Graph of your data  
- Integrate any of the Palmyra LLMs

**Quick start guides**

- [Build a text generation app](https://dev.writer.com/no-code/building-a-text-generation-app)  
- [Build a chat app](https://dev.writer.com/no-code/building-a-chat-app)

---

### Option 2: Writer framework

**Best for:** Python developers building custom web-based AI apps.

**API Key Required:** You will need an API key if you want to use Writer's LLMs and other advanced capabilities in the Writer framework. [Follow the instructions here to sign up for AI Studio and get your Framework API key](https://dev.writer.com/api-guides/quickstart#generate-a-new-api-key).

**With Writer framework, you can:**

- Build AI applications using a drag-and-drop visual editor for the frontend, and write backend code in Python  
- Use external data, like APIs, to bring in information from other sources  
- Handle complex user input and custom logic  
- Quickly analyze and visualize data using an LLM  
- Easily integrate Writer platform capabilities like Knowledge Graphs and tool calling using the AI module

**Things to know:**

- Install with `pip install writer` (a standard Python package)  
- UI is saved as JSON file, so you can version it with the rest of the application.  
- Two ways to edit the UI: Using your local code editor for instant refreshes or the provided web-based editor  
- See live updates while editing—no need to hit 'Preview'

**Quick start guides**

- Framework quickstart: [https://dev.writer.com/framework/quickstart](https://dev.writer.com/framework/quickstart)  
- Build a social post generator: [https://dev.writer.com/framework/social-post-generator](https://dev.writer.com/framework/social-post-generator)  
- Build a chat assistant: [https://dev.writer.com/framework/chat-assistant](https://dev.writer.com/framework/chat-assistant)  
- Sample app library: [https://github.com/writer/framework-tutorials](https://github.com/writer/framework-tutorials)  
- More sample apps: [https://github.com/writer/writer-framework/tree/dev/apps](https://github.com/writer/writer-framework/tree/dev/apps)

---

### Option 3: Writer APIs/SDKs

**Best for:** Developers integrating Writer's AI capabilities into new or existing applications, regardless of the programming language.

**API Key Required:** You will need an API key to use Writer APIs/SDKs. [Follow the instructions here to get your API key](https://dev.writer.com/api-guides/quickstart#generate-a-new-api-key).

**With the Writer APIs, you can:**

- Use chat and completion APIs to build custom apps, or build custom integrations with your existing tech stack.  
- **Build custom knowledge graphs:** Create knowledge bases using your own files and documents, allowing you to build intelligent Q\&A systems, content recommendation engines, and document retrieval systems that understand context.  
- **Tool calling (aka function calling):** Extend the AI’s functionality by enabling it to call your custom functions. The AI can use these functions to fetch real-time data or perform calculations when generating responses.  
- Use the RESTful API with any language you prefer, or use our SDKs for Python and Node.

**SDKs**

- Python SDK: [https://pypi.org/project/writer-sdk](https://pypi.org/project/writer-sdk/) (`pip install writer-sdk`)  
- Node SDK: [https://www.npmjs.com/package/writer-sdk](https://www.npmjs.com/package/writer-sdk) (`npm install writer-sdk`)

**SDKs Quick Start**

- [Getting started with Writer SDKs](https://dev.writer.com/api-guides/sdks)

**Python/Node Quick Start**

- Text generation: [https://dev.writer.com/api-guides/text-generation](https://dev.writer.com/api-guides/text-generation)  
- Chat completion: [https://dev.writer.com/api-guides/chat-completion](https://dev.writer.com/api-guides/chat-completionhttps://dev.writer.com/api-guides/chat-completion)  
- Knowledge graph: [https://dev.writer.com/api-guides/knowledge-graph](https://dev.writer.com/api-guides/knowledge-graph)  
- Applications API: [https://dev.writer.com/api-guides/applications](https://dev.writer.com/api-guides/applications)  
- Tool calling: [https://dev.writer.com/api-guides/tool-calling](https://dev.writer.com/api-guides/tool-calling)  
- Knowledge graph chat: [https://dev.writer.com/api-guides/kg-chat](https://dev.writer.com/api-guides/kg-chat)

**Cookbooks**

We also have several Python cookbooks available to help you get started with common tasks. Check it out here: [https://github.com/writer/cookbooks](https://github.com/writer/cookbooks/tree/main/tool_calling)

---

## Choosing the right path

While all three paths allow you to create powerful AI writing tools, you can determine which path is right for you by thinking about what you want to achieve and your technical background:

- **No-code builder:** Best for business and non-technical users looking to create AI tools quickly.  
- **Writer framework:** Ideal for Python developers who want to create custom web apps.  
- **Writer API/SDK:** Great for integrating AI features into existing apps or building large-scale systems.

---

## Start building today

Select the path that fits your skills and project needs, and get started with our [documentation](https://dev.writer.com/).

We can’t wait to see what you build with Writer—tools that improve communication, simplify content creation, and help people write better.

We’re excited to see how you’ll use Writer’s enterprise-grade tools to create impactful AI apps that elevate content creation, enhance communication, and drive better writing.  
