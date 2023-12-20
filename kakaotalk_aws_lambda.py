import json
import openai
import boto3
#import requests
#import asyncio

def lambda_handler(event, context):
    
    
    #type() 함수로 자료형 확인하기
    #print('event type=', type(event))
    #event_json = json.loads(event)
    #print("event dump=", json.dumps(event))
    body = event["body"]
    #print("body=", body)
    body_json = json.loads(body);
    print("body_json=", json.dumps(body_json))
    #userRequest_json = body_json["userRequest"]
    #print("userRequest_json=", json.dumps(userRequest_json))
    #utterance_json = userRequest_json["utterance"]
    #print("utterance_json=", json.dumps(utterance_json))
    
    utterance = body_json["userRequest"]["utterance"];
    print("utterance=", utterance)
    # model_to_use = "text-davinci-003"
    model_to_use = "gpt-3.5-turbo"
    ## input_prompt="Write an email to Elon Musk asking him why he bought Twitter for such a huge amount"
    # messages_to_use = [{"role": "user", "content": "What is the OpenAI mission?"}]
    # messages_to_use = [{"role": "user", "content": utterance}]
    query = utterance
    messages_to_use = [{"role": "system", "content":"You are a helpful assistant that helps users generate ..."},  
    {"role":"user", "content": query}]
    print("messages_to_use=", messages_to_use)
    
    
    
    # openai.api_key = 'sk-aaaa'
    #openai.api_key = 'sk-bbb'
    # response = openai.Completion.create(model=model_to_use, prompt=input_prompt,temperature=0, max_tokens=100, top_p=1,frequency_penalty=0.0, presence_penalty=0.0)
    #response = openai.Completion.create(model=model_to_use, prompt=input_prompt)
    #print(response)
    #text_response = response['choices'][0]['text'].strip()
    #text_response = response['choices'][0].message[0].role.user.content.strip()
    response = openai.ChatCompletion.create(model=model_to_use, messages=messages_to_use)
    text_response = response['choices'][0].message.content.strip()
    
    print("gpt_response=", text_response)
    #return {
    #    'statusCode':200,
    #    'body': {
    #       'response' : text_response
    #        'response' : 'OK'
    #    }
    #}
    
    
    
    #callbackUrl = body_json["userRequest"]["callbackUrl"];
    #if callbackUrl :
    #  payload = {
    #      "version": "2.0",
    #      "template": {
    #          "outputs": [
    #              {
    #                  "simpleText": {
    #                      "text": text_response
    #                  }
    #              }
    #          ]
    #      }
    #  }
    #  response = requests.post(callbackUrl, json=payload)
    #  print(response.text) #TEXT/HTML
    #  print(response.status_code, response.reason) #HTTP
      
    
    outputStr = text_response
    return {
      "statusCode": 200,
      "body": {
        "version": "2.0",
#        "useCallback" : True,
        "template": {
          "outputs": [
            {
              "simpleText": {
                "text": outputStr
              }
            }
          ]
        }
      }
    }
#elif outputType == 'simpleImage':
#	_ret = {"version": "2.0",
#			"template": {"outputs": [{'simpleImage': {"altText": outputType,
#			"imageUrl": "https://store.stocksidekick.xyz/static/images/ryan.png"}}] #"template"의 "outputs" 키 내에
#						}
#			}


#async def get_urls(event):
#    return {'msg':'Hello World'}