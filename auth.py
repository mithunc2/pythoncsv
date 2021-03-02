import requests

headers_token = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}



data_token = '{"username":"mithunchandran","password":"Sree@1988"}'

response = requests.post('https://mpidemo.4medica.io/mpi-api/v1/authtoken', headers=headers_token, data=data_token)
response =response.json()
token = response['authToken']

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': token ,
}
params = {
    'facilityId': 'LAB5113',
    'detailedScore': 'false',
    'datasourceRepresentation': 'false',
}

data = '{"id":"as3389","alternateId":[{"id":"12370"}],"commonKey":"CK-MIHIN#1789654asddf4353454354","datasourceId":[{"id":"DefaultDS"}],"facilityLocalId":[{"id":"A176954","idSrc":"QL"}],"firstname":["mithun "],"lastname":["chandran"],"middlename":"C","suffix":["Jr."],"nickname":["mithun"],"sex":"M","dateOfBirth":"19890306","personalId":[{"id":"DL10189","type":"DL","validity":true}],"ssn":"771-88-8894","address":[{"addressLine1":"Divya nivas","addressLine2":"Palakkad","city":"Phoenix","county":"Pinal","state":"AZ","postalCode":85123,"addressValidity":true,"addressNormalized":false,"postalCode5Digits":85129}],"phone":[{"number":8395559559,"type":"H","validity":true}],"email":[{"address":"mark_tom@usmail.com","validity":true}],"race":["C"],"ethnicity":["H"],"custom":[{"value":"Blue","type":"PrId"}],"deceased":true}'

response = requests.post('https://mpidemo.4medica.io/mpi-api/v1/identities', headers=headers, params=params, data=data)

print (response.text)
# The script to add data to mpi