#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:30:21 2020
@author: yu-hsuantseng
rtb_2020
"""


import os
import sys
import csv
import html
import re
import io
import json, urllib.request

from urllib import request, parse
from time import time, strftime, localtime, sleep
from ftplib import FTP

shop_id = None
shop_name = None

# Exclude keywords
re_exclude = re.compile("內衣|內褲|三角褲|陰道|性感|比基尼|角色扮演|丁字褲|開檔|夏季|褲襪|cosplay|絲襪|爆乳|開襠|按摩棒|子宮|翹臀|乳頭|胸貼|兔女郎|3P|APHRODISIA|AV女優|AV棒|A漫|A片|FLESHLIGHT Girls|FLESHLIGHT-SEX IN A CAN|FUN FACTORY|Gay片|GENMU|glock|glock17|Glove 極愛|G點|G點棒|G點調情套|HUANMEI|H漫|PINK PUSSY|PIPEDREAM|Pleasure Shell|Toughage|ViVi情趣精品|YouCups|乳交|乳環|乳首|兔棒|冰火三重天|冰火四重天|冰火五重天|冰火六重天|冰火七重天|冰火八重天|冰火九重天|冰火棒|刺激器|前列線腺激發器|前列腺G點|前列腺按摩|加藤鷹|勃起加強環|包皮阻復環|包皮阻複環|包皮環|包莖|北美硬漢|印度神油|口交|叫床|名器|壞男愛世界|壯陽|大屌|女陰|寫真集|屌環|巍廷山丘|巨屌|後庭|後庭大炸彈|後庭拉珠|後庭棒|德國OVO|快樂海螺|性愛|性愛大全|性愛娃娃|性愛玩具|性愛百貨|性愛與親密關係的指導|情慾|情色小說|情趣商品|情趣娃娃|情趣提升凝露|情趣玩具|情趣環|情趣用品|愛情夢工房|愛熙449|成人小說|成人書籍|成人玩具|成人用品|成人頻道|房事|手指鍛煉器|手指震動器|手淫|打手槍|拉珠|持久液|持久膏|指險套|撸杯|撸管|擬真娃娃|日本WINS|日本無碼|格雷50道陰影|格雷的50道陰影|格雷的五十道陰影|樂趣套|活力提升精華露|潤滑液|潮吹|激凸環|激情同志|激情套|激情震動器|炫煬堂|猛男DIY|猛男加強套|男根倒模|真人娃娃|真人矽膠|睪丸環|碧荷柏|神之手訓練器|私密生活|粗莖|糖衣丸|缸交|美穴|老二|老二棒|耐力噴霧|肛交|肛塞|肛門塞|自愛|自愛器|自慰|自慰器|自慰套|自慰杯|自衛器|舌誘|虐乳|虐陰|蜜穴|調情刷|調情棒|貞操帶|貞操裝置|超人氣彈丸|跳蛋|跳蛋棒|迴轉旋風機|迷你微蛋|通姦|逼真倒模|金屬屌|防水跳蛋|阻尿器|限制級|陰交|陰唇|陰器|陰核|陰穴|陰莖|陽具環|雙穴|電動旋轉棒|電動環|震動兔子|震動海豚|震動環|震動馬槌|震球|震蛋|飛機杯|香港AVIS|香港Venus|體位杯|高潮|高潮神器|龜頭|龜頭訓練器|電子菸|電子煙|情趣|舔陰器|震動棒|男用自慰|肛門|調情工具|老二套環|Fleshlight|變裝義乳|起火式|煤氣癌|成漫|激凸|淫亂|瓦斯槍|手槍|模型槍|陽具|KUU-HIP|假屌|SINMIS|連身衣|平口褲|塑身背心|蝴蝶結罩杯|醫用口罩|謎樣愛子和服|好硬杯|包臀迷你裙|青春無敵！清純學生服|魅惑紫色系緹花蕾絲馬甲四件組|酒精|口罩|紫外線殺菌|乾洗手|除菌液|H1N1|紫外線消毒燈|次氯酸|消毒液|震棒按摩器|蘇菲雅魅惑衣著|青春無敵！香肩美背女學生服|和服\(愛在今夜\)T9154\-桃\-F|成人人體透視|得意優質抽取式衛生紙|草莓大福6入組|KIRKLAND 抽取式衛生紙|幼萌系蘿莉娃娃|幼萌系平胸娃娃|全矽膠一體成型半身娃娃|全矽膠骨架爆乳半身娃娃|真人版 實體娃娃\/小優|全實體矽膠不銹鋼變形骨骼娃娃|迷情勾魂|三角無痕褲|Mimi Holliday Hide|iMake曖昧客|Ann Summers|River Island|天使霓裳|細網透明細帶|壓線肩帶可調小可愛|羅紋細肩半截背心|G線短褲|Ann Summers Love Me True lace thong in emerald-Green|MEIERQ\+俐落極簡素面泳褲;\(!\)|MEIERQ+素面無痕三角泳褲;\(!\)|小米|Redmi|紅米|米家|Yeelight|AMAZFIT|小衛質品|貝醫生巴氏|米兔|知吾", re.IGNORECASE)
# 1. 蝦皮商城 83
# 2. friday 9
# 3. 東森 50
# 4. 森森 90
# 5. udn買東西 20
# 6. yahoo奇摩超級商城 2
# 7. 台灣樂天 18

from_shop_id = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] is not None else 0
skip_tag = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] is not None else 0

# shops = [9,50,90,20,2,18]
shops = [9,50,90,20,18]
cat_parents = [1,47,118,273,443,488,532,564,625,742,824,877,902]
categories = {
    "273": "手機電玩",
    "118": "鞋包配飾",
    "443": "電腦週邊",
    "47": "流行服飾",
    "488": "家電影音",
    "742": "運動戶外",
    "625": "居家生活",
    "902": "圖書文具",
    "532": "婦幼童裝",
    "564": "美食生鮮",
    "1": "美妝保養",
    "824": "旅遊餐券",
    "877": "醫療保健"
}

print('Prep shops...')
url = "https://storage.googleapis.com/specialoffer/rules.json"
data = urllib.request.urlopen(url).read()
shopsDictOld = json.loads(data)

def find_shop_old(shop_id):
    obj = None
    for key in shopsDictOld:
        item = shopsDictOld[key]
        if int(item['shopid']) == shop_id:
            # obj = item
            parts = key.split('.')
            if len(parts) == 2:
                obj = parts[0]
            elif len(parts) == 3:
                obj = parts[1]
                if obj == 'com' or obj == '91app':
                    obj = parts[0]
            elif len(parts) == 4:
                obj = parts[1]

            if obj is not None:
                break
    return str(obj).replace('-', '', 99) if obj is not None else None

def queryProduct(query, shopId, page):
    query = query.strip().split(u'\b')
    query = u''.join(query)
    q = {
        "query": """query {{ search(types:[NORMAL], queryString:\"{0}\", page:{1}, pageSize:100, source: EXTERNAL, orderBy:MOST_RELEVANT, filter: {{ shops:[{2}] }}) {{contents {{...on Product {{ id shopProductId name description imageUrl outlinkUrl productPageUrl price specialPrice merchant {{ name shopId description point {{ amount }} }}  }}  }}  pageInfo {{ totalCount totalPages }}  }}}}""".format(
            str(query).replace('"', '\\"'),
            int(page),
            int(shopId)
        )
    }
    # ts1 = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
    # print('Query-pre:', ts1)
    q = json.dumps(q)
    q = str(q)
    # print(q)
    q = q.encode('utf-8')

    try:
        req =  request.Request("https://buy.line.me/api/graphql", data=q)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Origin', 'https://buy.line.me')
        data = request.urlopen(req).read()
        info = json.loads(data)
        # ts2 = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
        # print('Query-post:', ts2)
        sleep(0.5)
        return info
    except:
        print('Unable to process:', sys.exc_info()[0])
        print('Query:', q)


    return None

def loop(shop_id, shop_name):
    print('Processing shop...', shop_id, shop_name)

    csv_filename = """rtb_productfeed_{0}_pre.csv""".format(shop_id)
    rtb_file = open(csv_filename, 'w', newline='', encoding="UTF-8")
    fieldnames_rtb = ['id', 'categoryid', 'category', 'categoryid1', 'category1', 'title', 'highPrice', 'lowPrice', 'link', 'image_link','outlinkUrl']
    writer_rtb = csv.DictWriter(rtb_file, fieldnames=fieldnames_rtb, delimiter='\t')
    writer_rtb.writeheader()

    products = {}

    for q in range(0, len(tags)):
        if q < skip_tag:
            continue

        # if q > 2:
        #     break

        tag = tags[q][0]

        cat_level = tags[q][1]
        cat_levels = cat_level.split(",")
        cat_id = int(cat_levels[0])
        cat_name = categories[str(cat_id)]

        print('Processing tag query...', tag, q, len(products))
        for page in range(1, 22):
            # if page > 2:
            #     break
            print('Page:', page, tag, q, shop_name, len(products))
            res = queryProduct(tag, shop_id, page)
            if res is None or res['data'] is None or res['data']['search'] is None or res['data']['search']['contents'] is None:
                print('No more...', page)
                break

            contents = res['data']['search']['contents']
            if not len(contents):
                print('No more...', page)
                break

            for i in range(0, len(contents)):
                item = contents[i]
                # product_id = "{0}/{1}".format(shop_id, item['shopProductId'])
                product_id = item['id']

                if product_id in products:
                    # print('Already exists', product_id)
                    continue

                if re_exclude.search(item['name'], re.IGNORECASE) is not None or re_exclude.search(item['description'], re.IGNORECASE) is not None or re_exclude.search(item['name']) is not None or re_exclude.search(item['description']) is not None:
                    # print('Skipping...', item['id'], item['name'])
                    continue

                # print('shopProductId', i, item['shopProductId'], item['name'])

                item['cat_id'] = cat_id
                item['cat_name'] = cat_name
                products[product_id] = True

                write_cat_id = item['cat_id'] if item['cat_id'] else '0'
                write_cat_name = item['cat_name'].strip() if item['cat_name'].strip() else 'OTHER'

                if item['specialPrice'] and int(item['specialPrice']) < int(item['price']):
                    discount = ''.join([str(int(item['specialPrice']))])
                else:
                    discount = ''

                item['name'] = re.sub('[!！]', '', item['name'])
                item['name'] = re.sub('^=', '', item['name'])

                writer_rtb.writerow({
                    'id': "{0}-{1}".format(shop_id, item['shopProductId'].strip()),
                    'categoryid': write_cat_id,
                    'category': write_cat_name,
                    'categoryid1': write_cat_id,
                    'category1': write_cat_name,
                    'title': html.unescape(item['name'].strip()[0:150]),
                    'highPrice': ''.join([str(int(item['price']))]),
                    'lowPrice': discount,
                    'link': item['productPageUrl'].strip(),
                    'image_link': item['imageUrl'].strip(),
                    'outlinkUrl':item['outlinkUrl'].strip(),
                })
        #         break
        #     break
        # break

def proc(shop_id, shop_name):
    # Exclude product url
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTS3WLw7m6qeNiFjPXo9d1YVyzPPdjg4Foac2DULAP0pTOpXEMiyallgzekU9zSxwzkSLdz0lRRsxkq/pub?gid=1714156370&single=true&output=tsv"
    exclude_product_response = urllib.request.urlopen(url)

    exclude_csvfile = csv.reader(io.StringIO(exclude_product_response.read().decode('utf-8')), delimiter="\t")
    exclude_csvfile = list(exclude_csvfile)
    exclude_csvfile = exclude_csvfile[1:]

    exclude_list = []

    for e in range(1, len(exclude_csvfile)):
        exclude_list.append(exclude_csvfile[e][0])

    exclude_list_set = set(exclude_list)
    exclude_list = list(exclude_list_set)

    # Make sure no duplicate
    input_file = """rtb_productfeed_{0}_pre.csv""".format(shop_id)
    input_rtb_file = open(input_file)
    reader_rtb = csv.reader(input_rtb_file, delimiter='\t')

    csv_filename = """rtb_productfeed_{0}.csv""".format(shop_id)
    rtb_file = open(csv_filename, 'w', newline='', encoding="UTF-8")
    fieldnames_rtb = ['id', 'categoryid', 'category', 'categoryid1', 'category1', 'title', 'highPrice', 'lowPrice', 'link', 'image_link','outlinkUrl']
    writer_rtb = csv.DictWriter(rtb_file, fieldnames=fieldnames_rtb, delimiter='\t')
    writer_rtb.writeheader()

    products = {}
    line_count = 0
    # [
    #     0 'id',
    #     1 'categoryid',
    #     2 'category',
    #     3 'categoryid1',
    #     4 'category1',
    #     5 'title',
    #     6 'highPrice',
    #     7 'lowPrice',
    #     8 'link',
    #     9 'image_link',
    #     10 'outlinkUrl'
    # ]
    for item in reader_rtb:
        if line_count == 0:
            print(f'Column names are {", ".join(item)}')
            line_count += 1
        else:
            line_count += 1

            if re_exclude.search(str(item[5]), re.IGNORECASE) is not None or re_exclude.search(str(item[5])) is not None:
                print('Skipping...', item[0], item[5])
                continue

            product_id = item[0]

            if item[8].strip() in exclude_list:
                continue

            if product_id in products:
                continue

            products[product_id] = True

            writer_rtb.writerow({
                'id': product_id,
                'categoryid': item[1],
                'category': item[2],
                'categoryid1': item[3],
                'category1': item[4],
                'title': item[5],
                'highPrice': item[6],
                'lowPrice': item[7],
                'link': item[8],
                'image_link': item[9],
                'outlinkUrl':item[10]+str("&redir=true")
            })

    # FTP
    ftp = FTP(host='feedupload.rtbhouse.net', user='tw_line', passwd='shosaichee7suizaireigae7gi')
    ftp_send_file = open(csv_filename, 'rb')
    ftp.storbinary("STOR %s"%csv_filename, ftp_send_file)
    ftp_send_file.close()
    ftp.quit()

    # LINE Notify
    r = request.Request("""https://asia-east2-line-product-widget.cloudfunctions.net/line_notify_message/line_notify_message/line_notify_message?token=NsTN8pUzrlOz65qzyuv8qWAt8FymlFPTRGiRiovbJNP&message={0}""".format(
        urllib.parse.quote("""
Shop: {1}({0})
Count: {2}
{3}""".format(
            str(shop_id),
            shop_name,
            str(len(products)),
            csv_filename
        ).encode("utf-8"))
    ))
    request.urlopen(r)

tags = []
with open('./tags.tsv', newline = '') as tsv:
    tags_reader = csv.reader(tsv, delimiter='\t')
    for tag in tags_reader:
        tags.append(tag)

while True:
    start_flag = False if from_shop_id > 0 else True
    for idx in range(0, len(shops)):
        shop_id = shops[idx]

        if from_shop_id == 0 or int(shop_id) == from_shop_id:
            start_flag = True

        if start_flag == True:
            shop_name = find_shop_old(shop_id)

            if shop_name is not None:
                loop(shop_id, shop_name)
                skip_tag = 0
                proc(shop_id, shop_name)

print('Done')

