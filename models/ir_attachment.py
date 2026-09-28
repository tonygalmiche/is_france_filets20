# -*- coding: utf-8 -*-
from odoo import api, fields, models


# Migration v20 : la surcharge v15 de ir.attachment.check() (anomalie 16) est remplacée par :
# - le rattachement des pièces jointes à leur enregistrement (IsPieceJointeMixin) : les droits standard s'appliquent
# - une règle ciblée dans ir.access.csv (is_attachment_chantier_access) : lecture des pièces jointes de la commande
#   par les chefs d'équipe et de secteur de ses chantiers


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    # Relations inverses des champs Many2many de pièces jointes, utilisées par la règle d'accès
    is_order_ids       = fields.Many2many('sale.order' , 'sale_order_piece_jointe_attachment_rel' , 'attachment_id', 'order_id'      , 'Commandes (pièces jointes)')
    is_chantier_pj_ids = fields.Many2many('is.chantier', 'is_chantier_piece_jointe_attachment_rel', 'attachment_id', 'is_chantier_id', 'Chantiers (pièces jointes de la commande)')


class IsPieceJointeMixin(models.AbstractModel):
    """Rattache à l'enregistrement les pièces jointes ajoutées dans ses champs Many2many :
    le widget many2many_binary les crée sans res_id quand l'enregistrement n'est pas encore sauvegardé,
    et Odoo ne les montre alors qu'à leur créateur"""
    _name = 'is.piece.jointe.mixin'
    _description = "Rattachement des pièces jointes"

    _is_piece_jointe_fields = []

    def _is_rattacher_pieces_jointes(self):
        for record in self:
            for field_name in self._is_piece_jointe_fields:
                attachments = record.sudo()[field_name].filtered(
                    lambda a: not a.res_id and a.create_uid == self.env.user
                )
                if attachments:
                    attachments.write({'res_model': record._name, 'res_id': record.id})

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._is_rattacher_pieces_jointes()
        return records

    def write(self, vals):
        res = super().write(vals)
        if any(field_name in vals for field_name in self._is_piece_jointe_fields):
            self._is_rattacher_pieces_jointes()
        return res
