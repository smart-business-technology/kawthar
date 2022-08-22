# -*- coding: utf-8 -*-
# Part of Probuse Consulting Service Pvt. Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class ProductProduct(models.Model):
    
    _inherit = 'product.product'


    def action_mo_custom(self):
        action = self.env.ref('mrp.mrp_production_action').sudo().read()[0]
        action['domain'] = [('product_id', 'in', self.ids)]
        return action

    def action_workorder_custom(self):
        action = self.env.ref('mrp.mrp_workorder_todo').sudo().read()[0]
        action['domain'] = [('product_id', 'in', self.ids)]
        return action

    def action_unbuild_orders_custom(self):
        action = self.env.ref('mrp.mrp_unbuild').sudo().read()[0]
        action['domain'] = [('product_id', 'in', self.ids)]
        return action

    def action_scrap_orders_custom(self):
        action = self.env.ref('stock.action_stock_scrap').sudo().read()[0]
        action['domain'] = [('product_id', 'in', self.ids)]
        return action

    def action_bom_custom(self):
        action = self.env.ref('mrp.mrp_bom_form_action').sudo().read()[0]
        action['domain'] = [('product_id', 'in', self.ids)]
        return action

    def action_routing_custom(self):
        bom_records = self.env['mrp.bom']
        for rec in self:
            bom_ids = bom_records.search([('product_id', 'in', rec.ids)])
            routing_ids = self.env['mrp.routing.workcenter']
            for bom in bom_ids:
                if bom.routing_id:
                    routing_ids += bom.routing_id
            action = self.env.ref('mrp.mrp_routing_action').sudo().read()[0]
            action['domain'] = [('id', 'in', routing_ids.ids)]
        return action

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
