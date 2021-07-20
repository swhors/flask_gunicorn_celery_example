from lib.psql import PSQL
#from model.student import Student


psql = PSQL()

datas=(('lee', 3), ('kim', 2), ('ye', 1), ('sim', 2))

for data in datas:
    psql.insert(name=data[0], grade=data[1])

results = psql.get_all()

for result in results:
    print(result)

psql.delete_all()
