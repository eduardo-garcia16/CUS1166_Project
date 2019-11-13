from flask_sqlalchemy import current_app
from app import db

class ManagingCourse(db.Model):
    __tablename__ = "managing_course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    studentsEnrolled = db.Column(db.Integer, primary_key=True)

    teachers = db.relationship("Teacher", backref = "courses", lazy = True)
    students = db.relationship("Student", backref= "courses", lazy = True)

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    student_number = db.Column(db.Integer, primary_key = True)

    def add_student(self, name):
        new_student = student(name=name)
        db.session.add(new_student)
        db.session.commit()

    def remove_student(self, name):
        old_student = student(name=name)
        db.session.remove(old_student)
        db.session.commit()

class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

    def add_teacher(self, name):
        new_teacher = Teacher(name=name)
        db.session.add(new_teacher)
        db.session.commit()

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
