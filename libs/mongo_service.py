from pymongo import MongoClient


class MongoService(object):

    client = None
    db = None

    @classmethod
    def init(cls, db_name):
        cls.client = MongoClient('mongodb://localhost:27017/')
        cls.db = cls.client[db_name]

    @classmethod
    def healthcheck(cls):
        try:
            cls.client.server_info()
            return True
        except Exception as e:
            return False

    @classmethod
    def set_db(cls, name):
        cls.db = cls.client[name]

    @classmethod
    def close(cls):
        cls.client.close()

    @classmethod
    def create_index(cls, collection_name, index_name):
        cls.db[collection_name].create_index(index_name, unique=True)

    @classmethod
    def insert(cls, name, data):
        cls.db[name].insert_one(data)

    @classmethod
    def insert_many(cls, collection_name, data):
        cls.db[collection_name].insert_many(data)

    @classmethod
    def query(cls, collection_name, search=None, limit=10, page=1, order=-1):
        if search is None:
            search = {}
        filter_params = {"_id": 0}
        if limit == 0:
            res = cls.db[collection_name].find(search, filter_params).sort("_id",
                                                                           order)
        else:
            res = cls.db[collection_name].find(search, filter_params).sort("_id",
                                                                           order).skip(
                (page - 1) * limit).limit(limit)
        array = list(res)
        return array

    @classmethod
    def get_all(cls, collection_name):
        res = cls.db[collection_name].find({}, {'_id': False})
        array = list(res)
        return array

    @classmethod
    def query_one(cls, collection_name, search):
        filter_params = {"_id": 0}
        res = cls.db[collection_name].find_one(search, filter_params)
        return res

    @classmethod
    def delete_one(cls, collection_name, q):
        cls.db[collection_name].delete_one(q)

    @classmethod
    def update_one(cls, collection_name, q, new_val):
        cls.db[collection_name].update_one(q, new_val)

    @classmethod
    def count(cls, collection_name, search):
        if search is not None:
            res = cls.db[collection_name].find(search, {"_id": 0}).count()
            return res
        else:
            res = cls.db[collection_name].find({}, {"_id": 0}).count()
            return res
