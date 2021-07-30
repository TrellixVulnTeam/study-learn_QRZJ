import requests
import json

if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    id_list = []  # 存储企业的id
    all_data_list = []
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for page in range(1, 3):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic["ID"])
    # 获取企业的详情页数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById?'

    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        #print(detail_json)
        all_data_list.append(detail_json)
    # 持久化存储
    fp = open('./alldata.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    fp.close()
    print('抓取成功')

import requests
import json

if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    id_list = []  # 存储企业的id
    all_data_list = []
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for page in range(1, 3):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic["ID"])
    # 获取企业的详情页数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById?'

    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        #print(detail_json)
        all_data_list.append(detail_json)
    # 持久化存储
    fp = open('./alldata.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    fp.close()
    print('抓取成功')