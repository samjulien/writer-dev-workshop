const Writer = require('writer-sdk');
const dotenv = require('dotenv');

dotenv.config();

const client = new Writer({
    apiKey: process.env.WRITER_API_KEY,
});

async function main() {
    try {
      const completion = await client.completions.create({
        model: 'palmyra-x-003-instruct',
        prompt: 'Tell me a story about a magical forest and a hero who must save the forest from a dark wizard.',
        temperature: 0.7,
        stream: true
      });

      let content = '';
      for await (const chunk of completion) {
        content += chunk.value;
      }
      console.log(content);
    } catch (error) {
      console.error('Error:', error);
    }
  }

main();