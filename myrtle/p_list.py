from typing import List

def parse(input_list) -> List[int]:
    res = []
    def p_list(int_list):
        for e in int_list:
            if isinstance(e, int):
                res.append(e)
            else:
                p_list(e)
    p_list(input_list)
    return res

def yield_parse(input_list) -> List[int]:
    def p(int_list):
        for e in int_list:
            if isinstance(e, int):
                yield e
            p(e)

    return [x for x in p_list(input_list)]

def p_list(input_elem) -> List[int]:
    if isinstance(input_elem, int):
        return [input_elem]

    res = []
    for elem in input_elem:
        res += p_list(elem)

    return res
