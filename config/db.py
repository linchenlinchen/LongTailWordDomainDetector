import pymysql
import redis
import urllib.parse

from config.configSys2 import config
from pymongo import MongoClient

class DB:
    def __init__(self):
        pass

    def get_mysql(self, config=config['mysql']):
        if not hasattr(self, '_mysql') or self._mysql == None or self._mysql._closed:
            self._mysql = pymysql.connect(**config)

        return self._mysql

    def get_mongo(self, config=config['mongo']):
        if not hasattr(self, '_mongo') or self._mongo == None:
            mongo_config = {k:urllib.parse.quote(v) if isinstance(v, str) else v for k, v in config.items()}

            uri = 'mongodb://{user}:{password}@{host}:{port}/{database}'.format(**mongo_config)
            print(uri)
            reg="%40"
            result=uri.replace(reg,'@')
            print(result)            
            self._mongo = MongoClient(uri)

        return self._mongo

    def get_redis(self, config=config['redis']):
        if not hasattr(self, '_redis') or self._redis == None:
            pool = redis.ConnectionPool(**config)
            self._redis = redis.Redis(connection_pool=pool)
        
        return self._redis

    def close_mysql(self):
        if hasattr(self, '_mysql') and self._mysql != None:
            self._mysql.close()
    
    def close_mongo(self):
        if hasattr(self, '_mongo') and self._mongo != None:
            self._mongo.close()

    def close_redis(self):
        if hasattr(self, '_redis') and self._redis != None:
            self._redis.connection_pool.disconnect()

    def fetch(self, sql):
        db = self.get_mysql()
        cur = db.cursor()
        rows = []
        try:
            cur.execute(sql)
            rows = cur.fetchall()
        except Exception as e:
            # logging.exception(e)
            print(e)
        finally:
            cur.close()
        return rows


    def execute(self, sqls):
        db = self.get_mysql()
        cur = db.cursor()
        try:
            for sql in sqls:
                cur.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()

    def executemany(self, sql, tup):
        db = self.get_mysql()
        cur = db.cursor()
        try:
            cur.executemany(sql, tup)
            db.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            
    def batchpop(self, key, batch_size):
        db = self.get_redis()
        lst = [x for x in [db.lpop(key) for i in range(batch_size)] if x is not None]
        return lst

    def push(self, key, value):
        db = self.get_redis()
        db.rpush(key, value)
    
    def len(self, key):
        db = self.get_redis()
        return db.llen(key)

    def close(self):
        self.close_mysql()
        self.close_mongo()
        self.close_redis()
