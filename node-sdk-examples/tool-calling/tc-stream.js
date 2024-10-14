const dotenv = require('dotenv');
const Writer = require('writer-sdk');
const fetch = require('node-fetch');
const math = require('mathjs');

dotenv.config();

const client = new Writer();

async function getMovieInfo(title) {
    const omdbApiKey = process.env.OMDB_API_KEY;
    const url = `http://www.omdbapi.com/?apikey=${omdbApiKey}&t=${title}`;
    const response = await fetch(url);
    if (response.ok) {
        return JSON.stringify(await response.json());
    } else {
        return `Failed to retrieve movie info. Status code: ${response.status}`;
    }
}

function calculateFactorial(number) {
    return math.factorial(number);
}

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
                    }
                },
                required: ["title"],
            },
        },
    },
    {
        type: "function",
        function: {
            name: "calculateFactorial",
            description: "Calculate the factorial of a number",
            parameters: {
                type: "object",
                properties: {
                    number: { type: "integer", description: "The number to calculate the factorial of" }
                },
                required: ["number"]
            }
        }
    }
];

console.log("question: what is the revenue for interstellar and what is the factorial of 5?");
const messages = [{ role: "user", content: "What's the revenue for interstellar and what is the factorial of 5?" }];
// console.log("question: what is the fastest way to get to the moon?");
// const messages = [{ role: "user", content: "What's the fastest way to get to the moon?" }];
console.log("-".repeat(100));

async function main() {
    const response = await client.chat.chat({
        model: "palmyra-x-004",
        messages: messages,
        tools: tools,
        tool_choice: "auto",
        stream: true
    });

    let streamingContent = "";
    const functionCalls = [];

    for await (const chunk of response) {
        const choice = chunk.choices[0];

        if (choice.delta) {
            if (choice.delta.tool_calls) {
                for (const toolCall of choice.delta.tool_calls) {
                    if (toolCall.id) {
                        functionCalls.push({ name: "", arguments: "", call_id: toolCall.id });
                    }
                    if (toolCall.function) {
                        functionCalls[functionCalls.length - 1].name += toolCall.function.name || "";
                        functionCalls[functionCalls.length - 1].arguments += toolCall.function.arguments || "";
                    }
                }
            } else if (choice.delta.content) {
                streamingContent += choice.delta.content;
                process.stdout.write(choice.delta.content);
            }

            if (choice.finish_reason === "stop") {
                messages.push({ role: "assistant", content: streamingContent });
            } else if (choice.finish_reason === "tool_calls") {
                console.log(`collated function_calls: ${JSON.stringify(functionCalls)}`);
                for (const functionCall of functionCalls) {
                    if (functionCall.name === "getMovieInfo") {
                        const argumentsDict = JSON.parse(functionCall.arguments);
                        const functionResponse = await getMovieInfo(argumentsDict.title);
                        console.log(`Response from API:\n${functionResponse}`);
                        console.log("-".repeat(100));
                        messages.push({
                            role: "tool",
                            content: functionResponse,
                            tool_call_id: functionCall.call_id,
                            name: functionCall.name,
                        });
                    } else if (functionCall.name === "calculateFactorial") {
                        const argumentsDict = JSON.parse(functionCall.arguments);
                        const functionResponse = calculateFactorial(argumentsDict.number);
                        console.log(`Response from factorial:\n${functionResponse}`);
                        console.log("-".repeat(100));
                        messages.push({
                            role: "tool",
                            content: functionResponse.toString(),
                            tool_call_id: functionCall.call_id,
                            name: functionCall.name,
                        });
                    }
                }

                const finalResponse = await client.chat.chat({
                    model: "palmyra-x-004",
                    messages: messages,
                    stream: true
                });

                let finalStreamingContent = "";
                for await (const chunk of finalResponse) {
                    const choice = chunk.choices[0];
                    if (choice.delta && choice.delta.content) {
                        finalStreamingContent += choice.delta.content;
                        process.stdout.write(choice.delta.content);
                    }
                }
                // console.log(finalStreamingContent);
            }
        }
    }
}

main().catch(console.error);