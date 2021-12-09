import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["node-app"]

print(myclient.list_database_names())

## Kayit Ekleme

mycollections = mydb["products"]

print(mydb.list_collection_names())

product = {"name" : "Samsung S5" , "price" : 2000}

result = mycollections.insert_one(product)

print(result)
print(type(result))

# Birden fazla kayit ekleme

product_list = [{"name" : "Samsung S6" , "price" : 2000},{"name" : "Samsung S7" , "price" : 3000},
                {"name" : "Samsung S8" , "price" : 4000},{"name" : "Samsung S9" , "price" : 5000},
                {"name" : "Samsung S10" , "price" : 6000},{"name" : "Samsung S11" , "price" : 7000}]

result = mycollections.insert_many(product_list)

print(result.inserted_ids)

#ek özellikle kaydetme

product_list = [{"name" : "Samsung S6" , "price" : 2000 , "description" : "good"},
                {"name" : "Samsung S7" , "price" : 3000 , "categories" : ["phone" , "electronic"]}]

result = mycollections.insert_many(product_list)

print(result.inserted_ids)

## Kayıt Seçme

#tek bir tanesini getirmek için
bul = mycollections.find_one()
print(bul)

#hepsini getirmek için
for i in mycollections.find():
    print(i)

#belirli kritere göre getirme (where işlemi)
for i in mycollections.find({} , {"_id":0 ,"name":1 , "price":1}):
    print(i)

### Filtreleme

filter = {"name" : "Samsung S5"}
result = mycollections.find_one(filter)
print(result)

#filter içinde fazladan olsaydı döngü ile çeğıracaktık
result = mycollections.find(filter)
for i in result:
    print(i)

bul = mycollections.find_one({"_id" : ObjectId("61b1794cd7a4b4d6634da9f9")})
print(bul)

result = mycollections.find({
    "name" : {
        "$in" : ["Samsung S5" , "Samsung S6"]
    }
})
for i in result:
    print(i)

#fiyatı 2000 den fazla olan  //// $gte : büyük ve eşit //// $eq : eşit olanları getir  // $lt;$lte : küçük ; küçük ve eşit
result = mycollections.find({
    "price" : {
        "$gt" : 2000
    }
})
for i in result:
    print(i)

# kayıt içinde S ile başlayanları getir
result = mycollections.find({
    "name" : {
        "$regex" : "^S"
    }
})
for i in result:
    print(i)

## Sıralama

result = mycollections.find().sort("price" , 1) # -1 ile tersten sıralama yaparız
for i in result:
    print(i)

result = mycollections.find().sort([("price" , 1) , ("name" , -1)]) # -1 ile tersten sıralama yaparız
for i in result:
    print(i)

## Kayıt Güncelleme

for i in mycollections.find():
    print(i)
print("-" * 25)

mycollections.update_one({"name" : "Samsung S5"} ,
                         {"$set" : {"name" : "Iphone 6"}})

for i in mycollections.find():
    print(i)

for i in mycollections.find():
    print(i)
print("-" * 25)

mycollections.update_one({"name" : "Samsung S6"} ,
                         {"$set" : {"name" : "Iphone 8" , "price" : 6500}})

for i in mycollections.find():
    print(i)

for i in mycollections.find():
    print(i)
print("-" * 25)

mycollections.update_many({"name" : "Samsung S7"} ,
                         {"$set" : {"name" : "Iphone 12" , "price" : 12000}})

for i in mycollections.find():
    print(i)

query = {"name" : "Samsung S10"}

new_values = {"$set" : {"name" : "Iphone 13" , "price" : 13000}}

result = mycollections.update_many(query , new_values)

print(f'{result.modified_count} adet kayıt güncellendi.')

## Silme

for i in mycollections.find():
    print(i)
print("-" * 25)

mycollections.delete_one({"name" : "Samsung S11"})

for i in mycollections.find():
    print(i)

for i in mycollections.find():
    print(i)
print("-" * 25)

mycollections.delete_many({"name" : {"$regex" : "^S"}})

for i in mycollections.find():
    print(i)

#tamamını silmek için
result = mycollections.delete_many({})
print(f'{result.deleted_count} adet kayıt silindi.')

