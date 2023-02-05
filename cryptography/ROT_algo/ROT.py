import string


def rot(input_string, rot_step=13):
    """
    simple rot13
    (does consider whitespaces)
    """
    return "".join([chr(ord(c)+rot_step) for c in input_string])


def rot_to_ord(input_string, rot_step=13):
    """
    convert rot to ord sequence
    """
    return "".join([str(ord(c)+rot_step)+"/" for c in input_string])


def rot_to_ord_list(input_string, rot_step=13):
    """
    convert rot to ord_list
    """
    return list([ord(c)+rot_step for c in input_string])


print(rot_to_ord_list(string.ascii_letters))


###
def unrot(input_string, rot_step=13):
    """
    docstring
    """
    pass


def alrot(input_string):
    """
    alphabetic rot
    (leaves whitespaces unchanged)
    """
    pass
