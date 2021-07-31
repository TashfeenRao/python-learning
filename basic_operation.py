from Models import db, Puppy, Toy, Owner

jadugar = Puppy("jadugar", 3)
mircho = Puppy("mircho", 6)

db.session.add_all([jadugar, mircho])
db.session.commit()

print(Puppy.query.all())
