import os
import csv 
import json
import requests

url_prefix = "https://raw.githubusercontent.com/mogith-pn/Assests/refs/heads/main/testing_data/images/"
files = os.listdir("/workspaces/Assests/testing_data/images")
json_path = "/workspaces/Assests/testing_data/annotations"

gt = [('input','metadata')]
for file in files:
    url = f"{url_prefix}{file}"
    json_file = file.replace(".png",".json")
    with open(os.path.join(json_path, json_file)) as f:
        tags = json.load(f)
        gt_word = []
        for word in tags['form']:
            words = [w['text'] for w in word['words']]
            gt_word.extend(words)
    gt.append((url,gt_word))

with open('gt.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(gt)

print(f"Data written")