def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

def reverse_words(s):
    words = s.split(' ')
    if len(words) == 0:
        return s
    else:
        return ' '.join(reverse_words(words[1:]) + ' ' + words[0] if words[1:] else words[0])
