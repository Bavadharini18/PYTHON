import json
import hashlib
import pysolr


solr = pysolr.Solr('http://localhost:8983/solr/patent_data')

json_file = 'patent1.json'

with open(json_file, 'r') as file:
    data = json.load(file)

file_hash = hashlib.md5(json.dumps(data, sort_keys=True).encode()).hexdigest()

existing_files = solr.search(f'file_hash:{file_hash}')
if existing_files.hits > 0:
    print('File has already been indexed.')
    exit()

for doc in data:
    doc['file_hash'] = file_hash


solr.add(data)


solr.commit()

print('Data indexed successfully.')
