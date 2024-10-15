const Writer = require('writer-sdk');
const dotenv = require('dotenv');

dotenv.config();

const client = new Writer({
    apiKey: process.env.WRITER_API_KEY,
});

async function main() {
    try {
      const response = await client.applications.generateContent(
        process.env.APPLICATION_ID,
        {
        "inputs": [
          {
            "id": "Product description",
            "value": [
              "Terra running shoe"
            ]
          }
        ]
      },
      );
      console.log(response);
    } catch (error) {
      console.error('Error:', error);
    }
  }

main();