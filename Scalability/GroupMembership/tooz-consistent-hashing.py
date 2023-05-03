from tooz import hashring

NUMBER_OF_NODES = 16

hr = hashring.HashRing(["node%d" % i for i in range(NUMBER_OF_NODES)])
nodes = hr.get_nodes(b"some data")
print(nodes)
nodes = hr.get_nodes(b"some data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some other data", replicas=3)
print(nodes)
nodes = hr.get_nodes(b"some other of my data", replicas=2)
print(nodes)
## Output:
# {'node8'}
# {'node8', 'node11'}
# {'node6', 'node2', 'node13'}
# {'node8', 'node7'}


hr.remove_node("node8")
nodes = hr.get_nodes(b"some data")
print(nodes)
nodes = hr.get_nodes(b"some data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some other data", replicas=3)
print(nodes)
nodes = hr.get_nodes(b"some other of my data", replicas=2)
print(nodes)
## Output:
# Removing node8
# {'node11'}
# {'node6', 'node11'}
# {'node6', 'node2', 'node13'}
# {'node5', 'node7'}


print("Adding node17")
hr.add_node("node17")
nodes = hr.get_nodes(b"some data")
print(nodes)
nodes = hr.get_nodes(b"some data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some other data", replicas=3)
print(nodes)
nodes = hr.get_nodes(b"some other of my data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some data that should end on node17", replicas=2)
print(nodes)
## Output:
# Adding node17
# {'node11'}
# {'node6', 'node11'}
# {'node6', 'node2', 'node13'}
# {'node5', 'node7'}
# {'node17', 'node9'}



print("Adding back node8 with weight")
hr.add_node("node8", weight=100)

nodes = hr.get_nodes(b"some data")
print(nodes)
nodes = hr.get_nodes(b"some data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some other data", replicas=3)
print(nodes)
nodes = hr.get_nodes(b"some other of my data", replicas=2)
print(nodes)
## Output:
# Adding back node8 with weight
# {'node8'}
# {'node11', 'node8'}
# {'node2', 'node8', 'node6'}
# {'node8', 'node7'}