# Written by Chuguan Tian for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        node = self.head
        length = 1
        index_min = 0
        min_value = node.value
        while node.next_node:
            node = node.next_node
            if node.value < min_value:
                min_value = node.value
                index_min = length
            length = length + 1

        node.next_node = self.head
        index_node_2 = (index_min - 1) % length
        node = self.head
        while index_node_2:
            node = node.next_node
            index_node_2 = index_node_2 - 1
        pre_node = node
        cur_node = self.head = pre_node.next_node
        nb_of_iterations = (length - 1) // 2
        while nb_of_iterations:
            next_pre_node = cur_node.next_node
            cur_node.next_node = pre_node
            cur_node = next_pre_node.next_node
            pre_node.next_node = cur_node
            pre_node = next_pre_node
            nb_of_iterations = nb_of_iterations - 1
        cur_node.next_node = pre_node
        pre_node.next_node = None
        # Replace pass above with your code







