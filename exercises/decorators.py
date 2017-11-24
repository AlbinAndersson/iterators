"""Övningar på decorators."""

from functools import wraps  # NoQA


def memoize(F):
    """Implementera memoization (cache).

    Detta är den enklaste typen av cache som helt enkelt lagrar alla
    returvärden för de anropsvärden som används.
    """
    pass


def rovarsprak(F):
    """Översätt utdata till rövarspråket.

    Funktionen som dekoreras kan antas returnera textsträngar. Dessa översätts
    av decoratorn till rövarspråket.
    """
    data = F()
    result = ''
    vocal = ['a', 'e', 'i', 'o', 'u', 'å', 'ä', 'ö']
    for letter in data:
        if letter.lower() in vocal:
            result = result + letter
        else:
            result = result + letter + 'o' + letter

    return lambda: result
