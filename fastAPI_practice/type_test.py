def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    upper_first_name = first_name.upper()
    return full_name


print(get_full_name("john", "doe"))