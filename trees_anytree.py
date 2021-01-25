from anytree import Node,RenderTree

udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jet1 = Node("Jet1", parent=jet)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)
sudhan = Node("sudhan")


# for pre, fill, node in RenderTree(sudhan):
#     print("%s%s" % (pre, node.name))

sudhan.parent = udo
# print(sudhan.path)
for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))
print(jet)