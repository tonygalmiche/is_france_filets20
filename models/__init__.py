# -*- coding: utf-8 -*-
# Anomalie 16 (faille de sécurité) : surcharge de ir.attachment.check() non reprise en v20 (méthode obsolète depuis la 19.0),
# accès des chefs d'équipe aux pièces jointes des commandes à remplacer par une règle ciblée
# from . import ir_attachment
from . import res_users
from . import res_company
from . import res_partner
from . import sale
from . import account_move
from . import is_export_compta
from . import is_sale_order_line
from . import is_filet
from . import is_suivi_budget
from . import is_res_partner
from . import is_document_employe
