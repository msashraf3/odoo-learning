from odoo import models, fields
from odoo.exceptions import ValidationError


class SalesOrder(models.Model):
    _inherit = "sale.order"
    internal_note = fields.Text(string="Internal Note")

    def action_confirm(self):
        for record in self:
            if not record.internal_note:
                raise ValidationError("You must add an internal note before confirming.")
        return super().action_confirm()
