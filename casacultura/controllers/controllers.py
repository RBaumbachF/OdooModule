# -*- coding: utf-8 -*-
# from odoo import http


# class Casacultura(http.Controller):
#     @http.route('/casacultura/casacultura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/casacultura/casacultura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('casacultura.listing', {
#             'root': '/casacultura/casacultura',
#             'objects': http.request.env['casacultura.casacultura'].search([]),
#         })

#     @http.route('/casacultura/casacultura/objects/<model("casacultura.casacultura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('casacultura.object', {
#             'object': obj
#         })
