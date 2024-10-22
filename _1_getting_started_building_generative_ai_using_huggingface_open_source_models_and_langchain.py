# -*- coding: utf-8 -*-
"""#1-Getting Started Building Generative AI Using HuggingFace Open Source Models And Langchain

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pDpktY3QF2whfURl7WEgS0pciCtZBBrs
"""

!pip install langchain-huggingface
# For API calls
!pip install huggingface_hub
!pip install transformers
!pip install accelerate
!pip install bitsandbytes
!pip install langchain

from google.colab import userdata
sec_key = userdata.get('HF_TOKEN')
print(sec_key)

from langchain_huggingface import HuggingFaceEndpoint

import os
os.environ['HF_TOKEN'] = sec_key

repo_id="mistralai/Mistral-7B-Instruct-v0.3"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=sec_key)

llm.invoke("What is machine learning?")

repo_id="mistralai/Mistral-7B-Instruct-v0.3"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=sec_key)

llm.invoke("What is generative AI")

from langchain import PromptTemplate , LLMChain

question = "who won the cricket world cup in the year 2023"

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
print(prompt)

llm_chain = LLMChain(prompt=prompt, llm=llm)
print(llm_chain.invoke(question))

"""HuggingFacePipeline
Among transformers, the Pipeline is the most versatile tool in the Hugging Face toolbox. LangChain being designed primarily to address RAG and Agent use cases, the scope of the pipeline here is reduced to the following text-centric tasks: “text-generation", “text2text-generation", “summarization”, “translation”. Models can be loaded directly with the from_model_id method
"""

from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id="gpt2"
model=AutoModelForCausalLM.from_pretrained(model_id)
tokenizer=AutoTokenizer.from_pretrained(model_id)

pipe=pipeline("text-generation",model=model,tokenizer=tokenizer,max_new_tokens=100)
hf=HuggingFacePipeline(pipeline=pipe)

hf

hf.invoke("What is machine learning")

## Use HuggingfacePipelines With Gpu
gpu_llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    device=0,  # replace with device_map="auto" to use the accelerate library.
    pipeline_kwargs={"max_new_tokens": 100},
)

from langchain_core.prompts import PromptTemplate

template = """Question1: {question}

Answer1:"""
prompt = PromptTemplate.from_template(template)

chain=prompt|gpu_llm

import ast

question="What is Natural lenguaje processing?"
texto =  (chain.invoke({"question":question}))

print(texto)