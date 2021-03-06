# Copyright 2019 Akretion <raphael.reverdy@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    def _prepare_contract_line_values(self, contract):
        self.ensure_one()
        res = (
            super().
            _prepare_contract_line_values(contract))

        contract.fsm_location_id = self.order_id.fsm_location_id
        return res

    @api.multi
    def _field_service_generation(self):
        """ For contract lines, skip creating any type of
            field service order. The contract will do this
        """
        return super(
            SaleOrderLine, self.filtered(lambda l: not l.is_contract)
            )._field_service_generation()
