# ExchangeRate
A free RMB exchange rate API written in Flask

## iOS App
[https://upload.wikimedia.org/wikipedia/commons/5/51/Download_on_the_App_Store_Badge_US-UK_RGB_blk.svg](https://apps.apple.com/cn/app/dollar-currency-widget/id6450919353)

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
  "data": {
    "bocConversionRate": "785.01",
    "cashBuyingRate": "760.86",
    "cashSellingRate": "793.59",
    "currencyName": "EUR",
    "foreignExchangeBuyingRate": "785.26",
    "foreignExchangeSellingRate": "791.05",
    "releaseTime": "2023.07.06 01:25:36"
  }
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
