const Writer = require("writer-sdk");
const dotenv = require('dotenv');

dotenv.config();

const client = new Writer({
  apiKey: process.env.WRITER_API_KEY,
});

const getMovieInfo = async (title) => {
  const omdbApiKey = "7e7d8f43";
  const url = `http://www.omdbapi.com/?apikey=${omdbApiKey}&t=${encodeURIComponent(
    title
  )}`;
  try {
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      return JSON.stringify(data);
    } else {
      return `Failed to retrieve movie info. Status code: ${response.status}`;
    }
  } catch (error) {
    return `Error: ${error.message}`;
  }
};

const tools = [
  {
    type: "function",
    function: {
      name: "getMovieInfo",
      description: "Get information about a movie by its title",
      parameters: {
        type: "object",
        properties: {
          title: {
            type: "string",
            description: "The title of the movie to retrieve information for",
          },
        },
        required: ["title"],
      },
    },
  },
];

async function main() {
  try {
    console.log("question: what is the revenue for interstellar?");
    const messages = [
      { role: "user", content: "what is the revenue for interstellar?" },
    ];
    console.log("-".repeat(100));

    const response = await client.chat.chat({
      model: "palmyra-x-004",
      messages: messages,
      tools: tools,
      tool_choice: "auto",
      stream: false,
    });

    const responseMessage = response.choices[0].message;
    messages.push(responseMessage);

    console.log(`Tool calls response: ${JSON.stringify(responseMessage)}\n`);
    console.log("-".repeat(100));

    const toolCalls = responseMessage.tool_calls;
    if (toolCalls) {
      const toolCall = toolCalls[0];
      const toolCallId = toolCall.id;
      const functionName = toolCall.function.name;
      const functionArgs = JSON.parse(toolCall.function.arguments);

      if (functionName === "getMovieInfo") {
        const functionResponse = await getMovieInfo(functionArgs.title);
        console.log(`Response from API:\n${functionResponse}`);
        console.log("-".repeat(100));

        messages.push({
          role: "tool",
          tool_call_id: toolCallId,
          name: functionName,
          content: functionResponse,
        });

        const finalResponse = await client.chat.chat({
          model: "palmyra-x-004",
          messages: messages,
          stream: false,
        });
        console.log(
          `Final response:\n${finalResponse.choices[0].message.content}\n`
        );
      } else {
        console.log(`Error: function ${functionName} not found`);
      }
    }
  } catch (error) {
    console.error("Error:", error);
  }
}

main();
