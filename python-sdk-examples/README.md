# Writer Python SDK Examples

This folder contains simple examples of how to use the [Writer Python SDK](https://www.github.com/writer/writer-python) to build applications.

## Prerequisites

Before starting, ensure you have:

- A Writer AI Studio account ([sign up for free here](https://app.writer.com/aistudio/signup?utm_campaign=devrel))
- The Writer Python SDK installed (follow [these instructions](https://dev.writer.com/api-guides/sdks))

## Examples

Each folder contains simple examples demonstrating a specific feature of the Writer Python SDK.

- [completion](./completion) - These examples show how to use the Writer Python SDK to access the Writer completion API. This includes features like text generation, chat, and generating output from no-code applications.
- [knowledge-graph](./knowledge-graph) - These examples show how to use the Writer Python SDK to access the Writer file and Knowledge Graph APIs.
- [tool-calling](./tool-calling) - These examples show how to use the Writer Python SDK for tool calling, using both custom functions and built-in tools like Knowledge Graph chat.

## Running the examples

To run the examples:

1. Clone the repository and navigate to the example folder.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file with your Writer API key. The tool calling example also uses the free [OMDb API](https://www.omdbapi.com/), so you'll need to create an API key and set it as an environment variable called `OMDB_API_KEY`. You can also feel free use a different API for that example.
4. Run the individual example, for example:

```bash
python completion/text.py
```

## More information

For more information on the Writer API, check out the [full API reference documentation](https://dev.writer.com/api-guides/api-reference).

If you run into any issues, please feel free to [open an issue](https://github.com/samjulien/writer-dev-workshop/issues).
