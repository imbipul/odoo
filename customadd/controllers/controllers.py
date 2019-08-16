# -*- coding: utf-8 -*-
from odoo import http

# class Customadd(http.Controller):
#     @http.route('/customadd/customadd/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customadd/customadd/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customadd.listing', {
#             'root': '/customadd/customadd',
#             'objects': http.request.env['customadd.customadd'].search([]),
#         })

#     @http.route('/customadd/customadd/objects/<model("customadd.customadd"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customadd.object', {
#             'object': obj
#         })

