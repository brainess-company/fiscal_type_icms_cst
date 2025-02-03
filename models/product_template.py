from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    cst_icms = fields.Many2one(
        "l10n_br_fiscal.cst",
        string="Código CST ICMS"
    )

    fiscal_type = fields.Selection(
        selection=[
            ("00", "Mercadoria para Revenda"),
            ("01", "Matéria-prima"),
            ("02", "Embalagem"),
            ("03", "Produto em Processo"),
            ("04", "Produto Acabado"),
            ("05", "Subproduto"),
            ("06", "Produto Intermediário"),
            ("07", "Material de Uso e Consumo"),
            ("08", "Ativo Imobilizado"),
            ("09", "Serviços"),
            ("10", "Outros insumos"),
            ("99", "Outras"),
        ],
        string="Tipo Fiscal",
    )

    @api.onchange("cst_icms")
    def _onchange_cst_icms(self):
        """ Atualiza automaticamente o fiscal_type com base nos dois últimos dígitos do CST ICMS """
        if self.cst_icms and self.cst_icms.code:
            last_two_digits = self.cst_icms.code[-2:]  # Pega os últimos dois dígitos do CST
            mapping = self.env["l10n_br_fiscal.cst_icms_mapping"].search(
                [("cst_icms_code", "=", last_two_digits)], limit=1
            )
            if mapping:
                self.fiscal_type = mapping.fiscal_type
            else:
                self.fiscal_type = False  # Reseta caso não encontre um mapeamento
