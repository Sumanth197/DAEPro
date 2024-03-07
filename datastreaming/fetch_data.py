import requests

API_KEY = "P822ATQZ31ZZ5AT0"
COMPANY = "IBM"
TIME_INT = "60min"
FUNC = "TIME_SERIES_INTRADAY"
SIZE = "compact"


url = f'https://www.alphavantage.co/query?function={FUNC}&symbol={COMPANY}&interval={TIME_INT}&apikey={API_KEY}&outputsize={SIZE}&extended_hours=false'
r = requests.get(url)
data = r.json()