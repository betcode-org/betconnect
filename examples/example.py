from betconnect.apiclient import APIClient
from betconnect import resources
from decouple import config
from betconnect.enums import Envirnoment

SPORT_ID = 14
FIXTURE_ID = 8609469
MARKET_TYPE_ID = 6
BET_REQUEST_ID = '305de7a2-81eb-40a8-bd9d-72272d9d0b91'

def stop_active_bets(client: APIClient):
    active_bets = client.betting.get_active_bet_requests()
    for active_bet in active_bets.bets: # type: resources.ActiveBets
        if active_bet.status_name == 'Active':
            client.betting.bet_request_stop(bet_request_id=active_bet.bet_request_id)

client = APIClient(username=config("BETCONNECT_USERNAME"),
                   password=config("BETCONNECT_PASSWORD"),
                   api_key=config("BETCONNECT_API_KEY"),
                   environment=Envirnoment.PRODUCTION)


# Login
login = client.login.login()

active_sports = client.betting.active_sports()

types = client.betting.active_market_types(14)

fixtures = client.betting.active_fixtures(sport_id=SPORT_ID)


bet_requests = []
import time
while True:
    bet_request_get = client.betting.bet_request_get(
        filter=resources.filters.GetBetRequestFilter(sport_id=14)
    )
    if isinstance(bet_request_get, resources.BetRequest):
        bet_requests.append(bet_request_get)
    else:
        time.sleep(10)



stop_active_bets(client)

#client.betting.bet_request_stop(bet_request_id='8ea9d691-aa9e-4403-a482-50ebc5626705')


types = client.betting.active_market_types(14)

fixtures = client.betting.active_fixtures(sport_id=SPORT_ID)

active_fixture = fixtures[-1]

fixture_selection_prices = client.betting.selections_for_market(active_fixture.fixture_id,MARKET_TYPE_ID, False)

fixture_selection = fixture_selection_prices[0]

lay_client.login.login()


request = client.betting.bet_request_create(resources.CreateBetRequestFilter(
    fixture_id = active_fixture.fixture_id,
    market_type_id = MARKET_TYPE_ID,
    competitor = fixture_selection.competitor_id,
    price =fixture_selection.prices[0].price,
    stake = 1000,
    bet_type='Win'
))
import time
time.sleep(5)

lay_get = lay_client.betting.bet_request_get(filter=resources.GetBetRequestFilter(
bet_request_id= request.bet_request_id
))
lay_match_request = lay_client.betting.bet_request_match_more(
    bet_request_id=request.bet_request_id,
    requested_stake = int(500)
)


import time
hist_before = client.betting.bet_history(username=client._username, status='Settled')
active_bets_before = client.betting.get_active_bet_requests()
time.sleep(5)
stop = client.betting.bet_request_stop(bet_request_id=request.bet_request_id)
hist_after = client.betting.bet_history(username=client._username, status='Settled')
active_bets_after = client.betting.get_active_bet_requests()



active_bets = client.betting.get_active_bet_requests()
active_bets_2 = client.betting.get_active_bet_requests()



request_2 = client.betting.bet_request_create(resources.CreateBetRequestFilter(
    fixture_id = FIXTURE_ID,
    market_type_id = MARKET_TYPE_ID,
    competitor = fixture_selection_prices[0].competitor_id,
    price =fixture_selection_prices[0].max_price,
    stake = 50,
    bet_type='WIN'
))

lay_back_bet_request = lay_client.betting.bet_request_get(filter=resources.GetBetRequestFilter(
    bet_request_id=request.bet_request_id
))

#lay_match_request = lay_client.betting.bet_request_match(
#    bet_request_id=request.bet_request_id,
#    accepted_stake = 10
#)





active_requests = client.betting.get_active_bet_requests()

lay_back_bet_request = lay_client.betting.bet_request_get(filter=resources.GetBetRequestFilter(
    bet_request_id=request.bet_request_id
))

back_bet_request = client.betting.bet_request_get(filter=resources.GetBetRequestFilter(
    bet_request_id=request.bet_request_id
))



#lay_match_request = lay_client.betting.bet_request_match(
#    bet_request_id=request.bet_request_id,
#    accepted_stake = 10
#)

lay_match_request = lay_client.betting.bet_request_match_more(
    bet_request_id=request.bet_request_id,
    requested_stake = 10.0
)


request = client.betting.bet_request_create(resources.CreateBetRequestFilter(
    fixture_id = FIXTURE_ID,
    market_type_id = MARKET_TYPE_ID,
    competitor = fixture_selection_prices[0].competitor_id,
    price =fixture_selection_prices[0].max_price,
    stake = 10,
    bet_type='WIN'
))

back_bet_request = client.betting.bet_request_get(filter=resources.GetBetRequestFilter(
    sport_id=SPORT_ID,
    bet_request_id=request.bet_request_id
))

lay_back_bet_request = lay_client.betting.bet_request_get(filter=resources.GetBetRequestFilter(
    sport_id=SPORT_ID,
    bet_request_id=request.bet_request_id
))

lay_request = lay_client.betting.bet_request_match(
    bet_request_id=request.bet_request_id,
    accepted_stake = 10
)

lay_request_match_more = lay_client.betting.bet_request_match_more(
    bet_request_id=request.bet_request_id,
    requested_stake = 10
)




horse_racing = [s for s in active_sports if s.display_name == 'Horse Racing'][0]

# active regions
active_regions = client.betting.active_regions(sport_id=horse_racing.sport_id)

england = [r for r in active_regions if r.name == 'England'][0]
ireland = [r for r in active_regions if r.name == 'Ireland'][0]

# active market types
active_market_types = client.betting.active_market_types(
    sport_id=horse_racing.sport_id
)

win_type = [t for t in active_market_types if t.name == 'WIN'][0]

# get active competitions
active_competitions = client.betting.active_competitions(
    region_id=england,
    sport_id=horse_racing.sport_id
)

# All active fixtures with selections and prices (can be slow to request this way)
active_fixtures = client.betting.get_fixtures_with_active_selections(
    sport_id=horse_racing.sport_id,
    market_type_id=win_type.market_type_id
)



# Get active sports
active_sports = client.betting.active_sports()