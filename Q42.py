#Katherine O'Roark
def count_hashtag(complex):
    hash = 0
    count = 0
    while count < len(complex):
        if complex[count] == '#':
            hash+=1
            count+=1
        else:
            count+=1
    return hash

def hash_spam(str):
    h = count_hashtag(str)
    if h >= 4:
        return "this tweet will be considered as a spam!"
    else:
        return None

print(hash_spam("My number is ###"))
print(hash_spam("My number is ### ### ####"))
