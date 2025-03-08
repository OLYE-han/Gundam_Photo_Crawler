from bs4 import BeautifulSoup
from Url_Manager import Url_Manager
import os
import requests

class HTML_Message_Drawer:
    # 用网站的根域名对类进行初始化
    def __init__(self,url):
        self.root_url = url
        self.img_url_manager = Url_Manager()

    # 从自身的img_url_manager中把所有高达“图片的url”都访问一遍并存储在img目录下
    def draw_img(self):
        while(len(self.img_url_manager.new_urls)>0):
            url = self.img_url_manager.get_url()
            if url == None:return
            requester = requests.get(url)
            soup = BeautifulSoup(requester.text,"html.parser")
            img_nodes = soup.find("div",class_="fullMedia")
            img_node = img_nodes.find("a",class_="internal")
            if img_node.has_attr("href"):
                src = img_node["href"]
                filename = os.path.basename(src)
                if 'jpg'  in src:
                    filename = filename.split(".jpg")[0] + ".jpg"
                elif "png" in src:
                    filename = filename.split(".png")[0] + ".png"
                print(filename)
                with open (f"img/{filename}","wb") as f:
                    requrested_img = requests.get(src)
                    f.write(requrested_img.content)
        return

    # 找到目前请求页面下所有与高达有关的“页面的url”并将其返回
    def find_urls(self,requester):
        soup = BeautifulSoup(requester.text,"html.parser")
        url_nodes = soup.find("div",class_="mw-parser-output")
        if url_nodes==None:return
        url_nodes = url_nodes.find_all("a")
        urls = []
        for url_node in url_nodes:
            if(url_node.has_attr('href') ):
                if url_node.has_attr('title') and "高达" in url_node["title"]:
                    urls.append(self.root_url + url_node['href'])
        return urls
    
    # 找到目前请求页面下所有高达“图片的url”并存入自身的img_url_manager中
    def find_img_url(self,requester):
        soup = BeautifulSoup(requester.text,"html.parser")
        url_nodes = soup.find("div",class_="mw-parser-output")
        if url_nodes==None:return
        url_nodes = url_nodes.find_all("a",class_="image")
        for url_node in url_nodes:
            if(url_node.has_attr("href")):
                img_url = self.root_url + url_node["href"]
                # print(img_url)
                self.img_url_manager.add_new_url(img_url)
        return

