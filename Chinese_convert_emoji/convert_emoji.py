import requests
import json
from lxml import etree

def get_table_from_html(html):
    tree = etree.HTML(html)
    # 寻找所有的table标签
    emoji_lst = tree.xpath("//div[@class='emoji_card']/a[@class='emoji_font']/text()")
    chinese_lst = tree.xpath("//div[@class='emoji_card']/a[@class='emoji_name truncate']/text()")
    emoji_chinese_lst = []
    chinese_emoji_lst = []
    if len(emoji_lst) != len(chinese_lst):
        print("长度不等")
    for i in range(len(emoji_lst)):
        emoji_chinese_lst.append({emoji_lst[i]:chinese_lst[i]})
        chinese_emoji_lst.append({chinese_lst[i]:emoji_lst[i]})
    return emoji_chinese_lst,chinese_emoji_lst

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    return res.text

def run(url):    
    html = get_html(url)
    emoji_Chinese_list,Chinese_emoji_list = get_table_from_html(html)# 结构是比较简单的
    return emoji_Chinese_list,Chinese_emoji_list
    
if __name__ == '__main__':
    url = 'https://www.emojiall.com/zh-hans/all-emojis'
    emoji_Chinese_list,Chinese_emoji_list = run(url)
    with open('emoji_Chinese.json','a',encoding='utf-8') as f:
        json.dump(emoji_Chinese_list,f,ensure_ascii=False,indent=4)
    with open('Chinese_emoji.json','a',encoding='utf-8') as f:
        json.dump(Chinese_emoji_list,f,ensure_ascii=False,indent=4)
    
