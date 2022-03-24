import datetime

import requests
from .utils import get_data_from_site
from odoo import api, SUPERUSER_ID
import random

def fill_awards_from_web(cr):
    """
    Generate awards from WEB
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    awards = get_data_from_site.get_awards_from_site()
    for award in awards:
        vals = {
            "id": award['award_name'],
            "name": award['award_name'],
            "requirements": award['award_requirements'],
        }
        env['minesweeper.awards'].create(vals)

def create_random_games_data(env, player):
    """
    Generate random games for players
    """
    detes = [datetime.date.today() - datetime.timedelta(days=i) for i in range(1, 10)]
    for _ in range(1, random.randint(5, 15)):



        games_val = {
            'player_id': player.id,
            'field_id': random.randint(1, 4),
            'duration': random.randint(10, 10000),
            'score': random.randint(0, 1000000),
            'date': random.choice(detes),
            'status': random.choice(['win', 'lose'])

        }
        env['minesweeper.games'].create(games_val)

def fill_players_from_web(cr):
    """
    Generate players from WEB
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    players = get_data_from_site.get_players_from_site()
    fields = env["minesweeper.fields"].search([])
    for player in players:
        country = env["res.country"].search([('code', '=', player["country"])]).id

        vals = {
            "nickname": player["nickname"],
            "country_from_id": country
        }
        #
        player = env['minesweeper.players'].create(vals)
        create_random_games_data(env, player)


def pre_init_hook(cr):
    pass



def post_init_hook(cr, registry):
    fill_awards_from_web(cr)
    fill_players_from_web(cr)
    return True