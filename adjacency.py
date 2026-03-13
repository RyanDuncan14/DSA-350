def build_adjacency(data):
    adj_dict = dict()
    for node in data:
        a = node[0]
        b = node[1]
        if a in adj_dict:
            adj_dict[a].append(b)
        else:
            adj_dict[a] = [b]
        if b in adj_dict:
            adj_dict[b].append(a)
        else:
            adj_dict[b] = [a]
    return adj_dict

def display_adj(adj_dict):
    for key, val in adj_dict.items():
        print(f"{key}: {val}")
        
if __name__ == '_main_': 
    data = [("dan", "bob"), ("bob", "clem"), ("clem", "anita"), ("anita", "bob")]
    display_adj(build_adjacency(data))