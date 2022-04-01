from odoo import models, fields, api
from datetime import datetime


class Games(models.Model):
    _name = 'minesweeper.games'
    _description = 'Minesweeper games'
    _rec_name = 'date'
    status = fields.Selection([('win', 'Win'), ('lose', 'Lose')], string='Game status')
    player_id = fields.Many2one('minesweeper.players', string='Player', required=True, ondelete='restrict')
    field_id = fields.Many2one('minesweeper.fields', string='Field', required=True, ondelete='restrict')
    duration = fields.Integer(string="Game duration")
    score = fields.Integer(string="Game scores")
    date = fields.Date(string="Date of the game", default=datetime.today())
