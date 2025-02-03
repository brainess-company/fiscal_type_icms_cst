{
    "name": "Mapeamento CST ICMS para Tipo Fiscal",
    "summary": "Relaciona os últimos 2 dígitos do CST ICMS ao Tipo Fiscal dos produtos",
    "version": "14.0.1.0.0",
    "category": "Accounting",
    "author": "Seu Nome ou Empresa",
    "license": "AGPL-3",
    "website": "https://github.com/seu-repositorio",
    "depends": ["l10n_br_fiscal", "product"],
    "data": [
        "views/cst_icms_mapping_views.xml",
        "views/product_template_views.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "application": False,
}
