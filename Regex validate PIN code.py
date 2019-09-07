def validate_pin(pin: str):
    if len(pin) not in [4, 6]:
        return False
    for i in pin:
        if not i.isdigit():
            return False
    return True
