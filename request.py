import requests
import numpy as np
import json

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

person = [-0.07854, 0.48246, -1.43719, 0.96082, -0.31685,
          3.27393, -2.11437, -0.84732, -1.07533, -2.30408, 0.52975, -1.18084]
j_data = json.dumps({'person': person})

alcohol = 'http://localhost:5000/alcohol/'
amphet = 'http://localhost:5000/amphet/'
amyl = 'http://localhost:5000/amyl/'
benzos = 'http://localhost:5000/benzos/'
caffeine = 'http://localhost:5000/caffeine/'
cannabis = 'http://localhost:5000/cannabis/'
chocolate = 'http://localhost:5000/chocolate/'
coke = 'http://localhost:5000/coke/'
crack = 'http://localhost:5000/crack/'
ecstasy = 'http://localhost:5000/ecstasy/'
heroin = 'http://localhost:5000/heroin/'
ketamine = 'http://localhost:5000/ketamine/'
legal_highs = 'http://localhost:5000/legal-highs/'
lsd = 'http://localhost:5000/lsd/'
magic_mushrooms = 'http://localhost:5000/magic-mushrooms/'
meth = 'http://localhost:5000/meth/'
nicotine = 'http://localhost:5000/nicotine/'
semer = 'http://localhost:5000/semer/'
vsa = 'http://localhost:5000/vsa/'

drugs = [alcohol, amphet, amyl, benzos,
         caffeine, cannabis, chocolate, coke, crack, ecstasy, heroin, ketamine,
         legal_highs, lsd, magic_mushrooms, meth, nicotine, semer, vsa]


for drug in drugs:
    r = requests.post(drug, data=j_data, headers=headers)
    print(f"    {drug[22:-1]} : " + r.text)
