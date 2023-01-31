#!/usr/bin/env python3

import os,glob,csv,json

def get_all_keys(list_of_dicts):
    all_keys = set()
    for row in list_of_dicts:
        for key in row.keys():
            all_keys.add(key)
    return all_keys

for json_file in glob.glob(os.path.join('.', '*.json')):
    print(json_file)
    data = json.load(open(json_file, 'rt', encoding='utf8'))

    all_keys = get_all_keys(data)

    with open(json_file.replace('.json', '.csv'), 'w', encoding='utf8') as file:
        writer = csv.DictWriter(file, all_keys)
        writer.writeheader()
        writer.writerows(data)