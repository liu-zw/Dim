import json
import requests
import uuid

pic_name = []
pic_info = []
exist_pic = []


url = 'https://api.github.com/repos/liu-zw/Dim/git/trees/master?recursive=1'
data_orig = requests.get(url).text
x = 1
while x > 0:
    x = data_orig.find('img/')
    data_orig = data_orig[x+4:]
    y = data_orig.find('",')
    pic_name.append(data_orig[:y])
del pic_name[-1]

for i in pic_name:
    temp = {'fileName': i, 'width': 1920, 'height': 1080,
            'extname': i[i.find('.'):],
            'imgUrl': 'https://cdn.jsdelivr.net/gh/liu-zw/Dim@master/img/'+i,
            'type': 'github', 'id': str(uuid.uuid1())}
    pic_info.append(temp)

with open('C:\\Users\\liuzw\\AppData\\Roaming\\picgo\\data.json', 'r', encoding='utf-8') as f:
    data_file = json.loads(f.read())
    for i in data_file['uploaded']:
        exist_pic.append(i)
    data_file['uploaded'][:] = pic_info

with open('C:\\Users\\liuzw\\AppData\\Roaming\\picgo\\data.json', 'r+', encoding='utf-8') as f:
    f.write(json.dumps(data_file, sort_keys=True,
                       indent=4, separators=(',', ':')))
