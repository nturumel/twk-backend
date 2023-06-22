from typing import Dict, List

from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings


refine_template = """
Here is a Human input and an AI response:
---
Input: {input}
Response: {response}
---
Please modify the AI response to match the tone of the responses
in the following examples as closely as possible while ensuring
the information in the original response remains unchanged.

Examples are in the format:
Input:
Response:

If no change is necessary, return the response as is.

-----
Examples:
{examples}
------
"""

refine_prompt = PromptTemplate(
    input_variables=["input", "response", "examples"], template=refine_template
)


class ExampleRefineChain:
    example_prompt = PromptTemplate(
        input_variables=["input", "response"],
        template="Input: {input}\n Response: {response}",
    )
    examples: List[Dict]
    refine_chain: LLMChain
    example_selector: SemanticSimilarityExampleSelector

    def __init__(self, examples: List[Dict]):
        self.examples = examples
        self.example_selector = SemanticSimilarityExampleSelector.from_examples(
            examples=examples,
            embeddings=OpenAIEmbeddings(),
            vectorstore_cls=Chroma,
            k=3,
        )
        llm = OpenAI(temperature=0.5)

        self.refine_chain = LLMChain(llm=llm, prompt=refine_prompt)

    def refine_response(self, input: str, response: str) -> str:
        selected_examples = self.example_selector.select_examples({"input": input})
        refined_response: str = self.refine_chain.predict(
            input=input, response=response, examples=selected_examples
        )
        return refined_response
