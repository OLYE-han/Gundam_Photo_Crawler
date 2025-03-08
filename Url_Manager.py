class Url_Manager:
    # 初始化
    def __init__(self):
        # new_urls中存储着未爬取的url
        # old_urls中存储着已爬取的url
        self.new_urls = set()
        self.old_urls = set()
    
    # 向new_urls中添加新的未爬取url
    def add_new_url(self,url):
        # 判断url是否满足条件或者已经在new_urls或old_urls中
        # 不在的话添加进入new_urls
        if url is None or len(url)==0:
            return
        if "http://" not in url and "https://" not in url:
            return
        if url in self.new_urls or url in self.old_urls:
            return

        self.new_urls.add(url)
    
    # 向new_urls中批量添加未爬取的url
    def add_new_urls(self,urls):
        # 调用add_new_url实现该函数
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    
    # 从new_urls中取出一个url返回，并将该url存入old_urls中
    def get_url(self):
        # 如果有url就取出，否则返回None
        if len(self.new_urls)>0:
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None