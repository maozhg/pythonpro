from bs4 import BeautifulSoup
# 导入所需要的库
import requests

# 使用requests进行一次网页请求，把返回的response信息放在wb_data
url = 'https://www.ebay.com/itm/264934011608?ViewItem=&item=264934011608'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'html')
print("hello")
print(soup)
print(soup.text)


# 标题：根据规则发现
titles = soup.select('div > div > div > div > div.listing_info > div.listing_title > a')

print(titles)
# 图片的规则是宽度为180的打印出来
images = soup.select('img[width="180"]')

# 获取它的分类
cates = soup.select('#taplc_attraction_coverpage_attraction_0 > div > div:nth-child(1) > div > div > div.shelf_item_container > div > div.poi > div > div:nth-child(4)')
# print(titles,images,cates,sep='\n')

# 把获取到的内容放进一个字典中方便做查询
for title, image, cate in zip(titles,images,cates):
    data = {
        'title':title.get_text(),
        'image':image.get('src'),
        'cate':list(cate.stripped_strings)
    }
    print(data)

