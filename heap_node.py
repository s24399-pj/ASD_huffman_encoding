class HeapNode:
    @staticmethod
    def build_min_heap(arr):
        n = int((len(arr) // 2) - 1)

        for k in range(n, -1, -1):
            HeapNode.min_heapify_node(arr, k)

        return arr

    @staticmethod
    def build_min_heap_using_nodes(array_of_nodes):
        return HeapNode.build_min_heap(array_of_nodes)

    @staticmethod
    def min_heapify_node(arr, i):
        HeapNode.__min_heapify_node(arr, len(arr), i)

    @staticmethod
    def __min_heapify_node(arr, n, i):
        left_child = HeapNode.__left(i)
        right_child = HeapNode.__right(i)

        smallest = i
        if left_child < n and arr[left_child].value < arr[i].value:
            smallest = left_child

        if right_child < n and arr[right_child].value < arr[smallest].value:
            smallest = right_child

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            HeapNode.__min_heapify_node(arr, n, smallest)

    @staticmethod
    def insert_node(arr, node):
        n = len(arr)
        arr.append(node)
        HeapNode.__heapify(arr, n, n - 1)

    @staticmethod
    def __heapify(arr, n, i):
        parent = int(((i - 1) / 2))

        if arr[parent].value > 0:
            if arr[i].value > arr[parent].value:
                arr[i], arr[parent] = arr[parent], arr[i]
                HeapNode.__heapify(arr, n, parent)

    @staticmethod
    def __left(i):
        return 2 * i + 1

    @staticmethod
    def __right(i):
        return 2 * i + 2
