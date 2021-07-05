import sys
import os
from tkinter.filedialog import askopenfilename
import json
import pandas as pd

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
    ff.close()
    session.auth()
    log_list = None
    return session.get_api()


def get_group():
    group_name = askopenfilename()
    group_list = []
    with open(group_name, 'r', encoding="utf-8") as f:
        for line in f:
            group_list.append(line.rstrip('\n'))
    return group_list


def get_data(dom_name):
    data = vk_ses.wall.get(domain=dom_name, count=100)
    count = int(data.get('count')) // 100
    items = data.get('items')
    for i in range(1, count + 1):
        items = items + vk_ses.wall.get(domain=dom_name, offset=i * 100)['items']
    return items


filename = askopenfilename()
vk_ses = get_log(filename=filename)
list_groups_vk = get_group()
for elem in list_groups_vk:
    item = get_data(dom_name=elem)
    df = pd.DataFrame.from_dict(pd.json_normalize(item), orient='columns')
    df.to_csv(f'{elem}.csv', sep=',', index_label='index')
