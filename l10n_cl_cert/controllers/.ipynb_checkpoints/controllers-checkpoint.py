# -*- coding: utf-8 -*-
from odoo import http


class L10nClCert(http.Controller):
    @http.route('/l10n_cl_cert/conv', auth='user')
    def index(self, **kw):
        model = self.env["account.move"]
        content = model._xml_dte_list(["FNA 000110", "FNA 000111", "FNA 000112", "N/C 000018"])
        filecontent = base64.b64decode(content)
        filename = "envio.xml"
        return request.make_response(filecontent,
                            [('Content-Type', 'application/octet-stream'),
                             ('Content-Disposition', content_disposition(filename))])

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
