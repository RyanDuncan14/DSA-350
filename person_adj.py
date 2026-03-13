import random

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last 
        self.sid = random.randint(1000, 9999)
        self.friend_num = 0
    
    def name(self):
        return self.first + " " + self.last
    
    def num_friends(self, n):
        self.friend_num = n

    def __str__(self):
        return f"{self.name()} ({self.sid})"

    
def build_adj(data):
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

    for key in adj_dict:
        key.num_friends(len(adj_dict[key]))

    return adj_dict

def display_adj(adj_dict):
    for key, val in adj_dict.items():
        print(f"{key.sid}: {key.name()}, number of friends: {key.friend_num}")
        for person in val:
            print(f"  {person}")
        
if __name__ == '__main__': 
    p1 = Person("Anita", "Racinez")
    p2 = Person("Clem", "Jameson")
    p3 = Person("Lars", "Eriksson")
    p4 = Person("Jed", "Jones")
    data = [(p1, p2), (p2, p3), (p1, p4), (p2, p4)]
    print("hi")
    display_adj(build_adj(data))