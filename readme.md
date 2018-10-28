# Weather Forecast

This is a python program that has one purpose. Looking up weather for today, tomorrow and overmorrow. It does so by making a query to [yr.no](https://www.yr.no/?spr=eng) and handling the language conversion.

## Requirements

You will need the following to run the script

* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
* [requests](https://pypi.org/project/requests/)

## The config

In order for translations to work properly, you will want to head over to [Yandex Developer API](https://translate.yandex.com/developers), to get an API key. When you have the key, you want to rename [Example.Config.py](Example.Config.py) to `Config.py` and paste your API key in there.

## You're ready

You are now ready to look up weather forecasts for the coming days. Enjoy!