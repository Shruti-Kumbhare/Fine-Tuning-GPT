import openai
openai.api_key = 'Your_API_key' #Enter Your Open AI API key here.

response = openai.File.create(
  file=open("data.jsonl", "rb"),  #Replace data.jsonl with the name of your .jsonl file. 
  purpose='fine-tune'
)
print(response)     #run this file to acquire the file id which is required in train.py file.