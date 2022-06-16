import requests

response = requests.get('http://ddragon.leagueoflegends.com/cdn/12.11.1/data/en_US/champion.json').json()
data = response['data']
championNames = [name for name in data]

#print(championNames)

champIds = []
for i in range(len(championNames)):
    champIds.append(data[f'{championNames[i]}']['key'])

#print(champIds)

champIdDict = dict(zip(champIds,championNames))

print(champIdDict)