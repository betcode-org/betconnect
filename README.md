<p align="center">
  <a href="https://github.com/betcode-org">
    <img src="docs/images/logo-full.png" title="betcode-org">
  </a>
</p>

![Build Status](https://github.com/betcode-org/betconnect/actions/workflows/test.yml/badge.svg) [![PyPI version](https://badge.fury.io/py/betconnect.svg)](https://pypi.python.org/pypi/betconnect) [![Downloads](https://pepy.tech/badge/betconnect)](https://pepy.tech/project/betconnect)

# betconnect

Simple python wrapper for the [BetConnect](https://developer.betconnect.com/) api, allowing for retriveal of data for active 
betting markets and betting operations associated with those markets, see [examples](https://github.com/betcode-org/betconnect/tree/master/examples)

[docs](https://betcode-org.github.io/betconnect/)

[join betcode slack group](https://join.slack.com/t/betcode-org/shared_invite/zt-h0ato238-PPbfU_T7Ji0ORjz0ESIJkg)


# client requirements

- betconnect account (client required username & password) - can be set up via the [staging](https://staging.betconnect.com/) and [production](https://www.betconnect.com/) websites. 

- api key - the api key associated with you account. Unique per environment. 
- personalised production url - live (production) accounts have unqiue urls associated with your account. 

### Using the library
```python
import betconnect

# create a client
client = betconnect.APIClient(username='username',
                              password='password',
                              api_key='api_key',
                              personalised_production_url='https://custom.betconnect.com/')

# login
client.account.login()

# find active sports
active_sports = client.betting.active_sports()
```

Available endpoints:
- client.[account](https://github.com/betcode-org/betconnect/blob/master/betconnect/endpoints/account.py) - login, logout, account preferences
- client.[betting](https://github.com/betcode-org/betconnect/blob/master/betconnect/endpoints/betting.py) - find active sports, competitions, markets. Create and find bet requests.
