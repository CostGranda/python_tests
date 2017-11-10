def palindroma(palabra):
    """
    >>> palindroma('algo')
    error
    >>> palindroma('Amor a Roma')
    Amor a Roma
    >>> palindroma('Amar da drama')
    Amar da drama
    """
    if(palabra.lower().replace(' ', '') == palabra[::-1].lower().replace(' ', '')):
        print(palabra)
    else:
        print("error")
