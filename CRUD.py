from index import db, Puppy

################## Create ##################

adrak = Puppy('adrak', 3)
db.session.add(adrak)
db.session.commit()

################### Read ###################

all_puppies = Puppy.query.all()
print(all_puppies)

################### Edit ####################

item = Puppy.query.get(1)
item.name = 'kamkhua'
db.session.add(item)
db.session.commit()

#################### Delete ####################

deleted_item = Puppy.query.get(2)
db.session.delete(deleted_item)
db.session.commit()

##################### check changes ################

all_puppies = Puppy.query.all()
print(all_puppies)
