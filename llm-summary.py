import os
from dotenv import load_dotenv
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from tkinter import filedialog
import pandas as pd
import ntpath
import helper_functions as hf

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")
llm = OpenAI()


def main():
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=50)
    in_path = os.path.expanduser("~\\Desktop")
    skip = "N"
    file_path =  filedialog.askopenfilename(initialdir = r"%s" %in_path,title = "Select case to summarise and store", filetypes = (("PDF","*.pdf"),("all files","*.*")))
    case_name = ntpath.basename(file_path).replace(".pdf","")
    file_content = hf.read_pdf(file_path)
    texts = text_splitter.split_text(file_content)
    docs = [Document(page_content=t) for t in texts[:3]]


    prompt_template = """Write a concise summary of the following legal case, which includes all the areas of law that the case covers. 
    THEN, provide a list of the judges present.
    THEN, provide the court or tribunal the case was heard in.
    THEN, provide a list of categories that best describes the the case.
    THEN, provide the outcome of the judgement alongside a list of damages/sentencing (e.g. amount fined, jail term, damages, etc.).
    

    FOLLOW THE EXAMPLE PROVIDED BELOW!


    {text}


    EXAMPLE (the double quotes and commas should be included in the output):
    "case_summary": "SUMMARY OF CASE HERE",
    "corem": "LIST OF JUDGES HERE",
    "court": "COURT OR TRIBUNAL HERE",
    "categories": "LIST OF CATEGORIES HERE"
    "outcome": "OUTCOME OF JUDGEMENT AND DAMAGES/SENTENCING HERE"

    """


    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
    chain({"input_documents": docs}, return_only_outputs=False)


    result = chain.run(input_documents=docs)

    return result, case_name


raw_output, case_name = main()
output = f"""{{
"case_name": "{case_name}",{raw_output}
}}
"""
hf.append_to_db(output)
