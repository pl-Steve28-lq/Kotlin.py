from lark import Lark

L = Lark.open('./grammar/kotlin.lark', parser='lalr')
q=L.parse

def tree(s, indent=0):
    ind = "|   "*indent
    print(f"{ind}{s.data} :")
    for i in s.children:
        if hasattr(i, 'children'): tree(i, indent+1)
        else: print(f"{ind}|   {i.type} ( {i.value} )")

genNoIncl = lambda ch: f"^({''.join(map(lambda x: f'(?!{x})', ch))}.)*$"
