# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 15:23:12 2018

@author: Ren_xc
"""

import urllib.request
import re
import chardet
import os

date_begin = int(input("date_begin(mmdd):"))
date_over = int(input("date_over(mmdd):"))

for pic_date in range(date_begin,date_over+1):
    date_str = str(pic_date)+'/'
    url_date = r'http://222.195.136.24/chart/cma/201812/2018'+date_str
    res = urllib.request.urlopen(url_date)
    buf = res.read()
    encode_type = chardet.detect(buf)
    buf = buf.decode(encode_type['encoding'])
    link_sfc_list = re.findall(r"(?<=href=\").+?(?=_china.jpg\")|(?<=href=\').+?(?=_china.jpg\')" ,buf)
    link_up5_list = re.findall(r"(?<=href=\").+?(?=_asia_50.jpg\")|(?<=href=\').+?(?=_asia_50.jpg\')" ,buf)
    link_up7_list = re.findall(r"(?<=href=\").+?(?=_asia_70.jpg\")|(?<=href=\').+?(?=_asia_70.jpg\')" ,buf)
    link_up8_list = re.findall(r"(?<=href=\").+?(?=_asia_85.jpg\")|(?<=href=\').+?(?=_asia_85.jpg\')" ,buf)
    link_nsp_list = re.findall(r"(?<=href=\").+?(?=_nsph_50.jpg\")|(?<=href=\').+?(?=_nsph_50.jpg\')" ,buf)
    for sfc_time in link_sfc_list:
        url_pic = r'http://222.195.136.24/chart/cma/201812/2018'+date_str+sfc_time+'_china.jpg'
        res_pic = urllib.request.urlopen(url_pic)
        html = res_pic.read()
        # 将图片保存到文件夹中，如果没有该文件夹则创建
        path = "D:\\work\\forecast\\data\\sfc"
        if not os.path.isdir(path):
            os.makedirs(path)
        paths = path+'\\'
        f = open(paths+sfc_time+".jpg", 'wb')
        f.write(html)
        f.close
    for up5_time in link_up5_list:
        url_pic = r'http://222.195.136.24/chart/cma/201812/2018'+date_str+up5_time+'_asia_50.jpg'
        res_pic = urllib.request.urlopen(url_pic)
        html = res_pic.read()
        f = open("D:\\work\\forecast\\data\\500hpa\\"+up5_time+".jpg", 'wb')
        f.write(html)
        f.close
    for up7_time in link_up7_list:
        url_pic = r'http://222.195.136.24/chart/cma/201812/2018'+date_str+up7_time+'_asia_70.jpg'
        res_pic = urllib.request.urlopen(url_pic)
        html = res_pic.read()
        f = open("D:\\work\\forecast\\data\\700hpa\\"+up7_time+".jpg", 'wb')
        f.write(html)
        f.close
    for up8_time in link_up8_list:
        url_pic = r'http://222.195.136.24/chart/cma/201812/2018'+date_str+up8_time+'_asia_85.jpg'
        res_pic = urllib.request.urlopen(url_pic)
        html = res_pic.read()
        f = open("D:\\work\\forecast\\data\\850hpa\\"+up8_time+".jpg", 'wb')
        f.write(html)
        f.close
    for nsp_time in link_nsp_list:
        url_pic = r'http://222.195.136.24/chart/cma/201812/2018'+date_str+nsp_time+'_nsph_50.jpg'
        res_pic = urllib.request.urlopen(url_pic)
        html = res_pic.read()
        f = open("D:\\work\\forecast\\data\\nsph\\"+nsp_time+".jpg", 'wb')
        f.write(html)
        f.close

# downroad aqi
url_aqi = 'http://www.beijing-air.com/'
req_aqi = urllib.request.urlopen(url_aqi)
buf_aqi = req_aqi.read()
encode_type = chardet.detect(buf_aqi)
buf_aqi = buf_aqi.decode(encode_type['encoding'])
imglist=re.findall(r'(http:.+?w2.+?\.jpg)',buf_aqi)
f = open("D:\\work\\forecast\\data\\fct\\aqi.jpg", 'wb')
img_html=urllib.request.urlopen(imglist[0])
picture=img_html.read()
f.write(picture)
f.close

# downroad meteorological elements
fr = '2018'+str(date_begin)
to = '2018'+str(date_over)
urls = []
url_http = 'http://envf.ust.hk/dataview/stnplot/current/plot_image.py?lat=400700&lon=1165800&fr='
urls.append(url_http+fr+'&to='+to+'&tbl=a_temp&tz=8')
urls.append(url_http+fr+'&to='+to+'&tbl=a_wind&tz=8')
urls.append(url_http+fr+'&to='+to+'&tbl=a_dew_pt&tz=8')
urls.append(url_http+fr+'&to='+to+'&tbl=a_vis_ax&tz=8')
urls.append(url_http+fr+'&to='+to+'&tbl=a_rh_vt&tz=8')
urls.append(url_http+fr+'&to='+to+'&tbl=a_pre_stn&tz=8')
urls.extend(['temp', 'wind', 'dew', 'vis', 'rh', 'pre'])
for i in range(0,6):
    img_html=urllib.request.urlopen(urls[i])
    f = open("D:\\work\\forecast\\data\\fct\\"+urls[i+6]+".jpg", 'wb')
    picture=img_html.read()
    f.write(picture)
    f.close
