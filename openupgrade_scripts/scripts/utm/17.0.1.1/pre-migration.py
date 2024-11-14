# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr,
        """
        ALTER TABLE utm_campaign
        ADD COLUMN IF NOT EXISTS active BOOLEAN
        """,
    )
    openupgrade.logged_query(
        env.cr,
        """UPDATE utm_campaign
        SET active = True
        """,
    )
