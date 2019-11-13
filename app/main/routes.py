import sys
from flask import Flask, render_template, current_app, request
from app import db, create_app
from app.main import bp

@bp.route("/")
def index():
    #courses = Course.query.all()
    return render_template('base.html')

@bp.route("/view_classes")
def view_classes():
    classes = request.form.get("classes")

    view_classes = Testbank(view_classes = view_classes)
    db.session.delete(view_classes)
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

@dp.route("/remove_course", methods = ["post"])
def remove_course():
    course_name = request.form.get("course_name")
    course_content = request.form.get("course_content")

    course = Course(course_name = course_name, course_content = course_content)
    db.session.remove(course)
    db.session.commit()

    course = Course.query.all()
    return render_template("index.html", courses = courses)

@bp.route("/cc/add_topic", methods = ["post"])
def add_topic():
    topic = request.form.get("topic")
    author = request.form.get("author")

    topic = Testbank(topic = topic, author = author)
    db.session.add(topic)
    db.session.commit()

    topic = Testbank.query.all()
    return render_template('testbank.html', testbank = questions)

@bp.route("/contact", methods=["GET", "POST"])
def contact(form):
  if request.method == "POST":
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(subject, sender=sender, recipients=recipients])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('contact.html', success=True)

  elif request.method == "GET":
    return render_template('contact.html', form=form)

@dp.route("/remove_topic")
def remove_topic():
    topic = request.form.get("topic")
    author = request.form.get("author")

    topic = ContentCreator(topic = topic, author = author)
    db.session.remove(topic)
    db.session.commit()

    return render_template("remove_topic.html")
  
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
