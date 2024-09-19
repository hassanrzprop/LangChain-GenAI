from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain,LLMChain
from dotenv import load_dotenv
import os
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_TOKEN")
)
# Prompt template
# 1) method 1
langchainPrompt = PromptTemplate.from_template("Recipe of {cake} cake")
prompt_output= langchainPrompt.invoke({"cake":"Chocolate"})
prompt11="recipe for cake. output should be in three step and in json format"
print(prompt_output)
# 2) method 2 for prompt template
langchainPromptFinal=PromptTemplate(template= " Recipe of {type} cake", inputVariables=["type"])

result = chat_model.invoke(prompt_output)
print(result)



# Using CHAINING

prompt1=PromptTemplate(template=" translate the following text to French:{text}",inputVariables=["text"])
prompt2=PromptTemplate(template="What is the sentiment of this French Text:{text}",inputVariables=["text"])
chat_model= ChatHuggingFace(llm=llm)   #ChatHuggingFace is used to keep track of what what asked previously

# chain used to handle questions as ouptut of Q1 as input for Q2
chain1=LLMChain(llm=llm,prompt=prompt1)
chain2=LLMChain(llm=llm,prompt=prompt2)

chain = SimpleSequentialChain(chains=[chain1,chain2])
res1=chain.invoke("how are you")
print("RESULT CHAINED",res1)



