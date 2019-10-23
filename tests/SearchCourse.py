class SearchCourse(course):

course_id = request.form.get('id_field')
course_name = request.form.get('name_field')
course_content = request.form.content('content_field')

try:
    course = create_course(course_id, course_name, course_content)
    return render_template('add.html', course=course)
except Exception as e:

  course = course.query.get(id)

  if request.method == 'Get':
    return render_template('add.html', course = course, error = "Course ID Does Not Exist! Please Try Again.")
