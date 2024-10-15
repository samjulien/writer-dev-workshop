const Writer = require('writer-sdk');
const dotenv = require('dotenv');

dotenv.config();

const client = new Writer({
    apiKey: process.env.WRITER_API_KEY,
});

async function main() {
    try {
      const response = await client.graphs.question({
        graph_ids: [process.env.GRAPH_ID],
        question: 'Which of our products contain food coloring?',
        stream: false,
        subqueries: true,
      });
      console.log(response.answer);
    } catch (error) {
      console.error('Error:', error);
    }
  }

main();