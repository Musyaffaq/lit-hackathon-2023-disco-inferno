import os
from dotenv import load_dotenv
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")
llm = OpenAI()

text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)

with open("sample_case.txt", encoding="utf8") as f:
    sample_case = f.read()
texts = text_splitter.split_text(sample_case)
docs = [Document(page_content=t) for t in texts[:3]]


prompt_template = """Write a concise summary of the following legal case, which includes all the areas of law that the case covers. THEN, provide a list of categories that best describes the the case.


{text}



CONCISE SUMMARY:
LIST OF CATEGORIES:
"""


PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
chain({"input_documents": docs}, return_only_outputs=False)


result = chain.run(input_documents=docs)

print(result)
