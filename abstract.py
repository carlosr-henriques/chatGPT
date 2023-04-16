from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API')

def read_file(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as read_file:
        return read_file.read()

def abstract(file: str) -> None:
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Make a abstract about the text file: {file}',
        max_tokens=4096,
        temperature=1
    )
    
    return response['choices'][0]['text'].strip()

if __name__ == '__main__':
    file = read_file('text_file.txt')
    try:
        print(abstract(file))
    except openai.InvalidRequestError as e:
        print(e)

