#!/usr/bin/env python3
'''
Author: Vincent Young
Date: 2023-07-15 02:37:23
LastEditors: Vincent Young
LastEditTime: 2023-07-17 03:29:05
FilePath: /ExchangeRate/card-org.py
Telegram: https://t.me/missuo

Copyright © 2023 by Vincent, All Rights Reserved. 
'''
import httpx
from datetime import datetime, timedelta
from flask_cors import CORS
from flask import Flask, jsonify, request, abort
from flask_caching import Cache
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
CORS(app)

def clearCache():
    with app.app_context():
        cache.clear()
        print(f'Cache cleared at {datetime.now()}')

scheduler = BackgroundScheduler()
scheduler.add_job(func=clearCache, trigger="cron", hour=0)
scheduler.start()

supportedCurrenciesUnion = ['AUD', 'CAD', 'CNY', 'EUR', 'GBP', 'HKD', 'HUF', 'JPY', 'MOP', 'NZD', 'SGD', 'THB', 'USD', 'VND']
supportedCurrenciesVisa = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'MXN', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CYP', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GQE', 'GTQ', 'GWP', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MRU', 'MTL', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SIT', 'SKK', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']
supportedCurrenciesMaster = ['AFN', 'ALL', 'DZD', 'AOA', 'ARS', 'AMD', 'AWG', 'AUD', 'AZN', 'BSD', 'BHD', 'BDT', 'BBD', 'BYN', 'BZD', 'BMD', 'BTN', 'BOB', 'BAM', 'BWP', 'BRL', 'BND', 'BGN', 'BIF', 'KHR', 'CAD', 'CVE', 'KYD', 'XOF', 'XAF', 'XPF', 'CLP', 'CNY', 'COP', 'KMF', 'CDF', 'CRC', 'CUP', 'CZK', 'DKK', 'DJF', 'DOP', 'XCD', 'EGP', 'SVC', 'ETB', 'EUR', 'FKP', 'FJD', 'GMD', 'GEL', 'GHS', 'GIP', 'GBP', 'GTQ', 'GNF', 'GYD', 'HTG', 'HNL', 'HKD', 'HUF', 'ISK', 'INR', 'IDR', 'IQD', 'ILS', 'JMD', 'JPY', 'JOD', 'KZT', 'KES', 'KWD', 'KGS', 'LAK', 'LBP', 'LSL', 'LRD', 'LYD', 'MOP', 'MKD', 'MGA', 'MWK', 'MYR', 'MVR', 'MRU', 'MUR', 'MXN', 'MDL', 'MNT', 'MAD', 'MZN', 'MMK', 'NAD', 'NPR', 'ANG', 'NZD', 'NIO', 'NGN', 'NOK', 'OMR', 'PKR', 'PAB', 'PGK', 'PYG', 'PEN', 'PHP', 'PLN', 'QAR', 'RON', 'RUB', 'RWF', 'SHP', 'WST', 'STN', 'SAR', 'RSD', 'SCR', 'SLE', 'SGD', 'SBD', 'SOS', 'ZAR', 'KRW', 'SSP', 'LKR', 'SDG', 'SRD', 'SZL', 'SEK', 'CHF', 'TWD', 'TJS', 'TZS', 'THB', 'TOP', 'TTD', 'TND', 'TRY', 'TMT', 'UGX', 'UAH', 'AED', 'USD', 'UYU', 'UZS', 'VUV', 'VES', 'VND', 'YER', 'ZMW', 'ZWL']

def getUnionRate(basecurrName, transcurrName, unionDate):
    url = f"https://www.unionpayintl.com/upload/jfimg/{unionDate}.json"
    response = httpx.get(url)
    if response.status_code == 200:
        exchangeRateJson = response.json().get('exchangeRateJson', [])
        rateObj = next((rate for rate in exchangeRateJson if rate['baseCur'] == basecurrName and rate['transCur'] == transcurrName), None)
        rate = rateObj.get('rateData', 'No rate found for provided currencies') if rateObj else 'No rate found for provided currencies'
        return rate
    
def getVisaRate(basecurrName, transcurrName, visaDate, bankFee):
    headers = {'Referer': 'https://usa.visa.com/'}
    url = f"https://usa.visa.com/cmsapi/fx/rates?amount=1&fee={bankFee}&utcConvertedDate={visaDate}&exchangedate={visaDate}&fromCurr={basecurrName}&toCurr={transcurrName}"
    response = httpx.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        rate = data["convertedAmount"]
        return float(rate)

def getMasterRate(basecurrName, transcurrName, masterDate, bankFee):
	url = f"https://www.mastercard.us/settlement/currencyrate/conversion-rate?fxDate={masterDate}&transCurr={transcurrName}&crdhldBillCurr={basecurrName}&bankFee={bankFee}&transAmt=1"
	headers = {
		"Referer": "https://www.mastercard.us/en-us/personal/get-support/convert-currency.html",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
	}
	response = httpx.get(url, headers=headers)
	if response.status_code == 200:
		data = response.json()
		rate = data['data']['conversionRate']
		return rate

def cache_key():
    return request.url

@app.route('/')
@cache.cached(timeout=86400, key_prefix=cache_key)
def getRate():
    transcurrName = request.args.get('currency')
    if transcurrName is None:
        transcurrName = 'USD'
    else:
        transcurrName = transcurrName.upper()
    basecurrName = request.args.get('base')
    if basecurrName is None:
        basecurrName = 'CNY'
    bankFee = request.args.get('bankFee')
    if bankFee is None:
        bankFee = 0
    message = []
    if transcurrName not in supportedCurrenciesUnion:
        message.append("UnionPay does not support this currency!")
    if transcurrName not in supportedCurrenciesVisa:
        message.append("Visa does not support this currency!")
    if transcurrName not in supportedCurrenciesMaster:
        message.append("Mastercard does not support this currency!")
    respList = []
    resp = {
        "message": message,
        "data": respList
    }
    # Offset date by 11 hours
    today = datetime.today() - timedelta(hours=11) 
    unionRate = None
    visaRate = None
    masterRate = None
    if transcurrName not in supportedCurrenciesUnion and transcurrName not in supportedCurrenciesVisa and transcurrName not in supportedCurrenciesMaster:
        respList = []
    else:
        message.append("ok!")
        for i in range(7):
            date = (today - timedelta(days=i))
            formattedDate = date.strftime("%Y-%m-%d")
            if date.weekday() == 5: # Saturday
                unionDate = (today - timedelta(days=1))
                unionDate = unionDate.strftime("%Y%m%d")
            elif date.weekday() == 6: # Sunday
                unionDate = (today - timedelta(days=2))
                unionDate = unionDate.strftime("%Y%m%d")
            else:
                unionDate = date.strftime("%Y%m%d")
            visaDate = date.strftime("%m/%d/%Y")
            if transcurrName in supportedCurrenciesUnion:
                unionRate = getUnionRate(basecurrName, transcurrName, unionDate)
            if transcurrName in supportedCurrenciesVisa:
                visaRate = getVisaRate(basecurrName, transcurrName, visaDate, bankFee)
            if transcurrName in supportedCurrenciesMaster:
                masterRate = getMasterRate(basecurrName, transcurrName, formattedDate, bankFee)
            respDict = {
                "visaRate": visaRate,
                "unionRate": unionRate,
                "masterRate": masterRate,
                "releaseDate": formattedDate
            }
            respList.append(respDict)
    return jsonify(resp)
    
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=6666)