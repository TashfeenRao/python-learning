from Models import db, Puppy, Toy, Owner

jadugar = Puppy("jadugar", 3)
mircho = Puppy("mircho", 6)

db.session.add_all([jadugar, mircho])
db.session.commit()

print(Puppy.query.all())

mircho = Puppy.query.filter_by(name='mircho').first()

tashi = Owner("tashi", mircho.id)
# abc = Owner("abc", mircho.id)

toy1 = Toy("jhunjna", mircho.id)
toy2 = Toy("gubara", mircho.id)
toy3 = Toy("airplane", mircho.id)

db.session.add_all([tashi, toy1, toy2, toy3])
db.session.commit()

print(Puppy.query.all())

print(mircho.send_toys())
