from odoo import models, fields


class L10nBrFiscalCstIcmsMapping(models.Model):
    _name = "l10n_br_fiscal.cst_icms_mapping"
    _description = "Mapeamento CST ICMS para Tipo Fiscal"

    cst_icms_code = fields.Char(
        string="Código CST ICMS (Últimos 2 Dígitos)",
        required=True,
        size=2
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
        required=True,
    )

    _sql_constraints = [
        ('unique_cst_icms_code', 'unique(cst_icms_code)', 'O código CST ICMS deve ser único!')
    ]
