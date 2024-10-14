const Writer = require('writer-sdk');
const dotenv = require('dotenv');

dotenv.config();

const client = new Writer({
    apiKey: process.env.WRITER_API_KEY,
});

async function main() {
    try {
      const response = await client.applications.generateContent(
        "55e691b8-e471-4e85-89d0-b7f320a2d50f",
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