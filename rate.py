#!/usr/bin/env python3
'''
Author: Vincent Young, Sark Xing
Date: 2023-07-05 22:18:19
LastEditors: Vincent Young
LastEditTime: 2023-07-06 18:43:39
FilePath: /ExchangeRate/rate.py
Telegram: https://t.me/missuo

Copyright © 2023 by Vincent, All Rights Reserved. 
'''
import httpx
from lxml import etree
from flask_cors import CORS
from flask import Flask, jsonify, request, abort
from flask_caching import Cache
from datetime import datetime, timedelta
import requests

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
CORS(app)

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

def processText(text):
    return text.replace("\n","").replace("\r","").strip()

def cache_key():
    return request.url

def getBoCPastWeekDates():
    dates = []
    today = datetime.today().date()
    for i in range(7):
        date = today - timedelta(days=i)
        dates.append(date.strftime("%Y-%m-%d"))
    return dates

def getVISAPastWeekDates():
    dates = []
    today = datetime.today().date()
    for i in range(7):
        date = today - timedelta(days=i)
        dates.append(date.strftime("%m/%d/%Y"))
    return dates

def getUnionPastWeekDates():
    dates = []
    today = datetime.today().date()
    for i in range(7):
        date = today - timedelta(days=i)
        dates.append(date.strftime("%Y%m%d"))
    return dates

def get_boc_rate(currencyName):
    url = "https://srh.bankofchina.com/search/whpj/search_cn.jsp"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",

    }
    processedDataArray =[]

    for i in range(7):
        date = getBoCPastWeekDates()[i]
        if i == 0:
            page = 1
        else:
            page = 20
        body = {
            "erectDate": date,
            "nothing": date,
            "pjname": currencyName,
            "page": page,
            "head": "head_620.js",
            "bottom": "bottom_591.js",
        }
        r = httpx.post(url=url, data=body, headers=headers).text
        tree = etree.HTML(r)
        data = tree.xpath('//table/tr[2]/td')
        processedData = [processText(item.text) for item in data]
        processedData[0] = currencyDictReversed[processedData[0]]
        processedDataArray.append(processedData)
    return processedDataArray

def get_visa_rate(currencyName):
    headers = {'Referer': 'https://usa.visa.com/'}
    processedDataArray = []

    for visa_date in getVISAPastWeekDates():
        url = f"https://usa.visa.com/cmsapi/fx/rates?amount=1&fee=2&utcConvertedDate={visa_date}&exchangedate={visa_date}&fromCurr=CNY&toCurr={currencyName}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            rate = data["originalValues"]["fxRateVisa"]
            timestamp = data["originalValues"]["lastUpdatedVisaRate"]
            processedDataArray.append({'currencyName': currencyName, 'rate': rate, 'releaseTime': visa_date})
        else:
            print(f"Failed to get rate for {visa_date}")

    return processedDataArray


def get_union_rate(currencyName):
    processedDataArray = []

    for union_date in getUnionPastWeekDates():
        url = f"https://www.unionpayintl.com/upload/jfimg/{union_date}.json"
        response = requests.get(url)
        if response.status_code == 200:
            exchangeRateJson = response.json().get('exchangeRateJson', [])
            rateObj = next((rate for rate in exchangeRateJson if rate['baseCur'] == "CNY" and rate['transCur'] == currencyName), None)
            rate = rateObj.get('rateData', 'No rate found for provided currencies') if rateObj else 'No rate found for provided currencies'
            processedDataArray.append({'currencyName': currencyName, 'rate': rate, 'releaseTime': union_date})
        else:
            print(f"Failed to get rate for {union_date}")

    return processedDataArray

def cache_key():
    return request.url

@app.route('/')
@cache.cached(timeout=300, key_prefix=cache_key)
def rate():
    currencyName = request.args.get('currency')
    if not currencyName or len(currencyName) != 3:
        abort(400)
    # boc_data = get_boc_rate(currencyName)
    visa_data = get_visa_rate(currencyName)
    union_data = get_union_rate(currencyName)
    return jsonify({"union_data": union_data},{"visa_data": visa_data})
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=6666)