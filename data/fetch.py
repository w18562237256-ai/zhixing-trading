import sys
import urllib.parse
import urllib.request

url = sys.argv[1]
parsed = urllib.parse.urlparse(url)
if parsed.scheme != 'https' or parsed.hostname not in {'push2his.eastmoney.com', 'pushguest.eastmoney.com', 'push2.eastmoney.com'}:
    raise ValueError('Only public Eastmoney quote endpoints are allowed')
request = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://quote.eastmoney.com/',
    'Accept': 'application/json,text/plain,*/*'
})
with urllib.request.urlopen(request, timeout=15) as response:
    sys.stdout.buffer.write(response.read(8 * 1024 * 1024))
