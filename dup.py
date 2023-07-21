import json
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/patent_data')

json_file = 'patent1.json'

with open(json_file, 'r') as file:
    data = json.load(file)

existing_ids = set((doc['patent_number']) for doc in solr.search('*:*', fl='patent_number'))

filtered_data = [doc for doc in data['patents'] if (doc['patent_number']) not in existing_ids]

solr.add(filtered_data)
solr.commit()