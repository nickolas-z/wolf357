import os
import pickle
from openai import OpenAI
from pathlib import Path


API_KEY_PATH = Path(__file__).parent.parent.joinpath("secret_key.bin")  # todo find solution from error FileNotFoundError: [Errno 2] No such file or directory: 'stathem_bot/secret_key.bin'





def get_api_key():
    if os.path.exists(API_KEY_PATH):
        with open(API_KEY_PATH, 'rb') as file:
            #api_key = (file.read()).decode()   # todo find solution for decoding
            api_key = pickle.load(file)
            
    else:
        while True:
            user_input = input("Введіть API KEY from OpenAI: ")
            if len(user_input) == 51 and user_input.startswith("sk-"):
                api_key = user_input
                with open(API_KEY_PATH, 'wb') as file:
                    # file.write(api_key.encode())  # todo find solution for encoding
                    pickle.dump(api_key, file)
                break
            else:
                print("API KEY is not valid, should be like sk-....")
    return api_key


def gpt_handler(client: OpenAI, user_input: str, prompt: str):

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt.format(question=user_input)}
    ]
    )
    return response.choices[0].message.content

def main():
    api_key = get_api_key()
    client = OpenAI(api_key=api_key)
    prompt = "Дай відповідь у стилі Стетхема на насупне питання, важливо тримати стиль Стетхема з мемів та відповідай на Українській мові: {question}"
    while True:
        user_input = input("Введіть запит: ")
        if user_input in ['q', 'exit']:
            break
        answer = gpt_handler(client=client, user_input=user_input, prompt=prompt)
        print(answer)
        



if __name__ == "__main__":
    main()



