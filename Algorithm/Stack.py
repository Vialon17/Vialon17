
##  2.修改计算后序表达式的算法，使其能处理异常情况。
##  3.结合从中序到后序的转换算法以及计算后序表达式的算法，实现直接的中序计算。在计算时，应该使用两个栈从左往右处理中序表达式标记。一个栈用于保存运算符，另一个用于保存操作数。
##  4.将在练习 3 中实现的算法做成一个计算器。
##  5.使用列表实现队列抽象数据类型，将列表的后端作为队列的尾部。
##  6.设计和实现一个实验，对比两种队列实现的性能。能从该实验中学到什么？
from array import array
from inspect import stack
from os import lstat

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        temp = None
        if self.isEmpty():
            return temp
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

##  1.修改从中序到后序的转换算法，使其能处理异常情况。
def set_1(string):
    stack_num = Stack()
    stack_operator = Stack()
    prec = ('*', '/', '+', '-')
    bracket = ('(', ')')
    result = ''
    for i in string:
        if i in prec:
            stack_operator.push(i)
            result += stack_num.pop()
            result += stack_operator.pop()
            continue
        if i == bracket[0]:
            continue
        if i == bracket[1]:
            result += stack_num.pop()
            result += stack_num.pop()
            result += stack_operator.pop()
            continue
        stack_num.push(i)
    print(stack_num.items,stack_operator.items)
    print(result)
    for x in range(stack_num.size()):
        result += stack_num.pop()
        if x % 2 != 0 or x == 0:
            result += stack_operator.pop()
    print(result)

#recursion
def set_2():
    list_1 = [2, 4, 6, 8, 10]
    def recur(list1 : list):
        return list1[0] if len(list1) == 1 else list1.pop() + recur(list1)

    def len_list(list2 : list):
        if list2 == []:
            return 0
        else:
            list2.pop()
            return len_list(list2) + 1 
    print(len_list(list_1))

#D&C sum function
##4.1
def sum_func(list1 : list):
    if list1 == []:
        return 0
    else:
        return list1.pop() + sum_func(list1)

##4.3
def max_list(list1: list):
    if len(list1) == 1:
        return list1[0]
    if len(list1) == 0:
        return None
    else:
        if list1[0] >= list1[1]:list1.pop(1);return max_list(list1)
        else:list1.pop(0); return max_list(list1)

## Quick Sort Fake
def qui_sork_fake(list_temp : list):
    def function(list1 : list):
        if len(list1) < 2:
            raise KeyboardInterrupt('Input list Error!')
        else:
            if list1[0] < list1[1]: list1[0], list1[1] = list1[1], list1[0]
            return list1 if len(list1) == 2 else list1[:1] + qui_sork(list1[1:])
    list1 = list_temp
    for i in range(len(list1)):
        list1 = function(list1)
    return list1

## Quick Sort
def qui_sork(list1 : list):
    if len(list1) <= 2:
        if len(list1) == 2 and list1[0] > list1[1]:
            list1[0], list1[1] = list1[0], list1[1]
        return list1
    else:
        line_slice = len(list1)//2
        list2, list3 = list1[:line_slice], list1[line_slice + 1:]
        for x in range(len(list2)):
            if list2[x] > list1[line_slice]:
                list2[x], list1[line_slice] = list1[line_slice], list2[x]
        for y in range(len(list3)):
            if list3[y] < list1[line_slice]:
                list3[y], list1[line_slice] = list1[line_slice], list3[y]
        return qui_sork(list2) + list1[line_slice:line_slice + 1] + qui_sork(list3)

##Insert Sort
def ins_sort(list1: list):
    list2 = []
    list2.append(list1[0])
    for x in range(len(list1)):
        for y in range(len(list2)):
            if list2[y] < list1[x]:
                if y == len(list2) - 1:
                    list2.append(list1[x])
                continue
            if list2[y] > list1[x]:
                list2.insert(y, list1[x])
                break
    return list2

#Graph
class Graph_ver:
    def __init__(self):
        self._vertex = []
    
    @property
    def vertex(self):
        return self._vertex
    
    def add_vertex(self, key):
        self._vertex.append(key)
        return key
    
    def del_vertex(self, key):
        if key in self._vertex:
            self._vertex.remove(key)
        else:
            raise Exception('Key Error')
    

class Graph_rel():
    pass
def main():
    print(ins_sort([2, 59, 0, 46, 23]))

if __name__ == '__main__':
    main()