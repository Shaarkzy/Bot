from colorama import Fore as F
from colorama import Back as B
from colorama import Style as S

import os
print(F.YELLOW)
print("="*64)
print(f"{F.BLACK}         {B.CYAN}{os.getenv('GEMINI_USER_NAME')} Chat Bot : Powered By gemini-2.5-flash"+F.YELLOW, S.RESET_ALL, F.YELLOW)
print("="*64)
from google import genai
import subprocess
import requests

r = F.RED
b = F.BLUE
y = F.YELLOW
c = F.CYAN
g = F.GREEN
w = F.WHITE

start_prompt = ''

def _():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    user = os.getenv("GEMINI_USER_NAME")
    ai_name = os.getenv("GEMINI_NAME")


    num = 0
    memory_ = {}
    global start_prompt
    while True:

        num += 1
        print("━"*64)
        chat = input(f"{w}[{b}*{w}]{F.BLUE}{user}{F.WHITE}: ")

        if "@bye" in chat:
            print("━"*64)
            print(f"{w}[{g}*{w}]{F.GREEN}{ai_name}{F.WHITE}: Goodbye! It was a pleasure chatting with you. Feel free to reach out if you have any more questions in the future.")
            quit(0)
        
        prompt = f"Answer concisely (<= 100 words, 1–10 sentences depending on the context). Be direct and focused.\n\n(here is our previous chat, reply based on the context){start_prompt}: {chat}"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        data = response.text.strip()

        memory_.update({f'query{num}':chat})
        memory_.update({f'reply{num}':data})

        prompt = ''

        for key in memory_.keys():
            prompt += f'{key}:{memory_[key]} &'
        start_prompt = prompt

        print("━"*64)
        print(f"{w}[{g}*{w}]{F.GREEN}{ai_name}{F.WHITE}: ", data)
        
"""        
def fetch_web(query):
    response = requests.get(f"https://www.google.com/search?q={query}")
    return response.text """
    

try:
    _()
except KeyboardInterrupt:
    quit(0)
except Exception as er:
    print(F.RED, "\n", er)
