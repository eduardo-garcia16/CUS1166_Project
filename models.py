from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_table import Table, Col, LinkCol

class course(db.model):
    __tablename__ = "course"
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)
    course_content = db.Column(db.String, nullable=False)

class student(db.model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

    def add_student(self, name):
        new_student = student(name=name)
        db.session.add(new_student)
        db.session.commit()


class teacher(db.model):
    __tablename__ = "teacher"
    teacher_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

    def add_teacher(self, name):
        new_teacher = teacher(name=name)
        db.session.add(new_teacher)
        db.session.commit()

    student = db.relationship("student", backref="course", lazy=True)
    teacher = db.relationship("teacher", backref="course", lazy=True)

class contentcreator(db.model):
    __tablename__ = "content creator"
    contentcreator_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


    def add_contentcreator(self,name):
        new_contentcreator = contentcreator(name=name)
        db.session.add(new_contentcreator)
        db.session.commit()

class teacherUser(db.Model):
    __tablename__ = 'teaacherUsers'
    username = db.Column(db.String, index=False, unique=True, nullable=False)
    email = db.Column(db.String,index=True, unique=True, nullable=False)
    bio = db.Column(db.Text, index=False, unique=False, nullable=True)
    def __repr__(self):
        return '<User {}>'.format(self.username)


class globaltestbank(db.model):
    __tablename__ = "globaltestbank"
    questions = db.Column(db.String, nullable=False)
    answers = db.Column(db.String, nullable=False)
    testbank = db.relationship("testbank", backref="teacher", lazy=True)
    testbank = db.relationship("testbank", backref="contentcreator", lazy=True)

class teachertestbank(db.model):
    __tablename__ = "teachertestbank"
    questions = db.Column(db.String, nullable=False)
    answers = db.Column(db.String, nullable=False)
    testbank = db.relationship("testbank", backref="teacher", lazy=True)
    testbank = db.relationship("testbank", backref="contentcreator", lazy=True)
