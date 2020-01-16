import pymongo


def insertData():
    client = pymongo.MongoClient(
        'localhost', 27017
    )
    db = client.get_database("tnidatabase")
    # .insert_one, .insert_many
    # rs = db.students.insert_one({'id': '188888655443', 'name': 'Seeya'})
    # print('{}'.format(rs.inserted_id))

    rs = db.students.insert_many([{'id': '4460', 'name': 'Gigabute'},
                                  {'id': '9700', 'name': 'Hayate'},
                                  {'id': '18500400', 'name': 'Maybeline'}])
    print('{}'.format(rs.inserted_ids))
    for e in rs.inserted_ids:
        print('{}'.format(e))


def select_data():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.get_database("MobileShop")
    rs = db.Products.find({'pprice': {'$gt': 20000}}).sort([('pprice', pymongo.DESCENDING)])
    count = db.Products.count_documents({'pprice': {'$gt': 20000}})
    print("Found {} Record(s)".format(count))
    for e in rs:
        print("{} - {} - {}".format(e['pid'], e['pname'], e['pprice']))


def select_data2():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.get_database("MobileShop")
    start_price = int(input("Start price : "))
    end_price = int(input("End price : "))
    rs = db.Products.find({'$and': [{'pprice': {'$gt': start_price}}, {'pprice': {'$lt': end_price}}]}) \
        .sort([('pprice', pymongo.DESCENDING)])
    for y, e in enumerate(rs):
        print("{}.{} - {}".format(y + 1, e['pname'], e['pprice']))


if __name__ == '__main__':
    # insertData()
    # select_data()
    select_data2()
