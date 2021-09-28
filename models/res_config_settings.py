from odoo import fields, models
from . import constants


class Settings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'spotify.config.settings'
    _description = 'Settings for spotify module'

    token = fields.Char(
        string="OAuth token",
        config_parameter='spotify.token',
    )
    market = fields.Selection(
        constants.MARKETS,
        string="Market",
        default='CO',
        config_parameter='spotify.market',
        required=True,
    )
