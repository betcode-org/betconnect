from betconnect.apiclient import APIClient
from decouple import config
from betconnect.enums import Environment

import logging

logger = logging.getLogger(__name__)

"""
This file contains examples of account related requests
"""

# Create a trading client instance
client = APIClient(
    username=config("STAGING_BETCONNECT_USERNAME"),
    password=config("STAGING_BETCONNECT_PASSWORD"),
    api_key=config("STAGING_BETCONNECT_API_KEY"),
    environment=Environment.STAGING,
    personalised_production_url=config("PRODUCTION_URI"),
)

# login
login = client.account.login()

# get account balance
balance = client.account.get_balance()

# get account preferences
user_preferences = client.account.get_user_preferences()

# update client status (refresh token)
client.account.refresh_session_token()

# logout of client
client.account.logout()
