from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API')

def translate(text: str) -> None:
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Translate the words, sentences or in the specified text in {in_language} to {to_language}: {text}',
        max_tokens=4096,
        temperature=0
    )
    
    return response['choices'][0]['text'].strip()

if __name__ == '__main__':
    try:
        in_language = input("Would you like translate in: ")
        to_language = input("To: ")
        text = input("Inform the word, sentence or text that would you like to translate: ")
        print(translate(text))
    except openai.InvalidRequestError as e:
        print(e)

