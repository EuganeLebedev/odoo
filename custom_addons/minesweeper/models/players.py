from odoo import models, fields, api


class Players(models.Model):
    _name = 'minesweeper.players'
    _description = 'Minesweeper players'
    _rec_name = 'nickname'

    firstname = fields.Char(required=False, string='First name', copy=False)
    lastname = fields.Char(required=False, string='Last name', copy=False)
    nickname = fields.Char(required=True, index=True, string='Nickname', copy=False)
    active = fields.Boolean(default=True, string="Is active")
    player_states = fields.Selection([('new','New'),('old','Old')], string='Player type', index=True, default='new')
    country_from_id = fields.Many2one('res.country', string='Country from', required=False, ondelete='set null')
    awards_ids = fields.Many2many("minesweeper.awards", string="Awards")
    games_ids = fields.One2many('minesweeper.games', 'player_id', string="Games")
    description = fields.Text()
    games_win = fields.Integer(compute="_player_effectiveness", store=True)
    games_lose = fields.Integer(compute="_player_effectiveness", store=True)
    effectiveness = fields.Float(compute="_player_effectiveness", store=True)
    total_score = fields.Float(compute="_total_score", store=True)

    @api.depends("games_ids")
    def _player_effectiveness(self):
        for record in self:
            record.games_win = len(list(filter(lambda record: record.status == 'win', record.games_ids)))
            record.games_lose = len(list(filter(lambda record: record.status == 'lose', record.games_ids)))

            try:
                record.effectiveness = record.games_win/record.games_lose
            except ZeroDivisionError as e:
                record.effectiveness = record.games_win

    @api.depends("games_ids")
    def _total_score(self):
        for record in self:
            record.total_score = sum(game.score for game in record.games_ids)




