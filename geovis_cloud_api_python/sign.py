
from datetime import datetime
import hmac
import json
import requests
import uuid
import base64
import hashlib


class CloudApiSign(object):
    def __init__(self, secretId, secretKey, serviceName, extendKeys) -> None:
        self.secretId = secretId
        self.secretKey = secretKey
        self.serviceName = serviceName
        self.extendKeys = extendKeys

    def sign(self, path, method, body, queryString, nonceStr, timestamp):
        if (body == None):
            body = ''
        else:
            body = json.dumps(body, ensure_ascii=False).replace(' ', '')

        stringToSign = self.serviceName + "\n" + method + "\n" + path + "\n" + queryString + "\n" + body + "\n" + nonceStr + "\n" + timestamp
        secretKey = base64.b64decode(self.secretKey)
        signature = hmac.new(secretKey, stringToSign.encode('utf-8'), hashlib.sha256).hexdigest()
        return {
            'Content-Type': 'application/json',
            'authorization': f'secretId={self.secretId},nonceStr={nonceStr},service={self.serviceName},timestamp={timestamp},signature={signature}{self.getExtendParam(self.extendKeys)}'
        }
    
    def request(self, url: str, method: str, headers: object, body: object|None):
        if (body == None):
            body = ''
        else:
            body = json.dumps(body, ensure_ascii=False).replace(' ', '')
        response = requests.request(method, url, headers=headers, data=body)
        return response.text

    def getExtendParam(self, extendKeys):
        result = ''
        if (extendKeys != None):
            for item in extendKeys:
                result += f',{item[0]}={item[1]}'
        return result

class PaymentSign(CloudApiSign): 
    def __init__(self, secretId, secretKey, mchid) -> None:
        super().__init__(secretId, secretKey, 'geovis-payment-center', [['mchid', mchid]])

class CertificationSign(CloudApiSign): 
    def __init__(self, secretId, secretKey) -> None:
        super().__init__(secretId, secretKey, 'geovis-certification', None)

class DataCloudSign(CloudApiSign): 
    def __init__(self, secretId, secretKey) -> None:
        super().__init__(secretId, secretKey, 'geovis-data-cloud', None)
