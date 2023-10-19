from django import template

register = template.Library()


@register.filter()
def censor(value):
    banned_list = ['idiot', 'stupid']
    sentence = value.split()
    for i in banned_list:
        for words in sentence:
            if i in words:
                pos = sentence.index(words)
                sentence.remove(words)
                sentence.insert(pos, f"{words[0]}"+'*' * (len(i)-1))
    return " ".join(sentence)
