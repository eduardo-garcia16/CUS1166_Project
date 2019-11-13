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
    class Testbank(db.Model):
    tablename = "Testbank"
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    quesion_id = db.Column(db.Integer, db.ForeignKey('test.id'))
        t = Test(question_owner='teacher', question_type='cloned', question_id='1', test_id='1')
        t.save()
        t = Test(question_owner='teacher', question_type='cloned', question_id='2', test_id='1')
        t.save()
        t = Test(question_owner='teacher', question_type='cloned', question_id='3', test_id='1')
        t.save()
        new_test = q.test_set.create(test_id="Our first test")

class Questionbank(db.model):
    tablename = "Questionbank"
    id = db.Column(db.Integer, primary_key = True)
    questions = db.Column(db.String, nullable=False)
    answers = db.Column(db.String, nullable=False)
    testbank = db.relationship("Questionbank", backref="Testbank", lazy=True)
    question_owner = db.CharField(max_length=30)
    question_type = db.CharField(max_length=30)
    question_id = db.CharField(max_length=30)
    def __str__(self):
        return "%s %s" % (self.question_type, self.question_owner)
        q = Question(question_owner='cc', question_type='global', question_id='1')
        q.save()
        q2 = Question(question_owner='cc', question_type='global', question_id='2')
        q2.save()
        q3 = Question(question_owner='cc', question_type='global', question_id='3')
        q3.save()

class teacherUser(db.Model):
    __tablename__ = 'teacherUsers'
    username = db.Column(db.String, index=False, unique=True, nullable=False)
    email = db.Column(db.String,index=True, unique=True, nullable=False)
    bio = db.Column(db.Text, index=False, unique=False, nullable=True)
    def __repr__(self):
        return '<User {}>'.format(self.username)
