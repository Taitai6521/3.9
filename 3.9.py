# from typing import Any
#
#
# class Node(object):
#     def __init__(self, value: int) -> None:
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class BinarySearchTree(object):
#
#     def __init__(self) -> None:
#         self.root = None
#
#     def insert(self, value: int) -> None:
#
#         if self.root is None:
#             self.root = Node(value)
#             return
#
#         def _insert(node: Node, value: int) -> Node:
#             if node is None:
#                 return Node(value)
#             if value < node.value:
#                 node.left = _insert(node.left, value)
#             else:
#                 node.right = _insert(node.right, value)
#             return node
#
#         _insert(self.root, value)
#
#     def inorder(self) -> None:
#
#         def _inorder(node: Node) -> None:
#             if node is not None:
#                 _inorder(node.left)
#                 print(node.value)
#                 _inorder(node.right)
#
#         _inorder(self.root)
#
#     def search(self, value: int) -> bool:
#
#         def _search(node: Node, value: int) -> bool:
#             if node is None:
#                 return False
#             if node.value == value:
#                 return True
#             elif node.value > value:
#                 return _search(node.left, value)
#             elif node.value < value:
#                 return _search(node.right, value)
#
#         _search(self.root, value)
#
#     def min_value(self, node: Node) -> Node:
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current
#
#     def remove(self, value: int) -> Node:
#
#         def _remove(node: Node, value: int) -> Node:
#             if node is None:
#                 return node
#             if value < node.value:
#                 _remove(node.left, value)
#             elif value > node.value:
#                 _remove(node.right, value)
#             else:
#                 if node.left is None:
#                     return node.right
#                 elif node.right is None:
#                     return node.left
#
#                 temp = min_value(node.right)
#                 node.value = temp.value
#                 node.right = _remove(node.right, temp.value)
#             return node
#         _remove(self.root, value)
#
# if __name__ == '__main__':
#
#     binary_tree = BinarySearchTree()
#     binary_tree.insert(3)
#     binary_tree.insert(4)
#     binary_tree.insert(39)
#     binary_tree.insert(22)
#     binary_tree.insert(9)
#     binary_tree.insert(4)
#     binary_tree.insert(6)
#     binary_tree.inorder()
#
# import sys
# from typing import Optional
#
# class MiniHeap(object):
#     def __init__(self) -> None:
#         self.heap = [-1 * sys.maxsize]
#         self.current_size = 0
#     def parent_index(self, index: int) -> int:
#         return index // 2
#
#     def left_child_index(self, index: int) -> int:
#         return 2 * index
#
#     def right_child_index(self, index: int) -> int:
#         return (2 * index) + 1
#
#     def swap(self, index1: int, index2: int) -> None:
#         self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
#
#     def heapify_up(self, index: int) -> None:
#         while self.parent_index(index) > 0:
#             if self.heap[index] < self.heap[self.parent_index(index)]:
#                 self.swap(index, self.parent_index(index))
#             index = self.parent_index(index)
#
#     def push(self, value: int) -> None:
#
#         self.heap.append(value)
#         self.current_size += 1
#         self.heapify_up(self.current_size)
#
#     def min_child(self, index: int) -> int:
#         if self.right_child_index(index) > self.current_size:
#             return self.left_child_index(index)
#         else:
#
#             if (self.heap[self.left_child_index(index)] <
#                 self.heap[self.right_child_index(index)]):
#                 return self.left_child_index(index)
#             else:
#                 return self.right_child_index(index)
#
#
#
#     def heapify_down(self, index: int) -> None:
#         while self.left_child_index(index) <= self.current_size:
#             min_child_index = self.min_child(index)
#             if self.heap[index] > self.heap[min_child_index]:
#                 self.swap(index, min_child_index)
#             index = min_child_index
#
#     def pop(self) -> Optional[int]:
#         if len(self.heap) == 1:
#             return
#
#         root = self.heap[1]
#         data = self.heap.pop()
#         if len(self.heap) == 1:
#             return root
#         self.heap[1] = data
#         self.current_size -= 1
#         self.heapify_down(1)
#
#
#
#         return root
#
# if __name__ == '__main__':
#     min_heap = MiniHeap()
#     min_heap.push(5)
#     min_heap.push(3)
#     min_heap.push(4)
#     min_heap.push(644)
#     min_heap.push(26)
#     min_heap.push(63)
#     min_heap.push(29)
#     print(min_heap.heap)
#     print(min_heap.pop())
#     print(min_heap.heap)


# import heapq
#
# from collections import Counter
# from typing import List
#
# def top_n_with_heap(words: List[str], n: int) -> List[str]:
#     #
#     # d = {}
#     # for word in words:
#     #     d[word] = d.get(word, 0) + 1
#     # print(d)
#     counter_word = Counter(words)
#     # print(counter_words)
#     # print(counter_words.most_common(n))
#     data = [(-counter_word[word], word) for word in counter_word]
#     heapq.heapify(data)
#     return [heapq.heappop(data) for _ in range(n)]
#
#
# if __name__ == '__main__':
#     w = ['python', 'c', 'java', 'go', 'c', 'javascript']
#     print(top_n_with_heap(w, 3))

        #
        #
        # numbers = [1, 3, 5, 7, 9]
        # heap_data = []
        #
        # heapq.heapify(numbers)
        # print(numbers)
        #
        #
        # print(heapq.nlargest(3,numbers))
        # print(heapq.nsmallest(3,numbers))


    # for num in numbers:
    #     heapq.heappush(heap_data, num)
    #
    # print(heap_data)
    #
    #
    #
    # while heap_data:
    #     print(heapq.heappop(heap_data))
    #



# from typing import List
#
#
# def insertion_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(1, len_numbers):
#         temp = numbers[i]
#         j = i - 1
#         while j >= 0 and numbers[j] > temp:
#             numbers[j+1] = numbers[j]
#             j -= 1
#
#         numbers[j+1] = temp
# if __name__ == '__main__':
#
#     import random
#
#
#     nums = [1, 8, 4, 5, 4, 19, 3]
#     print(insertion_sort(nums))



#
#
# from typing import List
#
# def insertion_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(1, len_numbers):
#         j = i - 1
#         temp = numbers[i]
#
#         while j > 0 and numbers[j] > temp:
#             numbers[j+1] = numbers[j]
#             j -= 1
#
#         numbers[j+1] = temp
#     return numbers
#
#
# def bucket_sort(numbers: List[int]) -> List[int]:
#
#     max_num = max(numbers)
#     len_numbers = len(numbers)
#     size = max_num // len_numbers
#
#     buckets = [[] for _ in range(size)]
#     for num in numbers:
#         i = num // size
#         if i != size:
#             buckets[i].append(num)
#
#         else:
#             buckets[size-1].append(num)
#
#     for i in range(size):
#         insertion_sort(buckets[i])
#
#     result = []
#     for i in range(size):
#         result += buckets[i]
#
#     return result
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     import random
#
#     nums = [random.randint(0, 1000) for i in range(10)]
#     print(bucket_sort(nums))

#
# from typing import List
#
# def shell_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     gap = len_numbers // 2
#     while gap > 0:
#         for i in range(gap, len_numbers):
#             temp = numbers[i]
#             j = i
#             while j >= gap and numbers[j-gap] > temp:
#                 numbers[j] = numbers[j-gap]
#
#                 j -= gap
#             numbers[j] = temp
#
#         gap //= 2
#
#     return numbers
#
#
# if __name__ == '__main__':
#     nums = [3, 4, 4, 233, 5]
#     print(shell_sort(nums))

#
# from typing import List
#
# def counting_sort(numbers: List[int]) -> List[int]:
#     counts = [0] * 10
#     result = [0] * len(numbers)
#
#     for num in numbers:
#         index = int(num / place) % 10
#         counts[index] += 1
#
#     for i in range(1, 10):
#         counts[i] += counts[i-1]
#
#
#     i = len(numbers) - 1
#     while i >= 0:
#         index = numbers[i]
#         result[counts[index] -1] = numbers[i]
#         counts[index] -= 1
#         i -= 1
#
#     return result
#
# def radix_sort(numbers: List[int], place: int) -> List[int]:
#     max_num = max(numbers)
#     place = 1
#     while max_num > place:
#         numbers = counting_sort(numbers, place)
#         place *= 10
#     return numbers
#
#
#
#
#
#
# if __name__ == '__main__':
#     nums = [4, 3, 4, 3, 8]
#     print(radix_sort(nums))


# from typing import List
#
# def partition(numbers: List[int], low: int, high: int) -> int:
#
#     i = low - 1
#     pivot = numbers[high]
#     for j in range(low, high):
#         if numbers[j] <= pivot:
#             i += 1
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#     numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
#     return i+1
#
#
#
# def quick_sort(numbers: List[int]) -> List[int]:
#     def _quick_sort(numbers: List[int], low: int, high: int) -> None:
#         if low < high:
#             partition_index = partition(numbers, low, high)
#             _quick_sort(numbers, low, partition_index-1)
#             _quick_sort(numbers, partition_index+1, high)
#
#     _quick_sort(numbers, 0, len(numbers) -1)
#     return numbers
#
#
#     # partition(numbers, low, high)
#
# if __name__ == '__main__':
#     nums = [1,3,92,3,]
#     print(quick_sort(nums))

