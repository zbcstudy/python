import dbm

db = dbm.open("website", "c")
db["name"] = "zhaobicheng"
print(db["name"])
db.close
