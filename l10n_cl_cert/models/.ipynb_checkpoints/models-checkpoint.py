# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from html import unescape

import logging
_logger = logging.getLogger(__name__)

class AccountInvoiceReference(models.Model):
    _inherit = 'l10n_cl.account.invoice.reference'
    l10n_cl_reference_doc_type_selection = fields.Selection(selection_add=[("SET", "(SET) Set de Pruebas para SII")],
                                                           ondelete={'SET': 'set default'})
    
    

class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = ['account.move']
    
    def _xml_dte_list(self, dte_names):
        first_doc = None
        subtotals = self.env["account.move"].read_group([("name", "in", dte_names)], 
                                                   fields=["l10n_latam_document_type_id"],
                                                   groupby=["l10n_latam_document_type_id"])
        tipodte_subtotals = []
        for each in subtotals:
            code = self.env["l10n_latam.document.type"].search([("id", "=", 
                                                             each["l10n_latam_document_type_id"][0])]).code
            count = each["l10n_latam_document_type_id_count"]
            tipodte_subtotals.append({'code': code,
                            'count': count})
        dtes = []
        for each in dte_names:
            dte_attachment = self.env["account.move"].search([("name", "=", each)])[0]
            dtes.append(base64.b64decode(dte_attachment.l10n_cl_dte_file.datas).decode('ISO-8859-1'))
            if not first_doc:
                first_doc = dte_attachment

        digital_signature = first_doc.company_id._get_digital_signature(user_id=self.env.user.id)
        template = self.env.ref('l10n_cl_cert.envio_dte_cert')
        # _logger.info('Previo a render: {}'.format(tipodte_subtotals))
        dte_rendered = template._render({
            'RutEmisor': self._l10n_cl_format_vat(first_doc.company_id.vat),
            'RutEnvia': first_doc.company_id._get_digital_signature(user_id=self.env.user.id).subject_serial_number,
            'RutReceptor': first_doc.partner_id.vat,
            'FchResol': first_doc.company_id.l10n_cl_dte_resolution_date,
            'NroResol': first_doc.company_id.l10n_cl_dte_resolution_number,
            'TmstFirmaEnv': self._get_cl_current_strftime(),
            'dtes': dtes,
            'tipodte_subtotals': tipodte_subtotals
        })
        #_logger.info('Despues del render')
        dte_rendered = unescape(dte_rendered.decode('utf-8')).replace('<?xml version="1.0" encoding="ISO-8859-1" ?>', '')
        _logger.info('Despues de Unescape: {}'.format(dte_rendered))
        dte_signed = self._sign_full_xml(
            dte_rendered, digital_signature, 'SetDoc',
            'env',
            False
        )
        dte_final = dte_signed.encode('iso-8859-1')
        # _logger.info('Despues de Sign')
        # _logger.info('Envío DTE: {}'.format(dte_final))
        return (dte_final)

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
