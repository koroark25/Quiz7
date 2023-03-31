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

print(count_hashtag("My number is ###"))
