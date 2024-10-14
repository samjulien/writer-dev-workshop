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
        temperature: 0.7
      });

      console.log(completion.choices[0].text);
    } catch (error) {
      console.error('Error:', error);
    }
  }

main();