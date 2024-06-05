# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[('confirmed', 'OC Confirmado'), ('closed', 'Done')])
