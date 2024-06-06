from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return f"<Role {self.name}>"


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    reports = db.relationship("Report", backref="user", lazy="dynamic")
    health = db.relationship(
        "Health", backref="user", uselist=False
    )  # Each user has one health record
    daily_activities = db.relationship(
        "GeneralActivity", secondary="user_daily_activity", backref="users"
    )

    def __repr__(self):
        return f"<User {self.email}>"

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class GeneralActivity(db.Model):
    __tablename__ = "general_activities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f"<GeneralActivity {self.name}>"


class UserDailyActivity(db.Model):  # Association table for User and GeneralActivity
    __tablename__ = "user_daily_activity"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    general_activity_id = db.Column(
        db.Integer, db.ForeignKey("general_activities.id"), primary_key=True
    )


class Report(db.Model):
    __tablename__ = "reports"
    id = db.Column(db.Integer, primary_key=True)
    bmi = db.Column(db.Float)
    daily_streak = db.Column(
        db.String(128)
    )  # corrected typo from 'daily_strick' to 'daily_streak'
    progress = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"<Report for user_id {self.user_id}>"


class Health(db.Model):
    __tablename__ = "health"
    id = db.Column(db.Integer, primary_key=True)
    blood_pressure = db.Column(db.String(64))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    bmi = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"<Health for user_id {self.user_id}>"
