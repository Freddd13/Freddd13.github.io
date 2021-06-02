import requests
import json
import csv
import codecs
import time
import os


TITLE = 0
ID = 3
COVER = 4
OTHERS = 9

wantWatch_ls = []
watching_ls = []
watched_ls = []

def chooseNewFile():
    file_ls = os.listdir('.')
    for file in file_ls:
        if "想看" in file:
            wantWatch_ls.append(file)
        elif "在看" in file:
            watching_ls.append(file)
        elif "看过" in file:
            watched_ls.append(file) 

    wantWatch_csv = max([[int(os.path.getctime(file)), file] for file in wantWatch_ls])[1]
    watching_csv = max([[int(os.path.getctime(file)), file] for file in watching_ls])[1]
    watched_csv = max([[int(os.path.getctime(file)), file] for file in watched_ls])[1]

    print('newest data:')
    print(wantWatch_csv)
    print(watching_csv)
    print(watched_csv)

    return wantWatch_csv, watching_csv, watched_csv

def removeOldFile(wantWatch_csv, watching_csv, watched_csv):
    # remove old
    wantWatch_ls.remove(wantWatch_csv)
    watching_ls.remove(watching_csv)
    watched_ls.remove(watched_csv)
    for tmp_list in [wantWatch_ls, watching_ls, watched_ls]:
        for file in tmp_list:
            os.remove(file)
            print('delete ', file)


def constructType(content):
    wantWatch_existed, watching_existed, watched_existed =[], [], []
    watchtype = {
        "wantWatch":{
            "csv_name": wantWatch_csv,
            "exist_list": wantWatch_existed
        },
        "watching":{
            "csv_name": watching_csv,
            "exist_list": watching_existed
        },
        "watched":{
            "csv_name": watched_csv,
            "exist_list": watched_existed
        },
    }
    constructExist(watchtype, content)
    return watchtype

def constructExist(watchtype, content):
    # delete
    for tmpkey in content.keys():
        for each in content[tmpkey]:
            watchtype[tmpkey]['exist_list'].append(each['title'])
            print('append ', each['title'])
    return watchtype


def deal(watchtype, content):
    # deal
    for key in watchtype.keys():
        with codecs.open(watchtype[key]["csv_name"], 'rb', 'utf-8', errors='ignore') as csvfile:
            reader = csv.reader(csvfile, dialect='excel')
            # 用csv.writer()函数创建一个writer对象。
            rows= [row for row in reader]
            rows.pop(0)

        for test_row in rows:
            title = test_row[TITLE]
            
            if title in watchtype[key]["exist_list"]:
                print(title + 'existed')
                continue

            cover = test_row[COVER]
            id = test_row[ID].split('/')[-1]
            total_count = test_row[OTHERS].split('话')[0] + '话' if len(test_row[OTHERS].split('话')[0]) > 1 else '?'
            url = "https://cdn.jsdelivr.net/gh/czy0729/Bangumi-Subject@master/data/" + str(int(id)//100) + "/" + str(id) + ".json"

            # request cdn
            r = requests.get(url)
            # print(r.text)
            if 'Package size' not in r.text:
                try:
                    r = r.json()
                except:
                    print(title,' err')
                    continue
                collection = r['collection']
                follow = 0
                for ckey in collection:
                    follow += collection[ckey]
                follow = 'Ban ' + str(follow)

                danmaku = "Bangumi"
                view = "Bangumi"
                coin = "Bangumi"
                score = 'Ban ' + str(r['rating']['score']) if 'rating' in r else '?'
                des = r['summary'].replace('\r\n', '').replace('　　','') if 'summary' in r else '?'
                if len(des) > 145:
                    des = des[:145] + '......'

                ej = {} 
                ej['title'] = title
                ej['type'] = "番剧"
                ej['area'] = "日本"
                ej['cover'] = cover
                ej['totalCount'] = total_count
                ej['id'] = id
                ej['follow'] = follow
                ej['view'] = view
                ej['danmaku'] = danmaku
                ej['coin'] = coin
                ej['score'] = score
                ej['des'] = des

            else:
                ej = {} 
                ej['title'] = title
                ej['type'] = "番剧"
                ej['area'] = "日本"
                ej['cover'] = '?'
                ej['totalCount'] = total_count
                ej['id'] = id
                ej['follow'] = '?'
                ej['view'] = '?'
                ej['danmaku'] = '?'
                ej['coin'] = '?'
                ej['score'] = '?'
                ej['des'] = '?'
            
            tmp[key].append(ej)
    return tmp


def writeJson(tmp):
    with open('bangumis.json', 'w', encoding='utf8') as f:
        json.dump(tmp, f, ensure_ascii=False)


if __name__ == "__main__":
    wantWatch_csv, watching_csv, watched_csv = chooseNewFile()
    removeOldFile(wantWatch_csv, watching_csv, watched_csv)
    with open(r'.\bangumis.json', 'r', encoding='utf8') as f:
        tmp = json.load(f)
    watchtype = constructType(tmp)
    tmp = deal(watchtype, tmp)
    writeJson(tmp)

    
