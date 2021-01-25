from anytree import Node,RenderTree
import csv



with open("D:\\EAI\\Parent Child\\feed file.csv","r") as access_csv:
    #reader = csv.DictReader(access_csv)
    reader = csv.reader(access_csv)
    dict_list = []
    ids=[]
    pids=[]
    relation_dict = dict()
    for line in reader:
        dict_list.append(line)
        relation_dict[line[0]]= line[1]
        ids.append(line[0])
        pids.append(line[1])
Root = Node("Root")
sample=[]
tree_ids =[]
tree_pids =[]

for i in ids:
    tree_ids.append(Node(i))
    #tree_ids[ids.index(i)] = Node(i)
set_pids = set(pids)
#print(set_pids)
#print(relation_dict)

pids_dict = dict()
for i in set_pids:
    pids_dict[i] =  Node(i)
    tree_pids.append(pids_dict[i])
    #tree_pids[pids.index(i)] = Node(i)
ultimate_tree =[]

#print(pids_dict)

for i in tree_ids:
    ultimate_tree.append(Node(i,parent=pids_dict.get(relation_dict.get(i.name))))

#print(ultimate_tree)

# for i in tree_pids:
#     for pre, fill, node in RenderTree(i):
#         print("%s%s" % (pre, node.name))

# for pre, fill, node in RenderTree(ultimate_tree):
#     print("%s%s" % (pre, node.name))

# print(pids)


tree_pids[0].parent = Root

for pre, fill, node in RenderTree(Root):
    print("%s%s" % (pre, node.name))


#final_tree =

