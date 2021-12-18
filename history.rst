.. :changelog:

Release History
---------------

0.0.2 (18-12-2021)
+++++++++++++++++++
**ApiClient Changes (Breaking Changes)**

- change of login endpoint to account endpoint (APIClient)
- new personalised_production_url to handle betconnect unique supplied user production urls

**New Account Endpoint, Formerly Login (Breaking Changes)**

- get balance moved from betting endpoint to account endpoint
- new get_user_preferences request added
- both balance and get_user_preferences are called now on login
- status function renamed to refresh_session_token

**Betting Endpoint Functions Added (Breaking Changes)**

- my_bets new function added
- get balance removed (moved to the accounts endpoint)

**New Enums Helper Classes Created**

- various enums now created to help find correct status for requests

**Custom Exceptions**

- custom exceptions now throw to provide more user specific information


**Utils**

- uuid and strategy hashing functions added

**Tests**

- betting and account resource tests added
- betting endpoint new functions tested (see above function additions)
- account endpoint new functions test (see above function additions)

**Resource Name Changes (Breaking Change)**

- ActiveBetsRequest renamed to ActiveBetRequests

**New Examples Added**

- account, bettinghistory, dailyhorseracing & datarequests
- example.py removed
