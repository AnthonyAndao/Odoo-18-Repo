from odoo import models, fields, api

class RoomTypes(models.Model):
    _name = 'hotel.roomtypes'  # Model name
    _description = 'Room Types'

    name = fields.Char("Room Type", required=True)
    description = fields.Char("Room Type Description")
    photobed = fields.Image("Bed Photo")
    photorestroom = fields.Image("Comfort Room Photo")
    room_image = fields.Image(string="Room Image")
    bathroom_image = fields.Image(string="Bathroom Image")
    daily_charge = fields.Float(string="Daily Charge")
    extra_charge = fields.Float(string="Extra Charge")
    discount = fields.Float(string="Discount")
    total_charge = fields.Float(string="Total Charge", compute="_compute_total_charge", readonly=True)
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    ], string="Room Type", required=True)
    room_capacity = fields.Integer(string="Room Capacity")
    room_size = fields.Float(string="Room Size (sqm)")
    room_bed_type = fields.Selection([
        ('single', 'Single Bed'),
        ('double', 'Double Bed'),
        ('queen', 'Queen Bed'),
        ('king', 'King Bed')
    ], string="Bed Type")
    room_bed_count = fields.Integer(string="Number of Beds")

    def _compute_total_charge(self):
        for record in self:
            record.total_charge = (record.daily_charge + record.extra_charge) * (1 - (record.discount or 0) / 100)