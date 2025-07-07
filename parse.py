from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3")


def parse_with_ollama(dom_chunks, parse_description):
    #prompt have both dom_content and parse_content 
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    # The result, chain, is an object that knows how to:
    # Fill in your template with actual values.
    # Send the filled prompt to the LLM.
    # Return the LLM’s response. Every time you do chain.invoke(inputs), it merges inputs into the template and runs the LLM for you.
    parsed_results = []



    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)