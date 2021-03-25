# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = ['account.move']
    
    def _xml_dte_list(self, dte_names):
        dtes_attachment = env["account.move"].search([("name", "in", dte_names)])
        subtotals = env["account.move"].read_group([("name", "in", dte_names)], 
                                                   fields=["l10n_latam_document_type_id"],
                                                   groupby=["l10n_latam_document_type_id"])
        tipodte_subtotals = []
        for each in subtotals:
            code = each["l10n_latam.document.type"].search([("id", "=", 
                                                             each["l10n_latam_document_type_id"][0])])
            count = each["l10n_latam_document_type_id_count"]
            tipodte.append({'code': code,
                            'count': count})
        dtes = []
        for each in dtes_attachment:
            dtes.append(base64.b64decode(each.l10n_cl_dte_file.datas).decode('ISO-8859-1'))
        template = self.env.ref('l10n_cl_cert.envio_dte_cert')
        

# class l10n_cl_cert(models.Model):
#     _name = 'l10n_cl_cert.l10n_cl_cert'
#     _description = 'l10n_cl_cert.l10n_cl_cert'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
