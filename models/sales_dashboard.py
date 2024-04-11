# -*- coding: utf-8 -*-
from odoo import api, models
import datetime


class PartnerDashboard(models.Model):
    """Sales Dashboard"""
    _name = 'sales.dashboard'
    _description = 'sales Dashboard'

    @api.model
    def get_tiles_data(self):
        """ Return the chart data"""
        company_id = self.env.company
        currency = company_id.currency_id.symbol
        sale_team_name = self.env['crm.team'].search([]).mapped('name')
        sale_team_count = []
        for i in sale_team_name:
            data = self.env['sale.order'].search_count([('team_id.name', '=', i)])
            sale_team_count.append(data)
        sales = self.env['sale.order'].search([])
        sales_person = self.env['res.partner'].search([('sale_order_ids', '=', sales.ids)]).mapped('name')
        sale_count = []
        customer_count = []
        for rec in sales_person:
            data = self.env['sale.order'].search_count([('user_id.name', '=', rec)])
            sale_count.append(data)
            datas = self.env['sale.order'].search_count([('partner_id.name', '=', rec)])
            customer_count.append(datas)
        customer = self.env['res.partner'].search([('sale_order_ids', '=', sales.ids)]).mapped('name')
        product = self.env['product.product'].search([])
        lowest_selling_product = product.sorted('sales_count').mapped('name')
        highest_selling_product = product.sorted('sales_count', reverse=True).mapped('name')
        lowest_count = []
        highest_count = []
        for rec in lowest_selling_product:
            data = self.env['sale.order.line'].search_count([('product_id.name', '=', rec)])
            lowest_count.append(data)
        for rec in highest_selling_product:
            data = self.env['sale.order.line'].search_count([('product_id.name', '=', rec)])
            highest_count.append(data)
        state = ['sale', 'cancel']
        status = []
        for rec in state:
            status1 = self.env['sale.order'].search_count([('state', '=', rec)])
            status.append(status1)
        total_revenue = sum(sales.mapped('amount_total'))
        total_sale_count = []
        status1 = self.env['sale.order'].search_count([('state', '=', 'sale')])
        total_sale_count.append(status1)
        print(total_sale_count)
        invoice_status = []
        inv_status = self.env['sale.order'].search_count([('invoice_status', '=', 'to invoice')])
        invoice_status.append(inv_status)

        return {
            'team': sale_team_name,
            'total_sale': sale_team_count,
            'sale_person': sales_person,
            'sale_count': sale_count,
            'customer': customer,
            'customer_count': customer_count,
            'lowest_selling_product': lowest_selling_product,
            'highest_selling_product': highest_selling_product,
            'lowest_count': lowest_count,
            'highest_count': highest_count,
            'status': status,
            'currency': currency,
            'total_revenue': total_revenue,
            'total_sale_count': total_sale_count,
            'invoice_status': invoice_status
        }

    @api.model
    def get_week_data(self):
        """ Return the week chart data"""
        company_id = self.env.company
        currency = company_id.currency_id.symbol
        print(currency)
        my_date = datetime.date.today()
        sale_team_name = self.env['crm.team'].search([]).mapped('name')
        current_week = my_date.isocalendar().week
        sale_team_count = []
        for i in sale_team_name:
            datas = self.env['sale.order'].search([('team_id.name', '=', i)])
            data = len(datas.filtered(lambda x: x.week == current_week))
            sale_team_count.append(data)
        sales = self.env['sale.order'].search([])
        sales_person = self.env['res.partner'].search([('sale_order_ids', '=', sales.ids)]).mapped('name')
        sales_person_count = []
        customer_count = []
        customer = self.env['res.partner'].search([('sale_order_ids', '=', sales.ids)]).mapped('name')
        for rec in sales_person:
            datas = self.env['sale.order'].search([('user_id', '=', rec)])
            data = len(datas.filtered(lambda x: x.week == current_week))
            sales_person_count.append(data)
            datas_customer = self.env['sale.order'].search([('partner_id.name', '=', rec)])
            data_customer = len(datas_customer.filtered(lambda x: x.week == current_week))
            customer_count.append(data_customer)
        product = self.env['product.product'].search([])
        lowest_selling_product = product.sorted('sales_count').mapped('name')
        highest_selling_product = product.sorted('sales_count', reverse=True).mapped('name')
        lowest_count = []
        highest_count = []
        for rec in lowest_selling_product:
            datas = self.env['sale.order.line'].search([('product_id.name', '=', rec)])
            data = len(datas.filtered(lambda x: x.order_id.week == current_week))
            lowest_count.append(data)
        for rec in highest_selling_product:
            datas = self.env['sale.order.line'].search([('product_id.name', '=', rec)])
            data = len(datas.filtered(lambda x: x.order_id.week == current_week))
            highest_count.append(data)
        state = ['sale', 'cancel']
        status = []
        for rec in state:
            datas = self.env['sale.order'].search([('state', '=', rec)])
            data = len(datas.filtered(lambda x: x.week == current_week))

            status.append(data)
        return {
            'sale_team_name': sale_team_name,
            'sale_team_count': sale_team_count,
            'sales_person': sales_person,
            'sales_person_count': sales_person_count,
            'customer_count': customer_count,
            'customer': customer,
            'lowest_selling_product': lowest_selling_product,
            'highest_selling_product': highest_selling_product,
            'lowest_count': lowest_count,
            'highest_count': highest_count,
            'status': status,
            'currency': currency,
        }

    @api.model
    def get_year_data(self):
        """ return year chart data"""
        year = datetime.date.today().strftime("%Y")
        sale_team_count = []
        sale_team_name = self.env['crm.team'].search([]).mapped('name')
        for i in sale_team_name:
            datas = self.env['sale.order'].search([('team_id.name', '=', i)])
            data = len(datas.filtered(lambda x: x.year == year))
            sale_team_count.append(data)
        sales = self.env['sale.order'].search([])
        sales_person = self.env['res.partner'].search([('sale_order_ids', '=', sales.ids)]).mapped('name')
        sales_person_count = []
        customer_count = []
        customer = self.env['res.partner'].search([('sale_order_ids', '=', sales.ids)]).mapped('name')
        for rec in sales_person:
            datas = self.env['sale.order'].search([('user_id', '=', rec)])
            data = len(datas.filtered(lambda x: x.year == year))
            sales_person_count.append(data)
            datas_customer = self.env['sale.order'].search([('partner_id.name', '=', rec)])
            data_customer = len(datas_customer.filtered(lambda x: x.year == year))
            customer_count.append(data_customer)
        product = self.env['product.product'].search([])
        lowest_selling_product = product.sorted('sales_count').mapped('name')
        highest_selling_product = product.sorted('sales_count', reverse=True).mapped('name')
        lowest_count = []
        highest_count = []
        for rec in lowest_selling_product:
            datas = self.env['sale.order.line'].search([('product_id.name', '=', rec)])
            data = len(datas.filtered(lambda x: x.order_id.year == year))
            lowest_count.append(data)
        for rec in highest_selling_product:
            datas = self.env['sale.order.line'].search([('product_id.name', '=', rec)])
            data = len(datas.filtered(lambda x: x.order_id.year == year))
            highest_count.append(data)
        state = ['sale', 'cancel']
        status = []
        for rec in state:
            datas = self.env['sale.order'].search([('state', '=', rec)])
            data = len(datas.filtered(lambda x: x.year == year))
            status.append(data)
        return {
            'sale_team_name': sale_team_name,
            'sale_team_count': sale_team_count,
            'sales_person': sales_person,
            'sales_person_count': sales_person_count,
            'customer_count': customer_count,
            'customer': customer,
            'lowest_selling_product': lowest_selling_product,
            'highest_selling_product': highest_selling_product,
            'lowest_count': lowest_count,
            'highest_count': highest_count,
            'status': status
        }
