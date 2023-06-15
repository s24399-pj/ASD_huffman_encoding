from node import Node
from heap_node import HeapNode

class Tree:
    def __init__(self, array):
        self.roots = self.__make(array)

    def __make(self, array_of_elements):
        if len(array_of_elements) == 1:
            return array_of_elements[0]

        while len(array_of_elements) > 1:
            # Extract two smallest elements from the array
            first_head_element = array_of_elements.pop(0)
            second_head_element = array_of_elements.pop(0)

            # Create a new node
            new_node_key = first_head_element.key + second_head_element.key
            new_node_value = first_head_element.value + second_head_element.value
            new_element = Node(new_node_key, new_node_value, first_head_element, second_head_element)

            # Insert new node back into the array
            HeapNode.insert_node(array_of_elements, new_element)

        return array_of_elements[0]
