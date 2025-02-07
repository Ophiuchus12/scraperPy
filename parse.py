from models import models
from g4f import AsyncClient

client = AsyncClient()

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

print ("models", models)

async def parse_with_ai(dom_chunks, parse_description):
    parse_results = []
    for model in models : 
        try: 
            for i, chunk in enumerate(dom_chunks):
                response = await client.chat.completions.create(
                    model = model,
                    messages = [
                        {"role": "user", "content": template.format(dom_content= chunk, parse_description=parse_description)}
                    ], 
                    web_search = False
                )
                if response :
                    parse_results.append(response.choices[0].message.content)
                    print(f"Parsed batch: {i+1} of {len(dom_chunks)} with model {model}")
                
            return "\n".join(parse_results)
        except Exception as e:
            print(f"Error parsing with model {model}: {e}")
            continue
    return "No model was able to parse the content"

