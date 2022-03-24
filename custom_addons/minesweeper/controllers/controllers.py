# -*- coding: utf-8 -*-
# from odoo import http


# class ./customAddons/minesweeper(http.Controller):
#     @http.route('/./custom_addons/minesweeper/./custom_addons/minesweeper', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./custom_addons/minesweeper/./custom_addons/minesweeper/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./custom_addons/minesweeper.listing', {
#             'root': '/./custom_addons/minesweeper/./custom_addons/minesweeper',
#             'objects': http.request.env['./custom_addons/minesweeper../custom_addons/minesweeper'].search([]),
#         })

#     @http.route('/./custom_addons/minesweeper/./custom_addons/minesweeper/objects/<model("./custom_addons/minesweeper../custom_addons/minesweeper"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./custom_addons/minesweeper.object', {
#             'object': obj
#         })
