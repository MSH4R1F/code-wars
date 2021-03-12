def top_3_words(text):
    from collections import Counter

    import re
    if re.search('[a-zA-Z]', text) == None:
        return []
    words = re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower()))
    c = Counter()
    for x in words:
        c[x] += 1
    return [x[0] for x in c.most_common(3)]
