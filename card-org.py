#!/usr/bin/env python3
'''
Author: Vincent Young
Date: 2023-07-15 02:37:23
LastEditors: Vincent Young
LastEditTime: 2023-07-15 03:35:32
FilePath: /ExchangeRate/card-org.py
Telegram: https://t.me/missuo

Copyright © 2023 by Vincent, All Rights Reserved. 
'''
import httpx
from datetime import datetime, timedelta
from flask_cors import CORS
from flask import Flask, jsonify, request, abort
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
CORS(app)

supportedCurrenciesUnion = ['AUD', 'CAD', 'CNY', 'EUR', 'GBP', 'HKD', 'HUF', 'JPY', 'MOP', 'NZD', 'SGD', 'THB', 'USD', 'VND']
supportedCurrenciesVisa = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'MXN', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CYP', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GQE', 'GTQ', 'GWP', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MRU', 'MTL', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SIT', 'SKK', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']

def getUnionRate(currencyName, unionDate):
    url = f"https://www.unionpayintl.com/upload/jfimg/{unionDate}.json"
    response = httpx.get(url)
    if response.status_code == 200:
        exchangeRateJson = response.json().get('exchangeRateJson', [])
        rateObj = next((rate for rate in exchangeRateJson if rate['baseCur'] == "CNY" and rate['transCur'] == currencyName), None)
        rate = rateObj.get('rateData', 'No rate found for provided currencies') if rateObj else 'No rate found for provided currencies'
        return rate
    
def getVisaRate(currencyName, visaDate):
    headers = {'Referer': 'https://usa.visa.com/'}
    url = f"https://usa.visa.com/cmsapi/fx/rates?amount=1&fee=2&utcConvertedDate={visaDate}&exchangedate={visaDate}&fromCurr=CNY&toCurr={currencyName}"
    response = httpx.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        rate = data["originalValues"]["fxRateVisa"]
        return rate

def cache_key():
    return request.url

@app.route('/')
@cache.cached(timeout=300, key_prefix=cache_key)
def getRate():
    currencyName = request.args.get('currency')
    respList = []
    resp = {
        "data": respList
    }
    today = datetime.today().date()
    for i in range(7):
        date = today - timedelta(days=i)
        formattedDate = date.strftime("%Y-%m-%d")
        if date.weekday() == 5: # Saturday
            unionDate = today - timedelta(days=1)
            unionDate = unionDate.strftime("%Y%m%d")
        elif date.weekday() == 6: # Sunday
            unionDate = today - timedelta(days=2)
            unionDate = unionDate.strftime("%Y%m%d")
        else:
            unionDate = date.strftime("%Y%m%d")
        visaDate = date.strftime("%m/%d/%Y")
        if currencyName in supportedCurrenciesUnion:
            unionRate = getUnionRate(currencyName, unionDate)
        else:
            unionRate = "Unsupported Currency"
        if currencyName in supportedCurrenciesVisa:
            visaRate = getVisaRate(currencyName, visaDate)
        else:
            visaRate = "Unsupported Currency"
        respDict = {
            "visaRate": visaRate,
            "unionRate": unionRate,
            "releaseDate": formattedDate
        }
        respList.append(respDict)
    return jsonify(resp)
    
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=6666)