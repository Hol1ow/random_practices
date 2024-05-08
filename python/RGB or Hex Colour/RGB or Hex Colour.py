import re

def rgb_or_hex(r:int|str, g:int=0, b:int=0) -> str|tuple:
    hexa_code = re.compile(r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')
    if type(r) is str and len(r) == 7 and bool(re.match(hexa_code, r)):
        return (int(r[1:3], 16), int(r[3:5], 16), int(r[5:7], 16))
    elif type(r) is int and 0 <= r < 256:
        return f"#{r:02x}{g:02x}{b:02x}"
    else:
        return

print(rgb_or_hex(150, 50, 76))
#"#96324c"

print(rgb_or_hex("#303749"))
#(48, 55, 73)

print(rgb_or_hex(170, 14, 0))
#"#aa0e00"