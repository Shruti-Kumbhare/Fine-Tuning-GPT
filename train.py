import os
import openai
openai.api_key = 'Your_API_key'  #Enter Your Open AI API key here.

file_id = "Your-file-id"   #Enter Your File ID (keep updating when the )
response = openai.FineTuningJob.create(training_file=file_id, 
                                       model="gpt-3.5-turbo")
print(response)
