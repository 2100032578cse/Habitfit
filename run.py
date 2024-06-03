import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role, GeneralActivity, Report, Health

config_name = os.getenv("FLASK_CONFIG") or "default"
app = create_app(config_name)

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        User=User,
        Role=Role,
        GeneralActivity=GeneralActivity,
        Report=Report,
        Health=Health,
    )


if __name__ == "__main__":
    app.run()
