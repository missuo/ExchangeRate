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
{
    "data":[
        {
            "bocConversionRate":"91.86",
            "cashBuyingRate":"91.42",
            "cashSellingRate":"92.52",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.15",
            "foreignExchangeSellingRate":"92.52",
            "releaseTime":"2023.07.11 01:54:43"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.57",
            "cashSellingRate":"92.58",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.22",
            "foreignExchangeSellingRate":"92.58",
            "releaseTime":"2023.07.10 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.49",
            "cashSellingRate":"92.50",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.14",
            "foreignExchangeSellingRate":"92.50",
            "releaseTime":"2023.07.09 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.49",
            "cashSellingRate":"92.50",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.14",
            "foreignExchangeSellingRate":"92.50",
            "releaseTime":"2023.07.08 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.47",
            "cashSellingRate":"92.48",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.12",
            "foreignExchangeSellingRate":"92.48",
            "releaseTime":"2023.07.07 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.81",
            "cashSellingRate":"92.83",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.45",
            "foreignExchangeSellingRate":"92.83",
            "releaseTime":"2023.07.06 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.78",
            "cashSellingRate":"92.80",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.42",
            "foreignExchangeSellingRate":"92.80",
            "releaseTime":"2023.07.05 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.32",
            "cashSellingRate":"92.33",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.97",
            "foreignExchangeSellingRate":"92.33",
            "releaseTime":"2023.07.04 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.60",
            "cashSellingRate":"92.61",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.25",
            "foreignExchangeSellingRate":"92.61",
            "releaseTime":"2023.07.03 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.76",
            "cashSellingRate":"92.78",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.40",
            "foreignExchangeSellingRate":"92.78",
            "releaseTime":"2023.07.02 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.76",
            "cashSellingRate":"92.78",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.40",
            "foreignExchangeSellingRate":"92.78",
            "releaseTime":"2023.07.01 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.80",
            "cashSellingRate":"92.82",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.44",
            "foreignExchangeSellingRate":"92.82",
            "releaseTime":"2023.06.30 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.72",
            "cashSellingRate":"92.74",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.36",
            "foreignExchangeSellingRate":"92.74",
            "releaseTime":"2023.06.29 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.74",
            "cashSellingRate":"92.76",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.38",
            "foreignExchangeSellingRate":"92.76",
            "releaseTime":"2023.06.28 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.15",
            "cashSellingRate":"92.16",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.80",
            "foreignExchangeSellingRate":"92.16",
            "releaseTime":"2023.06.27 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.58",
            "cashSellingRate":"92.59",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"92.23",
            "foreignExchangeSellingRate":"92.59",
            "releaseTime":"2023.06.26 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.03",
            "cashSellingRate":"92.04",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.68",
            "foreignExchangeSellingRate":"92.04",
            "releaseTime":"2023.06.25 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.03",
            "cashSellingRate":"92.04",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.68",
            "foreignExchangeSellingRate":"92.04",
            "releaseTime":"2023.06.24 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"91.05",
            "cashSellingRate":"92.06",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.70",
            "foreignExchangeSellingRate":"92.06",
            "releaseTime":"2023.06.23 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.89",
            "cashSellingRate":"91.90",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.54",
            "foreignExchangeSellingRate":"91.90",
            "releaseTime":"2023.06.22 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.93",
            "cashSellingRate":"91.94",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.58",
            "foreignExchangeSellingRate":"91.94",
            "releaseTime":"2023.06.21 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.89",
            "cashSellingRate":"91.90",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.54",
            "foreignExchangeSellingRate":"91.90",
            "releaseTime":"2023.06.20 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.76",
            "cashSellingRate":"91.76",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.40",
            "foreignExchangeSellingRate":"91.76",
            "releaseTime":"2023.06.19 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.35",
            "cashSellingRate":"91.35",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"90.99",
            "foreignExchangeSellingRate":"91.35",
            "releaseTime":"2023.06.18 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.35",
            "cashSellingRate":"91.35",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"90.99",
            "foreignExchangeSellingRate":"91.35",
            "releaseTime":"2023.06.17 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.19",
            "cashSellingRate":"91.19",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"90.83",
            "foreignExchangeSellingRate":"91.19",
            "releaseTime":"2023.06.16 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.38",
            "cashSellingRate":"91.38",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.02",
            "foreignExchangeSellingRate":"91.38",
            "releaseTime":"2023.06.15 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.47",
            "cashSellingRate":"91.47",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.11",
            "foreignExchangeSellingRate":"91.47",
            "releaseTime":"2023.06.14 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.45",
            "cashSellingRate":"91.45",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.09",
            "foreignExchangeSellingRate":"91.45",
            "releaseTime":"2023.06.13 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.37",
            "cashSellingRate":"91.37",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"91.01",
            "foreignExchangeSellingRate":"91.37",
            "releaseTime":"2023.06.12 00:00:00"
        },
        {
            "bocConversionRate":"",
            "cashBuyingRate":"90.17",
            "cashSellingRate":"91.17",
            "currencyName":"HKD",
            "foreignExchangeBuyingRate":"90.81",
            "foreignExchangeSellingRate":"91.17",
            "releaseTime":"2023.06.11 00:00:00"
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

## Data Source
[Bank of China](https://www.boc.cn/en/)

## Author
**ExchangeRate** © [Vincent Young](https://github.com/missuo), Released under the [MIT](./LICENSE) License.<br>
