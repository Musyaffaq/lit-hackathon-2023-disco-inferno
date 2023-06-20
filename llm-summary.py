import os
from dotenv import load_dotenv
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain


def parse_result(text):

    result = {}

    result["summary"] = text.split("CONCISE SUMMARY:")[1].split("PARTIES INVOLVED:")[0]
    result["parties"] = text.split("PARTIES INVOLVED:")[1].split("KEY FACTS:")[0]
    result["facts"] = text.split("KEY FACTS:")[1].split("OUTCOME:")[0]
    result["outcome"] = text.split("OUTCOME:")[1].split("LIST OF CATEGORIES:")[0]
    result["categories"] = text.split("LIST OF CATEGORIES:")[1].replace(".", " ").split(", ")

    return result


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")
llm = OpenAI()

text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)

with open("sample_case.txt", encoding="utf8") as f:
    sample_case = f.read()
texts = text_splitter.split_text(sample_case)
docs = [Document(page_content=t) for t in texts[:3]]
categories = [
    'family',
    'housing',
    'money, debt and consumer issues',
    'work and employment law',
    'crime and prisons',
    'immigration',
    'estates, wills and guardianship',
    'health',
    'traffic and cars',
    'public benefits',
    'courts and lawyers',
    'accidents and torts',
    'education',
    'government services',
    'disaster relief',
    'small business and intellectual property',
    'civil and human rights'
]


prompt_template = """Here are some categories for legal texts.

{categories}


Write a concise summary of the following legal case, highlighting the parties involved, the key facts of the case and the outcome. THEN, provide a list of categories (separate by commas) that best describes the the case based on this list as well as any other categories you can generate that is suitable.

{text}


Give me the result in the following format:

CONCISE SUMMARY:
PARTIES INVOLVED:
KEY FACTS:
OUTCOME:
LIST OF CATEGORIES:
"""

PROMPT = PromptTemplate(template=prompt_template, input_variables=["categories", "text"])
PROMPT.format(categories=categories, text=docs)
chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
chain({"input_documents": docs, "categories": categories}, return_only_outputs=False)


result = chain.run(input_documents=docs, categories=categories)

print(result)

print("----------------------- DICTIONARY -----------------------")

print(parse_result(result))
