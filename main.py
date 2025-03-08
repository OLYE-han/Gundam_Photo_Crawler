from Url_Requester import Url_Requester

# 主循环，其中page_num用于限定提取的url个数，自行设定以防硬盘存爆
if __name__ == '__main__':
    page_num = 20
    My_requester = Url_Requester()
    # 以下网页就是高达图片网站
    My_requester.get_all_related_urls("https://wiki.biligame.com/gundam/RX-78-2%E9%AB%98%E8%BE%BE")
    url = My_requester.url_manager.get_url()
    count = 0
    while(url and count < page_num):
        My_requester.get_request()
        My_requester.get_all_related_urls(url)
        url = My_requester.url_manager.get_url()
        count += 1