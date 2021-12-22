# betconnect

Simple python wrapper for the [Betconnect](https://developer.betconnect.com/) api, allowing for retriveal of data for active 
betting markets and betting operations associated with those markets, see [examples](https://github.com/varneyo/betconnect/tree/master/examples)


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
- client.[account](https://github.com/varneyo/betconnect/blob/master/betconnect/endpoints/account.py) - login, logout, account preferences
- client.[betting](https://github.com/varneyo/betconnect/blob/master/betconnect/endpoints/betting.py) - find active sports, competitions, markets. Create and find bet requests.


