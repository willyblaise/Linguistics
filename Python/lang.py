import os

from dotenv import load_dotenv

from langchain.llms import OpenAI

load_dotenv()

#os.environ['OPENAI_API_KEY'] = 
#OPENAI_API_KEY = os.environ.get('OPEN_API_KEY')
OPENAI_API_KEY = 


def main():
    quest = input("What can i help you with? ")
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    #result = llm.predict("Give me 5 Topics related to foods needed for eating healthier")
    result = llm.predict(quest)
    print(result)



if __name__ == "__main__":
    print(OPENAI_API_KEY)
    main()
