import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
headers = {"Authorization": f"Bearer {'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'}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

data = input("Enter the text:")
output = query({"inputs":data})
#print(output)

for key, val in output[0][0].items():
      Neg = val*100
#print(Neg)
for key,val in output[0][1].items():
	Neu = val*100
#print(Neu)	
for key,val in output[0][2].items():
	Pos = val*100
#print(Pos)	 
 








 