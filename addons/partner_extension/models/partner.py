from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_type = fields.Selection(
        [("vip", "VIP"), ("regular", "Regular"), ("wholesale", "Wholesale")],
        string="Customer Type",
    )
    is_preferred = fields.Boolean(string="Preferred Customer")
