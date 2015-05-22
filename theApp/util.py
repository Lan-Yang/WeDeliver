DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULE_PER_PAGE = 4

def djb2_string_hash(social_id):
    """ See for details: http://www.cse.yorku.ca/~oz/hash.html """
    _hash = 5381
    for i in xrange(0, len(social_id)):
       _hash = ((_hash << 5) + _hash) + ord(social_id[i])
    return _hash%2147483647