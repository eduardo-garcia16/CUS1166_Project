# import the name of the database
from app import db
from app.models import User, Post

db.session.add(u)
db.session.commit()

# change to the name of table containing the questions
users = User.query.all()
 users

 #Print out questions based off database
 [<User john>, <User susan>]
 for u in users:
  print(u.id, u.username)
