from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    profit_margin = fields.Float(
        string="Profit Margin", compute="_compute_profit_margin", store=True
    )

    @api.depends("price_unit", "product_id")
    def _compute_profit_margin(self):
        for line in self:
            if line.product_id:
                line.profit_margin = line.price_unit - line.product_id.standard_price
            else:
                line.profit_margin = 0.0
