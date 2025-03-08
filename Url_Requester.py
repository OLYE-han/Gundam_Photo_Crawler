import requests
from Url_Manager import Url_Manager
from HTML_Message_Drawer import HTML_Message_Drawer

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br"
}

class Url_Requester:
    # 初始化url管理器与html提取器
    def __init__(self):
        self.url_manager = Url_Manager()
        self.drawer = HTML_Message_Drawer("https://wiki.biligame.com")

    # 向url管理器中添加一个待爬取的url
    def add_target_url(self,url):
        self.url_manager.add_new_url(url)
    
    # 向url管理器中添加一个待爬取的url列表
    def add_target_urls(self,urls):
        self.url_manager.add_new_urls(urls)

    # 找到目标url页面中的所有与高达相关的url并添加到url管理器中
    def get_all_related_urls(self,target_url):
        if "?action=edit" in target_url:
            return
        requester = requests.get(target_url,headers=headers)
        if requester.status_code == 200:
            requester.encoding = 'utf-8'
            urls = self.drawer.find_urls(requester)
            self.url_manager.add_new_urls(urls)

    # 从url管理器中提取url并从url请求中提取图片
    def get_request(self):
        url = self.url_manager.get_url()
        requester = requests.get(url,headers=headers)
        if requester.status_code == 200:
            requester.encoding = 'utf-8'
            self.drawer.find_img_url(requester)
            self.drawer.draw_img()


