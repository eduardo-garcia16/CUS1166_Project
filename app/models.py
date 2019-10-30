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
    course_id = db.Column(db.Integer, db.ForeignKey('course_id'), nullable=False)

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
