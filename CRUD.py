from index import db, Puppy

################## Create ##################

adrak = Puppy('adrak', 3)
db.session.add(adrak)
db.session.commit()

################### Read ###################

data = Puppy.query.all()
print(data)

################### Edit ####################

item = Puppy.query.get(1)
item.name = 'updated'
db.session.add(item)
db.session.commit()

#################### Delete ####################

deleted_item = Puppy.query.get(2)
db.session.delete(deleted_item)
db.session.commit()

##################### check changes ################

all_puppies = Puppy.query.all()
print(all_puppies)
