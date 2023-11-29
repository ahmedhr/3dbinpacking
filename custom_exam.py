# Let's use the simple example provided in the README to demonstrate the usage of the 3D bin packing library.
# The example initializes a bin and multiple items with different dimensions and properties,
# then uses the packer to pack these items into the bin.

from py3dbp import Packer, Bin, Item

# Initialize the packer
packer = Packer()

# Initialize a bin
box = Bin('example', (30, 10, 15), 99, 0)
packer.addBin(box)

# Initialize and add items
items = [
    Item('test1', 'test', 'cube', (9, 8, 7), 1, 1, 100, True, 'red'),
    Item('test2', 'test', 'cube', (4, 25, 1), 1, 1, 100, True, 'blue'),
    Item('test3', 'test', 'cube', (2, 13, 5), 1, 1, 100, True, 'gray'),
    Item('test4', 'test', 'cube', (7, 5, 4), 1, 1, 100, True, 'orange'),
    Item('test5', 'test', 'cube', (10, 5, 2), 1, 1, 100, True, 'lawngreen'),
]

for item in items:
    packer.addItem(item)

# Perform the packing
packer.pack(
    bigger_first=True,
    fix_point=True,
    distribute_items=True,
    check_stable=True,
    support_surface_ratio=0.75,
    number_of_decimals=0
)

# Retrieve the results
bins = packer.bins
unfit_items = packer.unfit_items

# Displaying the packed items and their positions in the bin
for b in bins:
    print(f"Bin: {b.partno}")
    for item in b.items:
        print(f"Item: {item.partno}, Position: {item.position}, Rotation: {item.rotation}, Dimensions: {item.get_dimension()}")

# Displaying the unfit items
print("Unfit Items:")
for item in unfit_items:
    print(f"Item: {item.partno}, Dimensions: {item.get_dimension()}")
