# # def add_elements(arr):
# #     sum=0
# #     for element in arr:
# #         sum+=element

# #     return f"sum of {arr}  after addition:{sum}" 

# # sample_array = [5, 10, 15, 20, 25]
# # result = add_elements(sample_array)
# # print("Sum of all elements:", result)

# # """========================================================"""

# # """to add digonal elements of an array"""
# # def print_digonal_elements(matrix):

# #     n=len(matrix)
# #     print("digonal elements are")

# #     for i in range(n):
# #         print([matrix[i][i]])

# #     print()


# # sample_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # print_digonal_elements(sample_matrix)


# def  non_zero_elements(arr):
#     print("non zero elements")

#     #n=len(arr)
#     for elements in  arr:
#         if elements !=0:
#             print(f"non zero elements{elements}:")
        
# arr = [10, 0, 45, 0, 0, 8, 99, 0]
# non_zero_elements(arr)



"""same code with oop"""

class ArrayOperations:

    def __init__(self, data_1d=None, data_2d=None):
        """Initializes the object with 1D and/or 2D array data."""
        self.array_1d = data_1d if data_1d is not None else []
        self.matrix_2d = data_2d if data_2d is not None else [[]]

    def add_all_elements(self):
        """(a) Adds and returns all elements of the 1D array."""
        total_sum = 0
        for element in self.array_1d:
            total_sum += element
        return total_sum

    def print_diagonal_elements(self):
        """(b) Prints only the primary diagonal elements of the 2D array."""
        n = len(self.matrix_2d)
        print("Diagonal elements are:", end=" ")
        for i in range(n):
            # Safe check to handle empty inner lists
            if len(self.matrix_2d[i]) > i:
                print(self.matrix_2d[i][i], end=" ")
        print()  # Newline

    def print_non_zero_elements(self):
        """(c) Prints all non-zero elements of the 1D array."""
        print("Non-zero elements are:", end=" ")
        for element in self.array_1d:
            if element != 0:
                print(element, end=" ")
        print()  # Newline


# ==========================================
# DRIVER CODE (Testing our OOP Implementation)
# ==========================================

# 1. Define sample data
sample_1d_list = [5, 0, 15, 0, 25, 30, 0]
sample_2d_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2. Instantiate the class (Create an object)
arr_obj = ArrayOperations(data_1d=sample_1d_list, data_2d=sample_2d_matrix)

# 3. Call the methods using the object
# (a) Sum of elements
total = arr_obj.add_all_elements()
print(f"Sum of 1D array elements: {total}")

# (b) Print diagonals
arr_obj.print_diagonal_elements()

# (c) Print non-zero elements
arr_obj.print_non_zero_elements()