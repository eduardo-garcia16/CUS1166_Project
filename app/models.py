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

    results = db.relationship("Results", backref = "students", lazy=True)


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
        new_question = Testbank(questions = question, answers = answers, author = self.name)
        db.session.add(new_question)
        db.session.commit()

class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)

    tests = db.relationship("Tests", backref="questions", lazy=True)

class Test(db.Model):
    __tablename__ = "tests"
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)

    results = db.relationship("Results", backref = "tests", lazy=True)

class Result(db.Model):
    __tablename__ == "results"
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String, nullable=False)
    student_name = db.Column(db.String, db.ForeignKey('students.name'), nullable=False)
    questions_id = db.Column(db.Integer, db.ForeignKey('tests.question_id'), nullable=False)
