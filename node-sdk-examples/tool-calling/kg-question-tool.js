const Writer = require("writer-sdk");
const dotenv = require('dotenv');

dotenv.config();

const client = new Writer({
  apiKey: process.env.WRITER_API_KEY,
});

tools = [
  {
      type: "graph",
      function: {
          description: "product descriptions",
          graph_ids: [
              "41eaf692-2bb6-46dc-a1e3-b09d4efe7b86"
          ],
          subqueries: true
      }
  }
];

async function main() {
  try {
    console.log("question: Which of our products contain either food coloring or chocolate?");
    const messages = [
      { role: "user", content: "Which of our products contain either food coloring or chocolate?" },
    ];
    console.log("-".repeat(100));

    console.log("Calling Writer with KG chat tool...");
    const response = await client.chat.chat({
      model: "palmyra-x-004",
      messages: messages,
      tools: tools,
      tool_choice: "auto",
      stream: false,
    });

    console.log(`Response: ${JSON.stringify(response)}`);
    console.log("-".repeat(100));

    const responseMessage = response.choices[0].message;
    console.log(
      `Final response:\n${responseMessage.content}\n`
    );
  } catch (error) {
    console.error("Error:", error);
  }
}

main();
