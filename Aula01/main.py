def replace(s, text01, texto2):
    index = 0
    while index >= 0:
        index = s.index(text01, index)
        if index != -1:
            s = s[:index] + texto2 + s [index + len(text01): ]
        index = index + len(texto2)
        return s
