"""index waze uuid

Revision ID: dfac32ad28e9
Revises: 27c808af7ccb
Create Date: 2020-10-19 15:38:49.071135

"""

# revision identifiers, used by Alembic.
revision = 'dfac32ad28e9'
down_revision = '27c808af7ccb'
branch_labels = None
depends_on = None

from alembic import op


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_waze_alerts_uuid'), 'waze_alerts', ['uuid'], unique=True)
    op.create_index(op.f('ix_waze_trafic_jams_uuid'), 'waze_trafic_jams', ['uuid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_waze_trafic_jams_uuid'), table_name='waze_trafic_jams')
    op.drop_index(op.f('ix_waze_alerts_uuid'), table_name='waze_alerts')
    # ### end Alembic commands ###
