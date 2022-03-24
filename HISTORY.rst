.. :changelog:

Release History
---------------

0.1.1 (24-03-2022)
+++++++++++++++++++
**Improvements**

- #17 session timeout

0.1.0 (24-03-2022)
+++++++++++++++++++
**Improvements**

- betcode-org migration
- __version__ added / setup updated
- GitHub actions added
- req-test added
- MIT Licence added
- ReadMe update
- docs added

0.0.7 (18-01-2022)
+++++++++++++++++++
**Resource updates**

- typing improvements


0.0.5 (21-12-2021)
+++++++++++++++++++
**Resource update**

- locality nullable

0.0.4 (21-12-2021)
+++++++++++++++++++
**Line Markets Bug fix**

- fix for line markets selections_for_market #9
- handicap param changed to string on active_selections & prices methods


0.0.3 (19-12-2021)
+++++++++++++++++++
**ApiClient Changes (Breaking Changes)**

- new personalised_production_url made a manditory paramater on the client

**Baseendpoint (Breaking Changes)**

- process_request_exception, check_bet_request_id, load_json_content, check_status_code changed to staticmethods

**CustomerStrategyRef & CustomerOrderRef (Breaking Changes)**

- is_valid_customer_order_ref & is_valid_customer_strategy_ref moved onto the class as a staticmethod (from utils)
- create_customer_order_ref & create_customer_strategy_ref moved to the class as classmethods (from utils)

**Updated Testing**

- All betting functions and resources re-tested to new BetConnect swagger spec
- exceptions classes

**Examples Updated**

- examples updated to reflect new required personalised_production_url

**House Keeping**

- Docstring updates
- gammar and spelling updates

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
