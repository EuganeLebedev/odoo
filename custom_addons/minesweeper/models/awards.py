from odoo import models, fields, api


class Games(models.Model):
    _name = 'minesweeper.awards'
    _description = 'Minesweeper awards'
    name = fields.Char(required=True, string="Awards")
    requirements = fields.Text(string="Achievement requirements")
