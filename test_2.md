 Create a simple application that rewrites the json data structure using Section A to Section B. Please note that Section A nodes are sorted in no particular order. The "subordinate" node must be removed when no child exists (see markcorderoi and richard)
 

Answer:

import json
def convert_to_hierarchy(data):
    managers = {}
    subordinates = set()

    for item in data:
        manager = item["manager_name"]
        sub = item.get("login_name", item.get("login_name ", "")).strip()
        
        if manager not in managers:
            managers[manager] = []
        managers[manager].append(sub)
        subordinates.add(sub)
    
    roots = [m for m in managers if m not in subordinates]
    
    def build_tree(person):
        node = {"name": person}
        if person in managers:
            node["subordinate"] = [build_tree(sub) for sub in managers[person]]
        return node
    
    return [build_tree(root) for root in roots]

data = [
    {"manager_name": "nssi", "login_name": "nishanthi"},
    {"manager_name": "mbarcelona", "login_name ": "nssi"},
    {"manager_name": "nishanthi", "login_name": "markcorderoi"},
    {"manager_name": "mbarcelona", "login_name ": "richard"},
    {"manager_name": "letecia", "login_name ": "rudy"}
]

result = convert_to_hierarchy(data)
print(json.dumps(result, indent=2))