import os
import requests
import datetime


# définition de l'adresse de l'API
api_address = "fast_api"
# port de l'API
api_port = 8000

print("******** Starting Content test ********")


Logins = [
["alice", "wonderland", "life is beautiful"], 
["alice", "wonderland", "that sucks"], 
["bob", "builder", "life is beautiful"], 
["bob", "builder", "that sucks"], 
["clementine", "mandarine", "life is beautiful"], 
["clementine", "mandarine", "that sucks"] 
]

for l in Logins:

    r1 = requests.get(url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port), params= {'username': '{}'.format(l[0]),'password': '{}'.format(l[1]), 'sentence': '{}'.format(l[2])})
    r2 = requests.get(url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port), params= {'username': '{}'.format(l[0]),'password': '{}'.format(l[1]), 'sentence': '{}'.format(l[2])})

    print(r1.text)
    print(r2.text)
            
    if os.environ.get('LOG') == '1':
        print('write to file')
        with open('log.txt', 'a') as file:
            file.write('Content test time for {} using the sentence {} : {}'.format(l[0], l[2], datetime.datetime.now()))
            file.write("\n")
            file.write('==> Content test : {}'.format(r1.text))
            file.write("\n")
            file.write('==> Content test : {}'.format(r2.text))
            file.write("\n")
            file.write("=================================================")
            file.write("\n")
            print("=================================================")
            
            
with open('log.txt', 'a') as file:
    file.write("\n")
            