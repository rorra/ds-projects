import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import argparse

from torch.fx.experimental.unification import variables

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

llm = OpenAI(openai_api_key=os.environ['OPENAI_API_KEY']) # Not needed, as ENV['OPENAI_API_KEY'] is used by default

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"],
)
test_prompt = PromptTemplate(
    template="Write a test for the following {language} code:\n{code}",
    input_variables=["language", "code"],
)

code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key="code",
)
test_chain = LLMChain(
    llm=llm,
    prompt=test_prompt,
    output_key="test",
)

chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["task", "language"],
    output_variables=["test", "code"],
)

result = chain({
    "language": args.language,
    "task": "return a list of numbers",
})

print(">>>>>> GENERATED CODE: ")
print(result["code"])

print(">>>>>> GENERATED TEST:")
print(result["test"])
