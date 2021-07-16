from index import db, Puppy

db.create_all()

jugnu = Puppy('jugnu', 2)
kamu = Puppy('kamu', 4)

print(jugnu.id)
print(kamu.id)

db.session.add_all([jugnu, kamu])

db.session.commit()

print(jugnu.id)
print(kamu.id)
