from prettytable import PrettyTable
from typing import List, Any


def print_matrix(
    mat: List[List[Any]], header: List[Any] = None, row_name: List[Any] = None
):
    p = PrettyTable(field_names=header)
    for row in mat:
        p.add_row(row)
    if row_name:
        p.add_column("row_name", row_name)
    print(p.get_string())
