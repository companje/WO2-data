#!/usr/bin/env python3

import requests, json, csv
api = "https://api.data.netwerkdigitaalerfgoed.nl/queries/hetutrechtsarchief/"

queries = ["wo2-documenten", "wo2-brontypes", "wo2-personen", "wo2-adressen-per-document", "wo2-adressen", "wo2-persoon-op-adres-per-document"]

for query in queries:
    rows = []
    for i in range(1,5):
        url = api+query+"/run.json?pageSize=10000&page="+str(i)
        response = requests.get(url)
        data = response.json()
        rows = rows + data

    json.dump(rows, open(f"{query}.json","w"), indent=2)
    