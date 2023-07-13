p=[
    {"name":"j","house":"los vegas"},
    {"name":"mj","house":"ny"},
    {"name":"sd","house":"los angels"}
    ]

def p1(p):
    return p["name"]

p.sort(key=p1)
print(p)