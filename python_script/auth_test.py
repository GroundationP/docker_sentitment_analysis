import os
import requests
import datetime


# définition de l'adresse de l'API
api_address = "fast_api"
# port de l'API
api_port = 8000

print("******** Starting authentification test ********")


Logins = [["alice", "wonderland"], ["bob", "builder"], ["clementine", "mandarine"]]

for l in Logins:

    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port), params= {'username': '{}'.format(l[0]),'password': '{}'.format(l[1])})

    

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
        
    output = "\n ==> Authentication test at permissions: username={}, password={}, expected result = 200, actual result = {}, {}" .format(l[0], l[1], status_code, test_status)

    print(output.format(status_code=status_code, test_status=test_status))

    # impression dans un fichier
    if os.environ.get('LOG') == '1':
        print('write to file')
        with open('log.txt', 'a') as file:
            file.write('Authentification test time: {}'.format(datetime.datetime.now()))
            file.write(output)
            file.write("\n")
            file.write("=================================================")
            file.write("\n")
            print("=================================================")
            
          
with open('log.txt', 'a') as file:
    file.write("\n")
            