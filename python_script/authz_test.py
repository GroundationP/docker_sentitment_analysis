import os
import requests
import datetime
import json


# définition de l'adresse de l'API
api_address = "fast_api"
# port de l'API
api_port = 8000

def Print_Output(l, output):
    if os.environ.get('LOG') == '1':
        print('write to file')
        with open('log.txt', 'a') as file:
            file.write('Authorization test time for {} at {}'.format(l[0], datetime.datetime.now()))
            file.write("\n")
            file.write('==> Authorization test : {}'.format(output))
            file.write("\n")
            file.write("=================================================")
            file.write("\n")
            print("=================================================")
            
            
print("******** Starting authorization test ********")


Logins = [
["alice", "wonderland", "life is beautiful"], 
["bob", "builder", "life is beautiful"]
]

#["alice", "wonderland", "life is beautiful"],  ["alice", "wonderland", "that sucks"], 

for l in Logins:

    r1 = requests.get(url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port), params= {'username': '{}'.format(l[0]),'password': '{}'.format(l[1]), 'sentence': '{}'.format(l[2])})
    r2 = requests.get(url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port), params= {'username': '{}'.format(l[0]),'password': '{}'.format(l[1]), 'sentence': '{}'.format(l[2])})

    rtext1 = json.loads(r1.text)
    rtext2 = json.loads(r2.text)
    
    output = ""
    try:
        if l[0] == rtext1["username"] and l[0] == rtext2["username"]:
            print("The versions V1 and V2 works for {}".format(l[0]))
            output = "The version V1 and V2 works for {}".format(l[0])
            Print_Output(l, output)
    except:
        pass
           
    try:
        if l[0] == rtext1["username"] and rtext2["detail"] == 'This service is not included in your plan.':
            print("The version V1 only works for {}".format(l[0]))
            output = "The version V1 only works for {}".format(l[0])
            Print_Output(l, output)
        
        else:
            print("User is not authorized")
            output = "User is not authorized"
            Print_Output(l, output)
    except:
        print("User not recognized")
        

with open('log.txt', 'a') as file:
    file.write("\n")
            
            
