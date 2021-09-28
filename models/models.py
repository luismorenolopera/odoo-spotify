# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from . import constants
from . import spotify_api


class Track(models.Model):
    _name = 'spotify.track'
    _description = 'Spotify Tracks'

    genre = fields.Selection(
        constants.GENRES,
        string="Genre",
        default='acoustic',
        required=True,
    )
    title = fields.Char(
        string="Title",
        compute='_get_metadata_track',
        store=True,
    )
    artist = fields.Char(
        string="Artist",
        compute='_get_metadata_track',
        store=True,
    )
    track_url = fields.Char(
        string="See on Spotify",
        compute='_get_metadata_track',
        store=True,
    )
    partner_id = fields.Many2one(
        'res.partner',
        ondelete='set null',
        readonly=True,
    )

    @api.depends('genre')
    def _get_metadata_track(self):
        token = self.env['ir.config_parameter'].sudo().get_param('spotify.token')
        market = self.env['ir.config_parameter'].sudo().get_param('spotify.market')
        if not token:
            raise exceptions.ValidationError('please set up a spotify OAuth token')
        for record in self:
            spotify = spotify_api.SpotifyTrackAPI(token, market)
            spotify.get_recommendations(record.genre)
            record.title = spotify.get_title()
            record.artist = spotify.get_artist()
            record.track_url = spotify.get_track_url()
