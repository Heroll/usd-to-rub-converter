import urllib.request
import json
webURL = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
link = 'https://www.cbr-xml-daily.ru/daily_json.js'
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
rate = json.loads(data.decode(encoding))['Valute']['USD']['Value']



def convert(amount, currency):
	result = amount * rate
	return_info = {'currency': currency, 'amount_in_dollars': amount , 'amount_in_rubles' : result}
	return json.dumps(return_info)





