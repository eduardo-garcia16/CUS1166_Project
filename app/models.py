from flask_sqlalchemy import current_app
from app import db

class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    teachers = db.relationship("Teacher", backref = "courses", lazy = True)
    students = db.relationship("Student", backref= "courses", lazy = True)

    def add_teacher(self, name):
        new_teacher = Teacher(name=name)
        db.session.add(new_teacher)
        db.session.commit()

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

    def add_student(self, name):
        new_student = student(name=name)
        db.session.add(new_student)
        db.session.commit()


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

class ContentCreator(db.Model):
    __tablename__ = "content_creators"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def add_contentcreator(self,name):
        new_contentcreator = contentcreator(name=name)
        db.session.add(new_contentcreator)
        db.session.commit()

    def add_question(self, question, answer):
        new_question = Testbank(questions = question, answers = answers, author = self.id)
        db.session.add(new_question)
        db.session.commit()

class Testbank(db.Model):
    __tablename__ = "testbank"
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)

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
