def star_args(*star_name):
    print(star_name)


def simple_args(simple_name):
    print(simple_name)


def tuple_dic_args(*tuple_args, **dic_args):
    """
    >>> tuple_dic_args()
    * : <class 'tuple'>
    **:  <class 'dict'>
    """
    print("* :", type(tuple_args))
    print("**: ", type(dic_args))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
