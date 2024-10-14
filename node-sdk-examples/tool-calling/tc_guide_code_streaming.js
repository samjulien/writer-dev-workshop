const dotenv = require("dotenv");
const Writer = require("writer-sdk");

dotenv.config();

const client = new Writer();

function calculateMean(numbers) {
    if (numbers.length === 0) {
        throw new Error("Cannot calculate mean of an empty array");
    }
    return numbers.reduce((sum, num) => sum + num, 0) / numbers.length;
}

const tools = [
    {
        type: "function",
        function: {
            name: "calculate_mean",
            description: "Calculate the mean (average) of a list of numbers.",
            parameters: {
            type: "object",
            properties: {
                numbers: {
                    type: "array",
                    items: { type: "number" },
                    description: "List of numbers",
                },
            },
            required: ["numbers"],
            },
        },
    },
];

async function main() {
    let messages = [
        { role: "user", content: "what is the mean of [1,3,5,7,9]?" },
    ];

    const response = await client.chat.chat({
        model: "palmyra-x-004",
        messages: messages,
        tools: tools,
        tool_choice: "auto",
        stream: true,
    });

    let streamingContent = "";
    const functionCalls = [];

    for await (const chunk of response) {
        const choice = chunk.choices[0];

        if (choice.delta) {
            if (choice.delta.tool_calls) {
                for (const toolCall of choice.delta.tool_calls) {
                    if (toolCall.id) {
                        functionCalls.push({
                            name: "",
                            arguments: "",
                            call_id: toolCall.id,
                        });
                    }
                    if (toolCall.function) {
                        functionCalls[functionCalls.length - 1].name +=
                            toolCall.function.name || "";
                        functionCalls[functionCalls.length - 1].arguments +=
                            toolCall.function.arguments || "";
                    }
                }
            } else if (choice.delta.content) {
                streamingContent += choice.delta.content;
            }

            // A finish reason of stop means the model has finished generating the response
            if (choice.finish_reason === "stop") {
                messages.push({ role: "assistant", content: streamingContent });
            } else if (choice.finish_reason === "tool_calls") {
                console.log(functionCalls);
                // A finish reason of tool_calls means the model has finished deciding which tools to call
                for (const functionCall of functionCalls) {
                    if (functionCall.name === "calculate_mean") {
                        const argumentsDict = JSON.parse(
                            functionCall.arguments
                        );
                        const functionResponse = calculateMean(
                            argumentsDict.numbers
                        );

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
                    stream: true,
                });

                let finalStreamingContent = "";
                for await (const chunk of finalResponse) {
                    const choice = chunk.choices[0];
                    if (choice.delta && choice.delta.content) {
                        finalStreamingContent += choice.delta.content;
                    }
                }

                console.log(finalStreamingContent);
                // The mean is 5
            }
        }
    }
}

main();
