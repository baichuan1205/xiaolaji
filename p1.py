import requests
from lxml import etree
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
url = "https://www.waihui321.com/"
response = requests.get(url, headers=headers)
html = response.text
# 将HTML字符串解析为ElementTree对象
tree = etree.HTML(html)

# 使用xpath抽取货币名称、代码和现汇买入价（除以100）
cur_names = tree.xpath('//table/tbody/tr/td[1]/a/text()')
curs = tree.xpath('//table/tbody/tr/td[2]/text()')
cur_to_rmb = []
rates = tree.xpath('//table/tbody/tr/td[3]/text()')
for rate in rates:
    if rate == '-':
        cur_to_rmb.append(None)  # 或者根据你的需求处理缺失值，这里暂时用None表示
    else:
        cur_to_rmb.append(round(float(rate) / 100, 4))

# 将抽取的数据组合成字典列表
data = [{'cur_name': cur_name.replace(' ', ''), 'cur': cur, 'cur_to_rmb': rate} for cur_name, cur, rate in
        zip(cur_names, curs, cur_to_rmb)]

print(data)