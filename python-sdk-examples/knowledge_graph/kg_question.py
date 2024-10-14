import os
import dotenv
from writerai import Writer

dotenv.load_dotenv()

client = Writer()

response = client.graphs.question(
    graph_ids=[os.getenv("GRAPH_ID")],
    question="Which products contain food coloring?",
    stream=True,
    subqueries=True,
)
answer = ""
for chunk in response:
    answer += chunk
    
print(answer)
