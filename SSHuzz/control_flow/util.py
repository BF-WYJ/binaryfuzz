import re


def is_valid_line(line: str):
    if not line.strip():
        return False
    black_list = ['Disassembly', 'file format', '...', '=']
    for item in black_list:
        if item in line:
            return False
    return True


def action(line: str):
    reg_exp = r'.*\t(\w+)\s?'
    match_obj = re.match(reg_exp, line)
    if not match_obj:
        print(f"[-]: warning! unable to recognize {line}")
        return 'None'
    return match_obj.group(1)
    
