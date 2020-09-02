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
    set_last_watch(keyword)
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    url = 'http://www.podbbang.com/_m_api/podcasts/12757/episodes'
    param = {'offset':'0', 'sort' :'pubdate:desc', 'episode_id':'0','keyword':keyword,'limit':'8','with':'summary','cache':'0'}
    res = requests.get(url, params=param)
    json_data = res.json()
    url = json_data['data'][0]['enclosure']['url']
    return url



