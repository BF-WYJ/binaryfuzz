import re


def is_valid_line(line: str):
    """
    从原始的objdump获取的文件中有许多无效信息, 需要对它进行过滤
    :param line:  需要处理的行
    :return:      该行是否有效
    """

    if not line.strip():
        return False
    black_list = ['Disassembly', 'file format', '...', '=']
    for item in black_list:
        if item in line:
            return False
    return True


def action(line: str):
    """
    解析一个汇编指令的具体动作, 例如call, jmp, ret等
    :param line: 要解析的汇编指令
    :return: 具体动作
    """

    reg_exp = r'.*\t(\w+)\s?'
    match_obj = re.match(reg_exp, line)
    if not match_obj:
        print(f"[-]: warning! unable to recognize {line}")
        return 'None'
    return match_obj.group(1)
    
