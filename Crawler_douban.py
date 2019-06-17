# coding=utf-8
import json
import requests



class Crawler:
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=1560739385509"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
            , "Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288"}

    def get_content_list(self, html_str):  #提取数据
        dict_data = json.loads(html_str)
        # print(dict_data)
        content_list=dict_data["subject_collection_items"]
        total=dict_data["total"]
        return  content_list,total

    def save_content_list(self, content_list):  #保存数据
        with open("douban.json", "a", encoding="utf-8") as f:
            for content in content_list:
                print(content)
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")

    def run(self):  #实现主要逻辑
        num = 0
        total = 50
        while num < total + 18:
            # 1.start_url
            start_url = self.temp_url.format(num)
            # print(start_url)
            # 2.发送数据,获取响应
            html_str = self.parse_url(start_url)
            # 3.提取数据
            content_url,total=self.get_content_list(html_str)
            # print(content_url)
            # 4.保存
            self.save_content_list(content_url)
            # 5.构造下一个的url地址,循环2-步
            num+=18

    def parse_url(self, start_url):  # 发起请求
        response=requests.get(start_url,headers=self.headers)
        return response.content.decode()

if __name__ == '__main__':
    crawler= Crawler()
    crawler.run()

