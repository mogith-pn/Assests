import os
import json
import requests

url_prefix = "https://raw.githubusercontent.com/mogith-pn/Assests/refs/heads/main/testing_data/images/"
files = os.listdir("/workspaces/Assests/testing_data/images")
img_urls = [ f"{url_prefix}{file}" for file in files]

json_path = "/workspaces/Assests/testing_data/annotations"
meta_files = os.listdir(json_path)

all_list = []
for file in meta_files:
    
    print("Inside file", file)
    with open(os.path.join(json_path, file)) as f:
        tags = json.load(f)
        gt_word = []
        for word in tags['form']:
            words = [w['text'] for w in word['words']]
            gt_word.extend(words)
        all_list.append((file[0:-4],gt_word))
    
print("total records",len(all_list))

            
    