from .cache import redisified

@redisified
def get():
    return {'total': _sum_of_big_numbers()}


def _sum_of_big_numbers():
    return sum([x for x in range(10_000_000)])
