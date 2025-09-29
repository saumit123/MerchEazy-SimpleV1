from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from pydantic import BaseModel,Field
from typing import List,Optional
import json

from src.core.prompts import PROMPT_TEMPLATES

from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    temperature=0.2,
    max_tokens=512
)

class InvoiceItem(BaseModel):
    name: str = Field(description="The name of the Item.")
    qty: str = Field(description="The quantity of the item (e.g., '5 kg', '2', '1 bottle').")
    qty_num: float = Field(description="The numeric quantity like 5 from 5kg or 3 from 3 bottles")
    category: str = Field(description="The category of the item (e.g., 'produce', 'cleaning supplies', 'personal care', 'pantry').")

class InventoryItem(BaseModel):
    items: list[InvoiceItem] = Field("List of items with name,quantity and category from a users request.")


# print(PROMPT_TEMPLATES['grocery_list'])

# prompt_template = PROMPT_TEMPLATES['grocery_list']

def process_grocery_list(text: str) -> dict:

    try:
        parser = PydanticOutputParser(pydantic_object=InventoryItem)
        prompt_string = PROMPT_TEMPLATES["grocery_list"]
        
        prompt = PromptTemplate(
            template=prompt_string,
            input_variables=["text"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        
        # This is where you can print the prompt for testing
        print("--- Generated Prompt ---")
        print(prompt.format(text=text))
        print("------------------------")

        chain = prompt|llm 
        llm_response = chain.invoke({"text":text})

        if hasattr(llm_response, "content"):
            llm_response_content = llm_response.content
        else:
            raise ValueError("LLM response does not contain 'content' attribute.")

        # Print the raw LLM response
        print("\n--- Raw LLM Response ---")
        print(llm_response_content)
        print("------------------------")
        
        # structured_data = parser.parse(llm_response_content)
        return llm_response_content

    except Exception as e:
        print(f"Error in LangChain processing: {e}")
        return {"items": []}
    

# if __name__ == "__main__":
#     test_text = "I need 5 kg of onions, 2 dishwash gels, and 1 Nivea body wash."
#     print("Running a direct test for llm_chain.py...\n")
#     processed_list = process_grocery_list(test_text)
    
#     print("\n--- Final Structured Data ---")
#     print(json.dumps(processed_list, indent=2))
#     print("----------------------------")

