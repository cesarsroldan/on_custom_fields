# -*- coding: utf-8 -*-

from . import controllers

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    trade_terms = fields.Selection([
        ('fob_1','FOB Colon, Panama'),
        ('fob_2', 'FOB Shanghai'),
        ('fob_3', 'FOB Shenzhen'),
        ('fob_4', 'FOB Hong Kong')], string="Trade Terms", default="fob_1")
    country_id = fields.Many2one('res.country', 'Destination country', required=False)
PurchaseOrder()