# -*- coding: utf-8 -*-
# from odoo import http


# class L10nClCert(http.Controller):
#     @http.route('/l10n_cl_cert/l10n_cl_cert/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_cert/l10n_cl_cert/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_cert.listing', {
#             'root': '/l10n_cl_cert/l10n_cl_cert',
#             'objects': http.request.env['l10n_cl_cert.l10n_cl_cert'].search([]),
#         })

#     @http.route('/l10n_cl_cert/l10n_cl_cert/objects/<model("l10n_cl_cert.l10n_cl_cert"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_cert.object', {
#             'object': obj
#         })
