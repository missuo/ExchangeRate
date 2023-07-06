#!/usr/bin/env python3
'''
Author: Vincent Young
Date: 2023-07-06 21:38:29
LastEditors: Vincent Young
LastEditTime: 2023-07-06 22:52:15
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

currencyDictReversed = {
    "港币": "HKD",
    "澳大利亚元": "AUD",
    "美元": "USD",
    "欧元": "EUR",
    "加拿大元": "CAD",
    "英镑": "GBP",
    "日元": "JPY",
    "新加坡元": "SGD",
    "瑞士法郎": "CHF",
    "新西兰元": "NZD"
}

currencyDict = {
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
    for day in range(2, 31):
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
    hositoryRateData = getHistoryRateFromCMB(currencyDict.get(currencyName))
    if not currentRateData or not hositoryRateData:
        abort(404)
    
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
    
    for dayItem in hositoryRateData:
        dataDict = {
        "currencyName": "",
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