from odoo import models, fields, api


class Fields(models.Model):
    _name = 'minesweeper.fields'
    _description = 'Minesweeper fields'
    name = fields.Char()
    # image = fields.Image(string="Image")
    games_ids = fields.One2many('minesweeper.games', 'field_id', string="Games")
    x_size = fields.Integer()
    y_size = fields.Integer()
    field_size = fields.Char(compute="_compute_size")
    total_games = fields.Char(compute="_total_games")
    games_win = fields.Char(compute="_total_games", string="Total games win")
    games_lose = fields.Char(compute="_total_games", string="Total games lose")

    @api.depends("x_size", "y_size")
    def _compute_size(self):
        for record in self:
            record.field_size = f"{record.x_size}x{record.y_size}"

    @api.depends("games_ids")
    def _total_games(self):
        for record in self:
            record.total_games = len(record.games_ids)
            record.games_win = len(list(filter(lambda game: game.status == 'win', record.games_ids)))
            record.games_lose = len(list(filter(lambda game: game.status == 'lose', record.games_ids)))

    @api.onchange("name")
    def _on_change_name(self):
        if self.name == 'Newbie':
            self.x_size = 9
            self.y_size = 9
