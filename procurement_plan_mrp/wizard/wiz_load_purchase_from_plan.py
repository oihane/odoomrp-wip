# -*- coding: utf-8 -*-
# (c) 2015 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, api


class WizLoadPurchaseFromPlan(models.TransientModel):

    _inherit = 'wiz.load.purchase.from.plan'

    @api.multi
    def _prepare_vals_for_procurement(self, prod_vals, plan, product, date):
        vals = super(
            WizLoadPurchaseFromPlan, self)._prepare_vals_for_procurement(
            prod_vals, plan, product, date)
        vals['level'] = 1000
        return vals
