# -*- coding: utf-8 -*-
from odoo import api, models, fields


class SalesStatus(models.Model):
    """status bar updated in sales module"""
    _inherit = 'sale.order'

    sale_order_date = fields.Date(compute="_compute_date")
    week = fields.Integer(compute="_compute_week")
    year = fields.Char(compute="_compute_year")

    @api.depends('sale_order_date')
    def _compute_date(self):
        for rec in self:
            rec.sale_order_date = fields.Date.to_string(rec.date_order.date())

    @api.depends('week')
    def _compute_week(self):
        for rec in self:
            rec.week = rec.sale_order_date.isocalendar().week

    @api.depends('year')
    def _compute_year(self):
        for rec in self:
            rec.year = rec.sale_order_date.isocalendar().year
