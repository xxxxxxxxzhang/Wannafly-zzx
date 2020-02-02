import jwt

# payload
token_dict = {
    "iss": "WebGoat Token Builder",
    "aud": "webgoat.org",
    "iat": 1580615877,
    "exp": 1580615937,
    "sub": "tom@webgoat.org",
    "username": "WebGoat",
    "Email": "tom@webgoat.org",
    "Role": ["Manager", "Project Administrator"]
}
key = "shipping"
# headers
headers = {
    "alg": "HS256"
}
# 调用jwt库,生成json web token
jwt_token = jwt.encode(token_dict,  # payload, 有效载体
                       key,
                       algorithm="HS256",  # 指明签名算法方式, 默认是HS256，需要与headers中"alg"保持一致。
                       headers=headers  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)
                       )
print("jwt_token")
print(jwt_token)
