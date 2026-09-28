# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


# class AccountMove(models.Model):
#     _inherit = "account.move"

#     date_due = fields.Date(string=u"Date d'échéance", readonly=False, states={}, index=True, copy=False)


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    is_account_invoice_line_id = fields.Integer('Lien entre account_invoice_line et account_move_line pour la migration')

