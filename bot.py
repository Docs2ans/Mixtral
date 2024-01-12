from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
import torch
import base64
import textwrap
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from io import StringIO
import json
from constants import CHROMA_SETTINGS

checkpoint = "mistralai/Mixtral-8x7B-v0.1"
# tokenizer = AutoTokenizer.from_pretrained("MBZUAI/LaMini-T5-738M")
# base_model = AutoModelForSeq2SeqLM.from_pretrained(
#     "MBZUAI/LaMini-T5-738M",
#     torch_dtype=torch.float32,
#     device_map='auto'
# ) 

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
base_model = AutoModelForCausalLM.from_pretrained(
    checkpoint,
    torch_dtype=torch.float32,
    device_map='auto'
) 

def llm_pipeline():
    pipe = pipeline(
        'text2text-generation',
        model=base_model,
        tokenizer=tokenizer,
        max_length=512,
        do_sample=True,
        temperature=0.3,
        top_p=0.95
    )

    local_llm=HuggingFacePipeline(pipeline=pipe)
    return local_llm


def qa_llm():
    llm=llm_pipeline()
    embeddings=SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')
    db=Chroma(embedding_function=embeddings, persist_directory='db', client_settings=CHROMA_SETTINGS)
    retriever=db.as_retriever()
    qa=RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever,
        return_source_documents='True'
    )
    return qa

def process_answer(instruction):
    # response=''
    instruction=instruction
    qa=qa_llm()
    generated_text=qa(instruction)
    answer=generated_text['result']
    return answer, generated_text

def chat(query):
    question=query
    response, metadata =  process_answer(question)
    print(response)
    ram={'res':response}
    z= json.dumps(ram)
     # llmStream = StringIO(response)
    # data = llmStream.read().decode()

    return z

def main():
    question='what is this paper about?'
    response, metadata = process_answer(question)
    print(response)


if __name__ == '__main__':
    main()