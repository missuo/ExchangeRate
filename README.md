# ExchangeRate
A free RMB exchange rate API written in Flask

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
    "bocConversionPrice": "785.01",
    "cashBuyPrice": "761.5",
    "cashSellPrice": "794.27",
    "currencyBuyPrice": "785.92",
    "currencyName": "EUR",
    "currencySellPrice": "791.72",
    "releaseTime": "2023.07.05 23:22:27"
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
