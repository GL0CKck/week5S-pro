def clear_sentence(n):
    # s = [i for i in n if i.isalpha() or i == ' ']
    # clear_sen = ''.join([i for i in n if i.isalpha() or i == ' '])
    return ''.join([i for i in n if i.isalpha() or i == ' '])


print(clear_sentence('prive12t, menya- zovut, misha.'))


def list_sentence(n: str) -> list:
    return list(n.split())


print(list_sentence(clear_sentence('prive12t, menya- zovut, misha.')))


def max_word_in_sentence(n: list):
    return max(n, key=len)


print(max_word_in_sentence(list_sentence(clear_sentence('prive12t, menya- zovut, misha.'))))


if __name__ == 'main':
    print('Main file!!!')
