import hashlib


def generator_hash(file):
    with open(file, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for elem in lines:
            line = elem.rstrip()
            hash_object = hashlib.md5(line.encode())
            yield hash_object.hexdigest()
