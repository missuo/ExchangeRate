#!/usr/bin/env python3
'''
Author: Vincent Young
Date: 2023-07-06 21:38:29
LastEditors: Vincent Young
LastEditTime: 2023-07-11 02:07:14
FilePath: /ExchangeRate/cmb.py
Telegram: https://t.me/missuo

Copyright © 2023 by Vincent, All Rights Reserved. 
'''

import httpx
from lxml import etree
from flask_cors import CORS
from flask import Flask, jsonify, request, abort
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
CORS(app)

def processText(text):
    return text.replace("\n","").replace("\r","").strip()

def processDate(text):
    return text.replace("年",".").replace("月",".").replace("日"," 00:00:00")

currencyDictCMB = {
    "HKD": "港币",
    "AUD": "澳大利亚元",
    "USD": "美元",
    "EUR": "欧元",
    "CAD": "加拿大元",
    "GBP": "英镑",
    "JPY": "日元",
    "SGD": "新加坡元",
    "CHF": "瑞士法郎",
    "NZD": "新西兰元"
}

currencyDict = {
    'GBP': '英镑',
    'HKD': '港币',
    'USD': '美元',
    'CHF': '瑞士法郎',
    'DEM': '德国马克',
    'FRF': '法国法郎',
    'SGD': '新加坡元',
    'SEK': '瑞典克朗',
    'DKK': '丹麦克朗',
    'NOK': '挪威克朗',
    'JPY': '日元',
    'CAD': '加拿大元',
    'AUD': '澳大利亚元',
    'EUR': '欧元',
    'MOP': '澳门元',
    'PHP': '菲律宾比索',
    'THB': '泰国铢',
    'NZD': '新西兰元',
    'KRW': '韩元',
    'RUB': '卢布',
    'MYR': '林吉特',
    'TWD': '新台币',
    'ESP': '西班牙比塞塔',
    'ITL': '意大利里拉',
    'NLG': '荷兰盾',
    'BEF': '比利时法郎',
    'FIM': '芬兰马克',
    'INR': '印度卢比',
    'IDR': '印尼卢比',
    'BRL': '巴西里亚尔',
    'AED': '阿联酋迪拉姆',
    'ZAR': '南非兰特',
    'SAR': '沙特里亚尔',
    'TRY': '土耳其里拉'
}

currencyDictReversed = {
    '英镑': 'GBP',
    '港币': 'HKD',
    '美元': 'USD',
    '瑞士法郎': 'CHF',
    '德国马克': 'DEM',
    '法国法郎': 'FRF',
    '新加坡元': 'SGD',
    '瑞典克朗': 'SEK',
    '丹麦克朗': 'DKK',
    '挪威克朗': 'NOK',
    '日元': 'JPY',
    '加拿大元': 'CAD',
    '澳大利亚元': 'AUD',
    '欧元': 'EUR',
    '澳门元': 'MOP',
    '菲律宾比索': 'PHP',
    '泰国铢': 'THB',
    '新西兰元': 'NZD',
    '韩元': 'KRW',
    '卢布': 'RUB',
    '林吉特': 'MYR',
    '新台币': 'TWD',
    '西班牙比塞塔': 'ESP',
    '意大利里拉': 'ITL',
    '荷兰盾': 'NLG',
    '比利时法郎': 'BEF',
    '芬兰马克': 'FIM',
    '印度卢比': 'INR',
    '印尼卢比': 'IDR',
    '巴西里亚尔': 'BRL',
    '阿联酋迪拉姆': 'AED',
    '南非兰特': 'ZAR',
    '沙特里亚尔': 'SAR',
    '土耳其里拉': 'TRY'
}

def getHistoryRateFromCMB(currencyName):
    url = "http://fx.cmbchina.com/hq/History.aspx?nbr={}".format(currencyName)
    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    r = httpx.get(url=url, headers=headers).text
    tree = etree.HTML(r)
    dayArray = []
    monthArray = []
    for day in range(1, 31):
        dayArray = []
        for i in range(1, 6):
            data = tree.xpath('//table/tbody[2]/tr[{}]/td[{}]'.format(day, i))
            for item in data:
                dayArray.append(processDate(item.text))
        monthArray.append(dayArray)
    return monthArray

def getCurrentRate(currencyName):
    url = "https://srh.bankofchina.com/search/whpj/search_cn.jsp"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",

    }
    body = {
        "erectDate": "",
        "nothing": "",
        "pjname": currencyName
    }
    r = httpx.post(url=url, data=body, headers=headers).text
    tree = etree.HTML(r)
    data = tree.xpath('//table/tr[2]/td')
    processedData = [processText(i.text) for i in data]
    processedData[0] = currencyDictReversed[processedData[0]]
    return processedData

def cache_key():
    return request.url

@app.route('/')
@cache.cached(timeout=1000, key_prefix=cache_key)
def rate():
    currencyName = request.args.get('currency')
    if not currencyName or len(currencyName) != 3:
        abort(400)
    currentRateData = getCurrentRate(currencyDict.get(currencyName))
    rateArray = []
    respDict = {
        "data": rateArray
    }
    dataDict = {
        "currencyName": currentRateData[0],
        "foreignExchangeBuyingRate": currentRateData[1],
        "cashBuyingRate": currentRateData[2],
        "foreignExchangeSellingRate": currentRateData[3],
        "cashSellingRate": currentRateData[4],
        "bocConversionRate": currentRateData[5],
        "releaseTime": currentRateData[6],
    }
    rateArray.append(dataDict)
    if currencyName in currencyDictCMB:
        hositoryRateData = getHistoryRateFromCMB(currencyDict.get(currencyName))
        for dayItem in hositoryRateData:
            dataDict = {
                "currencyName": currencyName,
                "foreignExchangeBuyingRate": dayItem[1],
                "cashBuyingRate": dayItem[2],
                "foreignExchangeSellingRate": dayItem[3],
                "cashSellingRate": dayItem[4],
                "bocConversionRate": "",
                "releaseTime": dayItem[0],
            }
            rateArray.append(dataDict)   

    return jsonify(respDict)
    
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=6666)