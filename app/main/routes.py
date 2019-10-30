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

    exam_question = Testbank(exam_question = exam_questions)
    db.session.add(exam_question)
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

    question = Testbank(question = question, answer = answer, author = author)
    db.session.add(question)
    db.session.commit()

    questions = Testbank.query.all()
    return render_template('testbank.html', testbank = questions)

@bp.route('/cc/edit_question', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Test).filter(
                Test.id==id)
    test = qry.first()

    if test:
        form = TestForm(formdata=request.form, obj=test)
        if request.method == 'POST' and form.validate():
            save_changes(test, form)
            flash('Test updated successfully!')
            return redirect('/')
        return render_template('testbank.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

    questions = Testbank.query.all()
    return render_template('testbank.html', testbank = questions)

@bp.route('/cc/add_teacherUser', methods=['GET'])
def create_teacherUser():
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing:
        return make_response(f'{username} ({email}) already created!')
        new_user = User(username=username, email=email, created=dt.now(), bio="This is a filler bio", admin=False)
        db.session.add(new_user)
        db.session.commit()
    return make_response(f"{new_user} successfully created!")
