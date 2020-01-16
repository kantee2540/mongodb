import pymongo


def insert_to_mongodb_web():
    client = pymongo.MongoClient(
        "mongodb+srv://kantee2540:Kant2540@cluster0-ww6d1.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("MobileShop")
    #rs = db.Products.insert_one({'pid': 'p009', 'pname': 'x500', 'pbrand': 'LG', 'pprice': 2500, 'psize': 5.5})
    #print(f'{rs.inserted_id}')
    mobile_data = [{"pid": "p002", "pname": "A83 (2018)", "pbrand": "OPPO", "pprice": 7800, "psize": 5.7},
                   {"pid": "p003", "pname": "Motion", "pbrand": "BlackBerry", "pprice": 9000, "psize": 4.5},
                   {"pid": "p004", "pname": "V11i", "pbrand": "Vivo", "pprice": 8990, "psize": 6.3},
                   {"pid": "p005", "pname": "X20  Plus UD", "pbrand": "Vivo", "pprice": 12000, "psize": 6.11}]
    rs = db.Products.insert_many(mobile_data)
    print("Inserted Data")


def select_data_web():
    client = pymongo.MongoClient("mongodb+srv://kantee2540:Kant2540@cluster0-ww6d1.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("MobileShop")
    rs = db.Products.find({}).sort([('pid', pymongo.ASCENDING)])
    count = db.Products.count_documents({})
    print("Found {} Record(s)".format(count))
    for e in rs:
        print("{} - {} - {}".format(e['pid'], e['pname'], e['pprice']))


if __name__ == '__main__':
    #insert_to_mongodb_web()
    select_data_web()