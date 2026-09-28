# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 20 pour France Filets',
    'version'  : '20.0.0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 20 pour France Filets
===================================================
Reprise d'is_france_filets15 (Odoo 15).
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'sale_management',
        'sales_team',
        'mail',
        'portal',
        'account',
        'l10n_fr',
        'attachment_indexation',
        'hr',

        # API Rest Akyos : base_rest n'existe pas en 20.0, en attente de la décision du client
        # "base_rest",                    # Pour API Rest Akyos
        # "base_rest_datamodel",          # Pour API Rest Akyos
        # "base_rest_auth_user_service",  # Pour API Rest Akyos
        # "component",                    # Pour API Rest Akyos
],
    'data' : [
        'security/res.groups.xml',
        'security/ir.access.csv',

        # Migration v20 : vues, menus et rapports désactivés pour installer d'abord les modèles
        'views/res_company_view.xml',
        'views/partner_view.xml',
        'views/sale_view.xml',
        'views/account_move_view.xml',
        # 'views/is_export_compta_view.xml',
        'views/is_sale_order_line.xml',
        'views/is_filet_view.xml',
        'views/is_suivi_budget_view.xml',
        'views/is_document_employe_view.xml',
        # 'views/report_templates.xml',
        # 'views/menu.xml',
        # 'report/sale_report_templates.xml',
        # 'report/report_invoice.xml',
        # 'report/planning_report_templates.xml',
        # 'report/fiche_travail_report_templates.xml',
        # 'report/pv_reception_report_templates.xml',
        # 'report/is_suivi_budget_report_templates.xml',
        # 'report/is_suivi_budget_journal_vente_report_templates.xml',
        # 'report/report.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'is_france_filets20/static/src/css/style.css',
        ]
    },

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

