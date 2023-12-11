import openai
import json
from google.colab import drive

def complete_message(messages, temperature=1, max_tokens=4293):

  completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

  return completion.choices[0].message.content


def complete_prompt_with_data(prompt, data, temperature=1, max_tokens=4293):
  messages=[
            {
                "role": "system",
                "content": prompt
            }
            ,            {
                "role": "user",
                "content": data
            }
        ]
  return complete_message(messages, temperature, max_tokens)


def read_contents(file_path) :
  try:
      with open(file_path, 'r') as file:
          # Read the entire contents of the file
          file_contents = file.read()
      return file_contents
  except FileNotFoundError:
      print(f"The file '{file_path}' does not exist.")
  except Exception as e:
      print(f"An error occurred: {e}")



drive.mount('/content/drive')

file_path = "/content/drive/MyDrive/datas/kt_c.txt"

file_path = "/content/drive/MyDrive/datas/kt_c.txt"
contents = read_contents(file_path)

prompt = """
다음 데이터를 '제목 : 내용'으로 형식으로 정형화해줘.
입력 데이터에서 '#'로 시작하는 문장은 제목에 해당해.
'-'로 시작하고 ':'로 끝나는 문장은 제목이야.
문장에 '|'가 두 개 이상있다면 문장의 처음부터 첫번쩨 '|'까지가 제목이야 
문장에 ':'가 하나 이상 있다면 처음부터 첫번쩨 ':'까지가 제목이야
"""
result = complete_prompt_with_data(prompt, contents, 1, 8500)
print(result)