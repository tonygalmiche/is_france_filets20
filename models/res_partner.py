# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import datetime


def _date_creation():
    now  = datetime.date.today()
    return now.strftime('%Y-%m-%d')


class IsRegion(models.Model):
    _name='is.region'
    _description = "IsRegion"
    _order='name'

    name = fields.Char('Région')


class IsSecteurActivite(models.Model):
    _name='is.secteur.activite'
    _description = "IsSecteurActivite"
    _order='name'

    name = fields.Char(u"Secteur d'activité")


class IsOrigine(models.Model):
    _name='is.origine'
    _description = "IsOrigine"
    _order='name'

    name = fields.Char(u"Origine Client")


class IsGroupeClient(models.Model):
    _name='is.groupe.client'
    _description = "IsGroupeClient"
    _order='name'

    name      = fields.Char(u"Groupe client", required=True)


class ResPartner(models.Model):
    _inherit = "res.partner"

    fax                = fields.Char('Fax')
    mobile             = fields.Char('Mobile')  # Supprimé d'Odoo en v20, remis pour les SMS du planning
    is_code_client_ebp = fields.Char('Code Client EBP')
    is_date_creation   = fields.Date('Date de création', default=lambda *a: _date_creation())
    is_siren           = fields.Char('SIREN')
    is_afacturage      = fields.Selection([
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ], 'Afacturage')
    is_validation_financiere = fields.Selection([
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ], u'Validation financière')
    is_type_partenaire = fields.Selection([
        ('Client'      , 'Client'),
        ('Prospect'    , 'Prospect'),
        ('Prescripteur', 'Prescripteur'),
    ], 'Type de partenaire')
    is_date_commande       = fields.Date(u'Date première commande')
    is_region_id           = fields.Many2one('is.region'          , u'Région')
    is_secteur_activite_id = fields.Many2one('is.secteur.activite', u"Secteur d'activité")
    is_origine_id          = fields.Many2one('is.origine'         , u'Origine Client')
    is_groupe_client_id    = fields.Many2one('is.groupe.client'   , u'Groupe client')

    # En v20, is_company est calculé (sans parent et avec un n° de TVA) : la plupart des sociétés
    # de France Filets n'ont pas de TVA. Comme en v15, c'est une case à cocher, la valeur saisie est conservée
    is_company = fields.Boolean(string='Société', readonly=False)

    def _compute_is_company(self):
        for partner in self:
            partner.is_company = partner.is_company



