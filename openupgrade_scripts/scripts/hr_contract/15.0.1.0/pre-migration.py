from openupgradelib import openupgrade

_columns_copy = {
    "hr_contract": [
        ("notes", None, None),
    ],
}

_model_renames = [
    ("hr.contract.history", "hr.contract.history_table"),
]

_table_renamed = [
    ("hr_contract_history", "hr_contract_history_table"),
]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.copy_columns(env.cr, _columns_copy)

    # Se hace esto porque en los custom de BPS ya existe este modelo, entonces se pasa para otro y asi evitar conflicto con Odoo
    openupgrade.rename_models(env.cr, _model_renames)
    openupgrade.rename_tables(env.cr, _table_renamed)
