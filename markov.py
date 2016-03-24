def chain(text):
    map = {}
    words = text.split()
    for i in range(0, len(words) - 1):
        w = words[i]
        n = words[i + 1]
        if w not in map:
            map[w] = {}
        map[w][n] = map[w].get(n, 0) + 1
    return map