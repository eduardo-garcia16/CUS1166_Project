from app.main import bp



@app.route('/item/<int:id>', methods=['GET', 'POST'])
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
        return render_template('edit_test.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
