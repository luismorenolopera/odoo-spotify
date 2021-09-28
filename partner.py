from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    genres_ids = fields.One2many(
        'spotify.track',
        'partner_id',
        string='Recommended Tracks',
    )
