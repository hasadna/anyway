from flask_login import current_user

from anyway.app_and_db import db
from anyway.models import UserOAuth


def get_current_user_email():
    cur_id = current_user.get_id()
    cur_user = (
        db.session.query(UserOAuth)
        .with_entities(UserOAuth.email)
        .filter(UserOAuth.id == cur_id)
        .first()
    )
    if cur_user is not None:
        return cur_user.email
    return None