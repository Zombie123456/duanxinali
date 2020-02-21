import json
import time
from urllib import parse
import hashlib
import base64
import hmac
import requests
from uuid import uuid4


a_id = 'LTAIb5I3lIEeE8G9'
s_id = '9aEqviBE0CwMU5MOvF2ScIeWGltKoR'

params = {
	'AccessKeyId': a_id,
	'Timestamp': time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(time.time() - (60 * 60 * 8))),
	'Format': 'json',
	'SignatureMethod': 'HMAC-SHA1',
	'SignatureVersion': '1.0',
	'SignatureNonce': hashlib.md5(uuid4().__str__().encode()).hexdigest(),
	'Action': 'SendSms',
	'Version': '2017-05-25',
	'RegionId': 'cn-hangzhou',
	'PhoneNumbers': '************',
	'SignName': '乐理二手',
	'TemplateCode': 'SMS_163438002',
	'TemplateParam': json.dumps({'code': '564564'})
	}
sign_str = '&'.join([f'{key}={value}' for key, value in sorted(params.items())])

s = parse.quote(sign_str, safe='=&')
s = parse.quote(s)
s = 'GET&%2F&' + s
s1 = s_id + '&'
s = hmac.new(s1.encode(), s.encode(), hashlib.sha1).digest()
s = base64.b64encode(s).decode()
params['Signature'] = s

url_data = parse.urlencode(params)
url = f'http://dysmsapi.aliyuncs.com/?{url_data}'

res = requests.get(url)
print(res.text)
