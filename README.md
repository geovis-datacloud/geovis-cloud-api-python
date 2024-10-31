### 使用方法

1 安装

```bash
pip install git+https://github.com/geovis-datacloud/geovis-cloud-api-python.git
```

2 DataCloudSign使用
```bash
from geovis_cloud_api_python import DataCloudSign
import uuid
from datetime import datetime

dataCloudSign = DataCloudSign('your secretId', 'your secretKey')

path = '/v1/cloudapi/application/publics'
method = 'GET'
body = None # body为空时，传None
queryString = 'key1=value1&key2=value2' # 无查询参数时，传空字符串
nonceStr = str(uuid.uuid4())
timestamp = str(round(datetime.now().timestamp() * 1000))
# 获取签名请求头 
headers = dataCloudSign.sign(path, method, body, queryString, nonceStr, timestamp)
# 请求接口
url = f'https://datacloud1.geovisearth.com{path}'
if (queryString):
    url = f'{url}?{queryString}'
result = dataCloudSign.request(url, method, headers, body)
```

3 CertificationSign使用
```bash
from geovis_cloud_api_python import CertificationSign
import uuid
from datetime import datetime

path = '/v1/cloudapi/certification/industry'
method = 'GET'
body = None # body为空时，传None
queryString = '' # 无查询参数时，传空字符串
url = f'https://api1-dev.geovisearth.com/daas/certification-dev{path}'
if (queryString):
    url = f'{url}?{queryString}'
nonceStr = str(uuid.uuid4())
timestamp = str(round(datetime.now().timestamp() * 1000))

certSign = CertificationSign('your secretId', 'your secretKey')
headers = certSign.sign(path, method, body, queryString, nonceStr, timestamp)

result = certSign.request(url, method, headers, body)
```

4 PaymentSign使用
```bash
from geovis_cloud_api_python import PaymentSign
import uuid
from datetime import datetime

path = '/v2/access/prepay'
method = 'POST'
# body为空时，传None
body = {
    'orderNo': 'test_2024092500001113',
    'productName': '测试商品',
    'total': 1,
    'payMode': 'wxpay',
    'payChannel': 'NATIVE',
    'callbackUrl': 'http://www.baidu.com?ad=12',
    'userId': 'test_userid_xxxxxxxx_yyyyyyyyyyyyy'
}
queryString = '' # 无查询参数时，传空字符串
url = f'https://api1.geovisearth.com/pay{path}'
nonceStr = str(uuid.uuid4())
timestamp = str(round(datetime.now().timestamp() * 1000))

payment = PaymentSign('your secretId', 'your secretKey', 'your mchid')
headers = payment.sign(path, method, body, queryString, nonceStr, timestamp)

result = payment.request(url, method, headers, body)
```

5 InvoiceSign使用
```bash
from geovis_cloud_api_python import InvoiceSign
import uuid
from datetime import datetime

path = '/v1/invoice'
method = 'POST'
# body为空时，传None
body = {
    "titleType":"XXX",
    "invoiceType":"1",
    "buyerName":"测试企业",
    "buyerEmail":"xxx@qq.com",
    "buyerPhone":"135xxxxxxxx",
    "remark":"",
    "items":[
        {
            "goodsCode":"",
            "goodsName":"数据服务",
            "num":2,
            "taxRate":6,
            "unit":"无",
            "taxFlag":"1",
            "amount":200,
            "mechOriginOrderNo":"1234567890"
        }
    ]
}
queryString = '' # 无查询参数时，传空字符串
url = f'https://api1.geovisearth.com/invoicecenter{path}'
nonceStr = str(uuid.uuid4())
timestamp = str(round(datetime.now().timestamp() * 1000))

invoiceSign = InvoiceSign('your secretId', 'your secretKey', 'your mchid')
headers = invoiceSign.sign(path, method, body, queryString, nonceStr, timestamp)

result = invoiceSign.request(url, method, headers, body)
```