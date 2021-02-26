# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    iface_shop_owner = fields.Boolean(string='Enable Shop Owner', help='Allow the cashier to set shop owner')
    shop_owner = fields.Many2one('res.users', string="Shop Owner")