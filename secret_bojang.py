#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import json
from flask import Flask
from flask import redirect
import urllib.request as req


# In[2]:


def get_last_watch():
    with open('watch.json','r') as f:# 상대 경로를 절대 주소로 변경 필요
        json_data = json.load(f)
        return json_data['watch']

def set_last_watch(value):
    with open('watch.json','r') as f:  # 상대 경로를 절대 주소로 변경 필요
        json_data = json.load(f)
    json_data['watch'] = int(value) + 1

    with open('watch.json','w', encoding = 'utf-8') as json_file:# 상대 경로를 절대 주소로 변경 필요
        json.dump(json_data, json_file, indent = '\t')

def get_secret_bojang_url(keyword):
    filename = 'adress.json' # 상대 경로를 절대 주소로 변경 필요
    with open(filename,'r') as f:
        json_data = json.load(f)
    if (keyword in json_data):
        set_last_watch(keyword)
        return json_data[keyword]
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    url = 'http://www.podbbang.com'
    query = url + '/podbbangchnew/episode_list'
    param = {'id':'12757','page':'','e': '','sort':'latest','page_view':'','keyword':keyword}
    res = requests.get(query, params=param)
    bs4 = BeautifulSoup(res.content,'lxml')
    a = bs4.select('script')
    script = str(a[1]).split()
    result = []
    for i in script:
        if ('down_file' in i):#| ('share_title' in i):
            result.append(i)
    target = keyword+'.mp3'
    for i in result:
        data = i.split(':',maxsplit=1) 
        data[1] = data[1].replace(',','')
        filename = data[1].split('/')[-1]
        filename = re.findall("\d+",filename)
        if filename[0] == keyword:
            ret = data[1]
            with open('adress.json','r') as f:  # 상대 경로를 절대 주소로 변경 필요
                jj = json.load(f)
                jj[keyword] = ret
            with open('adress.json','w', encoding = 'utf-8') as json_file:# 상대 경로를 절대 주소로 변경 필요
                json.dump(jj, json_file, indent = '\t')
            set_last_watch(keyword)
            return ret



