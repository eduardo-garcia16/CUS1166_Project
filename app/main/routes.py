import sys
from flask import Flask, render_template, current_app, request
from app import db, create_app
from app.main import bp

@bp.route("/")
def index():
    #courses = Course.query.all()
    return render_template('base.html')

@bp.route("/create_exam")
def create_exam():
    exam_questions = request.form.get("exam_questions")

    for questions in exam_questions:
        db.session.add(Testbank[questions])

    db.session.commit()

    return render_template('create_exam.html')

@bp.route("/view_exam")
def view_exam():
    exam_questions = request.form.get("exam_questions")

    exam_question = Testbank(exam_question = exam_questions)
    db.session.delete(exam_question)
    db.session.commit()

    return render_template('view_exam.html')

@bp.route("/add_course", methods = ["post"])
def add_course():
    course_name = request.form.get("course_name")
    course_content = request.form.get("course_content")

    course = Course(course_name = course_name, course_content = course_content)
    db.session.add(course)
    db.session.commit()

    courses = Course.query.all()
    return render_template('index.html', courses = courses)

@bp.route("/cc/add_question", methods = ["post"])
def add_question():
    question = request.form.get("question")
    answer = request.form.get("course_content")
    author = request.form.get("author")

    question = Question(question = question, answer = answer, author = author)
    db.session.add(question)
    db.session.commit()

    questions = Question.query.all()
    return render_template('testbank.html', testbank = questions)

@bp.route("/test", methods = ["post"])
def exam():
    test_id = request.form.get("test_id")

    return render_template('exam.html', test_id = test_id)

@bp.route("/test/<string:test_id>", methods = ["get"])
def take_exam(test_id):
    exists = db.session.query(Test.id).filter_by(test_id = test_id).scalar() is not None

    if exists == False:
        return redirect(url_for(exam))

    questions = Test.query.filter_by(test_id = test_id)

    return render_template('take_exam.html', questions = questions, test_id = test_id)

@bp.route("/test/<string:test_id>", methods=["post"])
def add_result():
    result = request.form.get("result")

    result = Result(result = result)
    db.session.add(result)
    db.session.commit()

    return render_template('exam.html')
