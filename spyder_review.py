# -*- coding: utf-8 -*-

import logging
import os
import requests
from bs4 import BeautifulSoup
import json
import time
import random

#获取当前url中的内容
def get_review(url):
    try:
        wb_data = requests.get(url).text
#        print(wb_data)
        return wb_data

    except Exception as e:
        print('error:',e)
        return ""

#根据itemid和page数来爬取评论并存成txt
def review_spider(itemid,n):
    for number in range(n):

        url='https://rate.tmall.com/list_detail_rate.htm?itemId=' + itemid + '&sellerId=201749140&currentPage='+ str(number+1)
        
        web_data = get_review(url)
        
        t = random.randint(0,10)
        time.sleep(t)
        try:
    
            save_path = './Desktop/冰箱'
            with open(save_path + "/" + itemid +'_'+ str(number+1) + '.txt','w',encoding='utf-8') as file_object:
                file_object.write(web_data.strip()) 
                #json.dump(data, file_object)
            print('Successfully done in page '+str(number+1))
        except Exception as e:
            print('ERROR:',e)


if __name__=="__main__":
    
    #需要爬的itemid列表
    itemid = ['548139427167','527080261251','564757424716','564755376111','555147153186','565407577941',
              '547528742234','546410826756','555071736063','563346745172','563346357057','567426531843',
              '546431319023','565219061604','569562918455','564756016803','564940730654','565376223041',
              '555105358684','566731914449','570448923926','566653697202']
    n = 100
    for item in itemid:
        review_spider(item,n)