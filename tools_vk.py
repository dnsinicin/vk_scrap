import sys
import os
from tkinter.filedialog import askopenfilename
import json

sys.path.append("/home/dmitry/anaconda3/lib/python3.7/site-packages")
import vk_api


def get_log(filename):
    session = vk_api.VkApi()
    ff = open(filename, 'r', encoding="utf-8")
    log_list = []
    for line in ff:
        log_list.append(line.rstrip('\n'))
        if len(log_list) == 3:
            session = vk_api.VkApi(
                login=log_list[0],
                password=log_list[1],
                token=log_list[2]
            )
    session.auth()
    log_list = None
    return session.get_api()


def data_to_file(file_to_write):
    with open(file_to_write, 'w', encoding="utf-8") as f:
        f.write(str(data))
    return f


filename = askopenfilename()
file_to_write = 'data1.txt'
vk_ses = get_log(filename=filename)
data = vk_ses.wall.get(domain='skillbox', count=3)
# data_to_file(file_to_write)
item = data.get('items')
print(type(item), len(item))
for i in item:
    print(i)
    print(len(i))
with open(file_to_write, 'w', encoding="utf-8") as f:
    json.dump(item, f)
