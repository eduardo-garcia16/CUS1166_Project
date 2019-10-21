from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_table import Table, Col, LinkCol

class course(Table):
    __tablename__ = "course"
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)
    course_content = db.Column(db.String, nullable=False)

class student(Table):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

    def add_student(self, name):
        new_student = student(name=name)
        db.session.add(new_student)
        db.session.commit()


class teacher(Table):
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

class contentcreator(Table):
    __tablename__ = "content creator"
    contentcreator_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


    def add_contentcreator(self,name):
        new_contentcreator = contentcreator(name=name)
        db.session.add(new_contentcreator)
        db.session.commit()



class testbank(Table):
    __tablename__ = "testbank"
    questions = db.Column(db.String, nullable=False)
    answers = db.Column(db.String, nullable=False)
    edit = LinkCol('Edit', 'edit' url_kwargs=dict(id='id'))
    testbank = db.relationship("testbank", backref="teacher", lazy=True)
    testbank = db.relationship("testbank", backref="contentcreator", lazy=True)
