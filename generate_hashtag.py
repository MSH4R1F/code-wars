def generate_hashtag(s):
    hashtag = ''.join([x[0].upper()+x[1:].lower() for x in s.split()])
    if len(hashtag) == 0 or len(hashtag) > 140:
        return False
    return '#'+hashtag
