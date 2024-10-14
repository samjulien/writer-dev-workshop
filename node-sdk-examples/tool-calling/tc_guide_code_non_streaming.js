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
        stream: false,
    });

    const responseMessage = response.choices[0].message;
    const toolCalls = responseMessage.tool_calls;
    if (toolCalls && toolCalls.length > 0) {
        const toolCall = toolCalls[0];
        const toolCallId = toolCall.id;
        const functionName = toolCall.function.name;
        const functionArgs = JSON.parse(toolCall.function.arguments);

        if (functionName === "calculate_mean") {
            const functionResponse = calculateMean(functionArgs.numbers);

            messages.push({
                role: "tool",
                tool_call_id: toolCallId,
                name: functionName,
                content: functionResponse.toString(),
            });
        }
    }

    const finalResponse = await client.chat.chat({
        model: "palmyra-x-004",
        messages: messages,
        stream: false
    });
    
    console.log(`Final response: \n${finalResponse.choices[0].message.content}\n`);
    // Final response: "The mean is 5"
}

main();
