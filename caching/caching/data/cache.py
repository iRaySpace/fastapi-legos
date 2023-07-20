import redis


def redisified(fn):
    def get_fn():
        r = redis.Redis(host='172.28.128.1', port=6379, db=0)
        redis_data = r.hgetall("data")
        if redis_data:
            return redis_data
        fn_data = fn()
        r.hset("data", fn_data)
        return fn_data
    return get_fn
