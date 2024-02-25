from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from prompts.system_prompt import generate_system_prompt

llm = Ollama(model="chat")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "{system_prompt}"),
        ("system", "{input}")
    ]
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

response = chain.invoke({"system_prompt": system_prompt, "input": "Introduce yourself to the user."})

# Trim special token from the response
if response.endswith("<|lm_end|>"):
    response = response[:-len("<|lm_end|>")]

# Print response
print(response)
