# ExchangeRate
A free RMB exchange rate API written in Flask

## iOS App
[![Download on App Store](https://upload.wikimedia.org/wikipedia/commons/5/51/Download_on_the_App_Store_Badge_US-UK_RGB_blk.svg)](https://apps.apple.com/cn/app/dollar-currency-widget/id6450919353)


## User Guide
### Call API
```
# Get the exchange rate of RMB and USD
[GET] http://127.0.0.1:6666/?currency=USD

# Get the exchange rate of RMB and EUR
[GET] http://127.0.0.1:6666/?currency=EUR

......
```

### Response
```json
// 20231121013418

{
  "data": [
    {
      "bocConversionRate": "714.06",
      "cashBuyingRate": "712.9",
      "cashSellingRate": "715.9",
      "currencyName": "USD",
      "foreignExchangeBuyingRate": "713.06",
      "foreignExchangeSellingRate": "715.9",
      "releaseTime": "2023.11.21 14:20:51"
    },
    {
      "bocConversionRate": "716.12",
      "cashBuyingRate": "718.74",
      "cashSellingRate": "721.76",
      "currencyName": "USD",
      "foreignExchangeBuyingRate": "718.9",
      "foreignExchangeSellingRate": "721.76",
      "releaseTime": "2023.11.20 09:36:04"
    },
    {
      "bocConversionRate": "717.28",
      "cashBuyingRate": "720.28",
      "cashSellingRate": "723.32",
      "currencyName": "USD",
      "foreignExchangeBuyingRate": "720.44",
      "foreignExchangeSellingRate": "723.32",
      "releaseTime": "2023.11.19 10:30:00"
    },
    {
      "bocConversionRate": "717.28",
      "cashBuyingRate": "719.98",
      "cashSellingRate": "723.02",
      "currencyName": "USD",
      "foreignExchangeBuyingRate": "720.14",
      "foreignExchangeSellingRate": "723.02",
      "releaseTime": "2023.11.18 01:41:04"
    },
    {
      "bocConversionRate": "717.24",
      "cashBuyingRate": "722.98",
      "cashSellingRate": "726.02",
      "currencyName": "USD",
      "foreignExchangeBuyingRate": "723.14",
      "foreignExchangeSellingRate": "726.02",
      "releaseTime": "2023.11.17 00:01:21"
    },
    {
      "bocConversionRate": "717.52",
      "cashBuyingRate": "723.31",
      "cashSellingRate": "726.35",
      "currencyName": "USD",
      "foreignExchangeBuyingRate": "723.47",
      "foreignExchangeSellingRate": "726.35",
      "releaseTime": "2023.11.16 00:59:46"
    },
    {
      "bocConversionRate": "717.68",
      "cashBuyingRate": "724.03",
      "cashSellingRate": "727.07",
      "currencyName": "USD",
      "foreignExchangeBuyingRate": "724.19",
      "foreignExchangeSellingRate": "727.07",
      "releaseTime": "2023.11.15 00:37:25"
    }
  ]
}
```

## Cache
Since the bank exchange rate changes are not real-time, the API of this project does caching and the default is 300 seconds.

For example, the first time to get the dollar exchange rate, the API of this project needs to get the data from the third-party API, which may take 300ms, and the second time to get the dollar exchange rate within 300 seconds only takes 2-3ms.

### Adjust the cache time
```python
@cache.cached(timeout=300, key_prefix=cache_key)
```
## Deploy
### Install required dependencies
```bash
pip install -r requirements.txt
```
### Run
```bash
gunicorn cmb:app
# or
gunicorn card-org:app
# or
gunicorn rate:app
```

## Data Source
[Bank of China](https://www.boc.cn/en/)

## Author
**ExchangeRate** © [Vincent Young](https://github.com/missuo), Released under the [MIT](./LICENSE) License.<br>
