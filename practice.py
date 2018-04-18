
# def frenchDictionary():
#     french = dict()
#     french['hello']= 'bonjour'
#     french['yes']='oui'
#     french['no']='non'
#     french['goodbye']= 'au revior'
#     french['one']='un'
#     french['two']='deux'
#     french['three']='trois'
#     return french
#
# def main():
#     dictionary = frenchDictionary()
#     print(dictionary['two'])
#
# main()
# x = 3
# def main():
#     f(x)
# def f(x):
#     print(x)
# main()
#
# def almighty_formula(a,b,c):
#     d = (b*b)-(4*a*c)
#     root1 = (-b+d)/(2*a)
#     root2 = (-b-d)/(2*a)
#     print ('x = {} or x = {}'.format(root1,root2))
# def main():
#     a = int(input('a = '))
#     b = int(input('b = '))
#     c = int(input('c = '))
#     print('{}x^2 + {}x + {}'.format(a,b,c))
#     almighty_formula(a,b,c)
# main()

# def frenchDict():
#     french = dict()
#     french['Hello']='Bonjour'
#     french['Goodbye']='Au revoir'
#     french['Yes']='Oui'
#     french['No']='Non'
#     french['one']='un'
#     french['two']='deux'
#     french['three']='trois'
#     french['red']='rouge'
#     french['yellow']='jaune'
#     french['blue']='bleu'
#     french['white']='blanc' or 'blanche'
#     french['black']='noir' or 'noire'
#
# def main():
#     translate = frenchDict()
#     word = str(input('Write a word: '))
#     print(translate[word])
# main()

# def frenchDict():
#     french = dict()
#     french['Hello']='Bonjour'
#     french['Goodbye']='Au revoir'
#     french['Yes']='Oui'
#     french['No']='Non'
#     french['one']='un'
#     french['two']='deux'
#     french['three']='trois'
#     french['red']='rouge'
#     french['yellow']='jaune'
#     french['blue']='bleu'
#     french['white']='blanc' or 'blanche'
#     french['black']='noir' or 'noire'
#     return french
# def main():
#     dictionary = frenchDict()
#     numberFormat = 'Count in french: {one}, {two}, {three}, ...'
#     withSub = numberFormat.format(**dictionary)
#     print(withSub)
#     print("French colors: {red}, {yellow}, {blue}, ...".format(**dictionary))
# main()

# K = list(map(int, input().split()))
# M = list(map(int, input().split()))
# L = list(map(int, input().split()))
# N = list(map(int, input().split()))
# O = (pow(max(M),2)+pow(max(L),2)+pow(max(N),2)%K[-1])
# # print(O)

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# if query_name in student_marks:
#     avg = ((sum(student_marks[query_name]) / len(student_marks[query_name])))
#     print("{0:.2f}".format(avg))

# import re
# regex_pattern = r"[.,]+"
# n = ("\n".join(re.split(regex_pattern,input())))
# print(n)

# n = int(input().strip())
# for i in range(n):
#     i += 1
#     a = abs(i-n)
#     print(a*" "+i*"#")

# arr = list(map(int, input().split()))
# rev = arr[::-1]
# print (rev)
# print (*rev)

# import re
# def refexp(p1):
#     p1 = re.compile('[A-Za-z0-9._%+-+@[A-Za-z0-9.-]+.\[A-Za-z]{3,4}')
#     print(p1)

# if text is None:
#     text = "None is"
#     text += " just nothing"
# else:
#     text += " meaningful"
# print(text)

# x = int(input())
# y = int(input())
# sum = x+y
# prod = x*y
# formatStr = '{x} + {y} = {sum};\n{x} * {y} = {prod}'
# equation = formatStr.format(**locals())
# print(equation)

# name = input("Hi, what's your name? ")
# greeting = "Hello, {name}\nNice to meet you"
# print(greeting.format(**locals()))

# x = 3
# y = x + 2
# y = 2*y
# x = y - x
# print (x,y)
# for count in [1,3,5]:
#     print(count)
#     print('Yes'*count)
# print('Done counting')
# for color in ['red','blue','green']:
#     print(color)

# storyFormat = '{name} is a {age} year old {gender}'
# def addIn(cue,dictionary):
#     prompt = 'What is your ' + cue + '? '
#     response = input(prompt)
#     dictionary[cue] = response
# def tellStory():
#     userIn = dict()
#     for cue in ['name', 'age', 'gender']:
#         addIn(cue, userIn)
#     story = storyFormat.format(**userIn)
#     print('\n'+story)
# if __name__ == '__main__':
#     tellStory()

# print(2,type(2))
# print(3.5,type(3.5))
# print('a',type('a'))
# print([],type([]))
# print(True,type(True))
# print(None,type(None))

# colors = ['red','orange','yellow','green']
# num = 0
# for color in colors:
#     num += 1
#     print(num, color)

# def num_list(items):
#     num = 0
#     for item in items:
#         num +=1
#         print(num,item)
#
# if __name__ == '__main__':
#     num_list(['red','orange','yellow','green','blue','indigo','violet'])
#     print()
#     num_list(['apples','oranges','pears','mangoes'])

# def sum_list(nums):
#     sum = 0
#     for num in nums:
#         sum = sum + num
#     return sum
# print(sum_list([5,12,23,45]))

# def join(strings):
#     word =''
#     for string in strings:
#         word += string
#     return word
# if __name__ == '__main__':
#     s = join(['very','hot','day'])
#     print(s)

# def m(x):
#     return 5*x
# y = 3
# print (m(y) + m((2*y)-1))

# x = 0
# y = 1
# print(x,y)
# for n in [5,4,6]:
#     x = x+y*n
#     y = y+1
#     print(x,y)

# def product(nums):
#     prod = 1
#     for n in nums:
#         prod = prod*n
#     return prod
# if __name__ == '__main__':
#     print(product([5,4,6]))

# def one_line(items):
#     for item in items:
#         print(item,end=' ')
# one_line(['lets','see','what','we','get'])
# print()
# print('Oh, forgot to add this thing')

# seq = list()
# n = int(input('n: '))
# for i in range (n):
#     g = input('G: ')
#     seq.append(g)
# print(seq)
# print(seq[1])
# print(max(seq))

# #How to print last three letters
# def back(s):
#     return s[-3:]
#
# if __name__ == '__main__':
#     n = int(input())
#     words = list()
#     for i in range(n):
#         s = input('Word: ')
#         v = back(s)
#         words.append(v)
#         #word = set(words)   #set cannot have repeated variables
#     print('\n'.join(words))

# s = input('Word: ')
# print('The full string is: ',s)
# n = len(s)
# for i in range(n):
#     print()
#     print('i = ',i)
#     print('The letter at index i:', s[i])
#     print('The letter before index i: ', s[:i])
#     print('The part before index i+2: ',s[:i+2])

# s = "Stuff I'm typing"
# print(''.join(s))
# print(' '.join(s))
# print('//'.join(s))
# print('##'.join(s))

# phrase = input()
# phr = format(str.lower(phrase))
# print('_'.join(phr.split()))

# def multipall(num_list,multi):
#     new_list = list()
#     for num in num_list:
#         new_list.append(num*multi)
#     return new_list
#
# if __name__ == '__main__':
#     num_list = list(map(int, input('Enter items in array sepearated by spaces: ').split()))
#     multi = int(input('Multiplier: '))
#     print(multipall(num_list,multi))

# story_format = '''This is a story about {name}.
# {name} is a {gender} who lives in {city}.
# {pronoun} does lots of awesome stuff.
# But I'm not going to mention any of the awesome stuff {name} gets up to in {city}
# Because I'm lazy.
# Sue me.'''
# second_story = '''This is a story about {animal}.
# {animal} is a {specie} who lives in {habitat}.
# {animal} does lots of awesome stuff.
# But I'm not going to mention any of the awesome stuff {animal} gets up to in {habitat}
# Because I'm lazy.
# Sue me.'''
#
# def get_keys(story):
#     key_list = list()
#     repetition = story.count('{')
#     end = 0
#     for i in range(repetition):
#         start = story.find('{',end ) + 1
#         end = story.find('}',start)
#         key = story[start:end]
#         key_list.append(key)
#     return set(key_list)
# def add(cue,dictionary):
#
#     prompt_format = 'Enter a specific example for '
#
# print(get_keys(story_format))
# print(get_keys(second_story))
#
# def printLocation(text,letter):
#     texts = list()
#     repetition = text.count(letter)
#     end = 0
#     for i in range(repetition):
#         start = text.find(letter,end) + 1
#         end = text.find(letter,start)
#         t = text[start:end]
#         texts.append(t)
#     return texts

# def printLocations(text,letter):
#     rep = text.count(letter)
#     end = 0
#     for i in range(rep):
#         start = text.find(letter, end)
#         print('Start: ',start)
#         end = text.find(letter, start) + 1
#         print('End: ', end)
#         t = text.find(letter, start)
#         print(t)
# if __name__ == '__main__':
#     text = input('Enter string here: ')
#     letter = input('Enter search object here: ')
#     printLocations(text,letter)

# n,m = input().split()
# n,m = [int(n), int(m)]
# c = list(map(int, input().split())
# while len(c)>n or len(c)<n:
#     print('n/a')
#     c = list(map(int, input().split()))
# s = list(range(m))
# count_list = []
# for student in s:
#     count = 0
#     for classes in c:
#         if student == classes:
#             count+=1
#     count_list.append(count)
# print(*count_list)

# n = int(input())
# times = 'HelloWorld '
# spl = (n*times).split()
# print('-'.join(spl))

# n = int(input())
# A = list()
# for i in range(n):
#     a = int(input())
#     A.append(a)
# print(A)
# num = int(input())
# if num in A:
#     print('YES')
# else:
#     print('NO')
# import sys
# import os
#
# def oddNumbers(l,r):
#     res = list()
#     for i in range(l,r+1):
#         if i%2!=0:
#             res.append(i)
#         if i%2==0:
#             pass
#     return res
#
# if __name__ == '__main__':
#     _l = int(input())
#     _r = int(input())
#
#     res = oddNumbers(_l,_r)
#     for res_cur in res:
#         print(str(res_cur)+"\n")
# n = int(input())
# arr = list(map(int,input().split()))
# if len(arr)<n:
#     print('NIL')
# else:
#     pos = len(arr)-n
#     print(arr[pos])

# n = int(input())
# a = 0
# b = 1
# c = 1
# fib=list()
# for i in range(n):
#     c = a+b
#     a = b
#     b = c
#     fib.append(c)
# print(fib)

# t = int(input())
#
# for i in range(t):
#     n,k = map(int, input().strip().split())
#
#     A = list(map(int, input().strip().split()))
#     A.sort()
#
#     B = list(map(int, input().strip().split()))
#     B.sort(reverse=True)
#
#     answer = True
#     for a,b in zip(A,B):
#         if a+b < k:
#             answer = False
#     if answer:
#         print("YES")
#     else:
#         print("NO")

# n = int(input())
# if n==0:
#     print('n/a')
# else:
#     fac = list(range(n+1))
#     fac.remove(min(fac))
#     prod = 1
#     for x in fac:
#         prod *= x
#     print(prod)
#

# a = input().split(',')
# N = list(map(int,input().split()))
# rem = set([x for x in N if N.count(x) > 1])
# for item in rem:
#     for x in N:
#         if item in N:
#             N.remove(item)
# print(rem)
# print(*N)

# n = int(input())
# N = list(range(n+1))
# N.remove(min(N))
# for index, item in enumerate(N):
#     if item%3==0:
#         N[index] = 'Fizz'
#     if item%5==0:
#         N[index] = 'Buzz'
#     if item%3==0 and item%5==0:
#         N[index] = 'FizzBuzz'
# for i in N:
#     print(i)

# arr = list(map(int,input().split()))
# if len(arr)!=5:
#     pass
# else:
#     add = list()
#     for x in arr:
#         arr.remove(x)
#         arradd = sum(arr)
#         arr.append(x)
#         add.append(arradd)
#     print(min(add),max(add))
# def miniMaxSum(arr):
#     add = sum(arr)
#     print (add-(max(arr)), (add-(min(arr))))

# n = int(input())
# arr = list(map(int,input().split()))
# if len(arr)!=n:
#     pass
# else:
#     count = 0
#     for item in arr:
#         if item == max(arr):
#             count+=1
#     print(count)

# n = int(input())
# arr = list(map(int,input().split()))
# zer,pos,neg=0,0,0
# for item in arr:
#     if item==0:
#         zer+=1
#     if item>0:
#         pos+=1
#     if item<0:
#         neg+=1
# pos = format((pos/len(arr)), '.6f')
# neg = format((neg/len(arr)), '.6f')
# zer = format((zer/len(arr)), '.6f')
# print(pos)
# print(neg)
# print(zer)

# time = input()
# pm = time[-2:]
# spl = time.split(pm)
# spl = ''.join(spl)
# spl2 = spl.split(':')
# res = list(map(int, spl2))
# print(res)
# if pm == 'AM':
#     if res[0]==12:
#         res[0]=00
#     res = ["%02d" % n for n in res]
#     res = ':'.join(res)
#     print(res)
# else:
#     res[0] = res[0]+12
#     if res[0]==12:
#         res[0] = 12
#     res = ["%02d" % n for n in res]
#     res = ':'.join(res)
#     print(res)

# import re
# s = input()
# spl = re.findall('[A-Z][^A-Z]*', s)
# if s[0].isupper() == False:
#     print(len(spl)+1)
# else:
#     print(len(spl))
# import re
#
# spec = "!@#$%^&*()-+"
# spec_list=list(spec)
#
# n = int(input())
# if n<6:
#     print(6-n)
# else:
#     s = input()
#     spl = list(s)
#     upp = re.findall('[A-Z]', s)
#     low = re.findall('[a-z]', s)
#     num = re.findall('[0-9]', s)
#     spe=[]
#     for x in spec_list:
#         for i in spl:
#             if i == x:
#                 spe.append(i)
#     count = 0
#     if len(upp) == 0:
#         count += 1
#     if len(low) == 0:
#         count+=1
#     if len(num) == 0:
#         count+=1
#     if len(spe) == 0:
#         count+=1
#     print(count)

# n = int(input())
# grades=[]
# for i in range(n):
#     grade = int(input())
#     grades.append(grade)
# for grade in grades:
#     if grade<38:
#         grade=grade
#     else:
#         diff = (((grade+5)//5)*5)-grade
#         if diff<3:
#             grade = (((grade+5)//5)*5)
#     print(grade)
# def lena_sort(nums):
#     # if len(nums)<1:
#     #     return nums
#     pivot = nums[0]
#     less = list()
#     more = list()
#     for x in nums:
#         if x<pivot:
#             less.append(x)
#         else:
#             more.append(x)
#     sort_less = lena_sort(less)
#     print(less,sort_less)
# nums = list(map(int,input().split()))
# lena_sort(nums)

# s,t = input().split()
# a,b = input().split()
# m,n = input().split()
# s,t,a,b,m,n = [int(s), int(t),int(a),int(b),int(m),int(n)]
# apples = list(map(int,input().split()))
# oranges = list(map(int,input().split()))
# acount=0
# bcount=0
# for apple in apples:
#     if (apple+a) in range(s,t):
#         acount+=1
# for orange in oranges:
#     if (orange+b) in range(s,t):
#         bcount+=1
# print(acount)
# print(bcount)

# k1,d1,k2,d2 = input().split()
# k1,d1,k2,d2 = [int(k1), int(d1), int(k2), int(d2)]
# for i in range(k1,d1):
#     for j in range(k2,d2):
#         if i == j:
#             print('YES')
#         else:
#             print('NO')

# n,m = input().split()
# n,m = [int(n),int(m)]
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# for a in A and b in B:
#         if a%b==0:
#             print(a)

# s = input()
# t = input()
# # k = int(input())
# s_list = list(s)
# t_list = list(t)
# for i,x in enumerate(s_list):
#     for j,y in enumerate(t_list):
#         if x==y:
#             s_list.remove(s_list[i])
#             t_list.remove(t_list[j])
# print(s_list,t_list)

# import time
# n = int(input())
# A = []
# for i in range(n):
#     a = int(input())
#     A.append(a)
# print(sorted(A, key=int))
# print(A.sort(key=int))

# def introTutorial(v, arr):
#     if v in arr:
#         return arr.index(V)
#
# if __name__ == "__main__":
#     V = int(input().strip())
#     n = int(input().strip())
#     arr = list(map(int, input().strip().split(' ')))
#     result = introTutorial(V, arr)
#     print(result)

# a,b,n = input().split()
# a,b,n=[int(a),int(b),int(n)]
# fib=list()
# for i in range(n):
#     c = a+(b*b)
#     a = b
#     b = c
#     fib.append(a)
# print(fib[n-2])

# graph = {"a":["c"],
#          "b":["c","e"],
#          "c":["a","b","d","e"],
#          "d":["c"],
#          "e":["c","b"],
#          "f":[]}
# def edges(graph):
#     edge=[]
#     for node in graph:
#         for neighbour in graph[node]:
#             edge.append((node,neighbour))
#     return edge
# def isolated(graph):
#     isolate = []
#     for node in graph:
#         if not graph[node]:
#             isolate += node
#     return isolate
# print(edges(graph))
# print(isolated(graph))

# def rotate(l,n):
#     return l[n:]+l[:n]
# l = [1,2,3,4,5]
# n = int(input())
#
# print(rotate(l,n))

# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# C = list()
# D = list()
# for i in A:
#     if i in B:
#         C.append(i)
#     if i not in B:
#         D.append(i)
# for j in B:
#     if j not in A:
#         D.append(j)
# print(C)
# print(D)

# text1 = input()
# text2 = input()
# text1_list=list(text1)
# text2_list=list(text2)
# same=[]
# diff=[]
# for text in text1_list:
#     if text in text2_list:
#       same.append(text)
# print(same)
#
# for a in range(1000):
#     for b in range(1000):
#         for c in range(1000):
#             for d in range(1000):
#                 if pow(a,3)+pow(b,3)==pow(c,3)+pow(d,3):
#                     print(a,b,c,d)

# def KMPSearch(pattern,text):
#     m = len(pattern)
#     n = len(text)
#     lps = [0]*m
#     computeLPSarray(pattern, m, lps)
#     j = 0
#     i = 0
#     while  i<n:
#         if pattern[j]==text[i]:
#             i+=1
#             j+=1
#         if j == m:
#             print("Pattern found at index: "+str(i-j))
#             j = lps[j-1]
#         elif i<n and pattern[j]!=text[i]:
#             if j!=0:
#                 j = lps[j-1]
#             else:
#                 i+=1
# def computeLPSarray(pattern,m,lps):
#     len = 0
#     lps[0]
#     i = 1
#     while i<m:
#         if pattern[i]==pattern[len]:
#             len+=1
#             lps[i]=len
#             i+=1
#         else:
#             if len!=0:
#                 len=lps[len-1]
#             else:
#                 lps[i]=0
#                 i+=1
# text = input('Text: ')
# pattern = input('Pattern: ')
# KMPSearch(pattern,text)
#
# maximum=256
# def compare(arr1,arr2):
#     for i in range(maximum):
#         if arr1[i]!=arr2[i]:
#             return False
#     return True
# def search(pattern,text):
#     m = len(pattern)
#     n = len(text)
#     countP=[]
#     for i in range(maximum):
#         countP.append(0)
#     countTW=[]
#     for i in range(maximum):
#         countTW.append(0)
#     for i in range(m):
#         countP[ord(pattern[i])]+=1
#         countTW[ord(text[i])]+=1
#         print(pattern[i])
#         print(text[i])
#     for i in range(m,n):
#         if compare(countP,countTW):
#             print('Found at Index',(i-m))
#         countTW[ord(text[i])]+=1
#         countTW[ord(text[i-m])]-=1
#     if compare(countP,countTW):
#         print('Found at Index',n-m)
# text = input()
# pattern = input()
# search(pattern,text)

# a = input()
# b = input()
# A = list(a)
# B = list(b)
# count=0
# for letter in A:
# 	if letter not in B:
# 		count+=1
# for letter in B:
# 	if letter not in A:
# 		count+=1
# print(count)

# def Node(value):
# 	left = list()
# 	right = list()
# 	value_list = list()
# 	n = int(input('Number of Value {} nodes: '.format(value)))
# 	for i in range(n):
# 		a = int(input('Node {} for Value {}: '.format(i+1,value)))
# 		if a < value:
# 			left.append(a)
# 		if a > value:
# 			right.append(a)
# 		value_list.append(value)
# 		print(left, set(value_list), right)
# 	for item in right:
# 		right.append(right)
# 	for item in left:
# 		Node(item)
# 	return (left,set(value_list),right)
#
# value = int(input('Value: '))
# print(Node(value))
#
# class Tree(object):
# 	def __init__(self):
# 		self.left = None
# 		self.right = None
# 		self.data = None
#
# root=Tree()
# root.data="root"
# root.left=Tree()
# root.left.data="left"
# root.right=Tree()
# root.right.data="right"
#
# root.left.left = Tree()
# root.left.left.data = "left 2"
# root.left.right=Tree()
# root.left.right.data = "left-right"
# print(root.left.data)

# class Tree:
# 	def __init__(self,data,left=None,right=None):
# 		self.data = data
# 		self.left = left
# 		self.right = right
#
# 	def __str__(self):
# 		return str(self.data)
# def total(tree):
# 	if tree == None: return 0
# 	print(total(tree.left) + total(tree.right) + tree.data)
#
# def print_tree(tree):
# 	if tree == None: return
# 	print(tree.data)
# 	print_tree(tree.left)
# 	print_tree(tree.right)
#
# def print_tree_postorder(tree):
# 	if tree == None: return
# 	print_tree_postorder(tree.left)
# 	print_tree_postorder(tree.right)
# 	print(tree.data)
#
# def print_tree_inorder(tree):
# 	if tree ==  None: return
# 	print_tree_inorder(tree.left)
# 	print(tree.data)
# 	print_tree_inorder(tree.right)
#
# def print_tree_indent(tree, level=0):
# 	if tree == None: return
# 	print_tree_indent(tree.right, level+1)
# 	print('  '*level + str(tree.data))
# 	print_tree_indent(tree.left, level+1)
#
# def get_token(token_list, expected):
# 	if token_list[0] == expected:
# 		del token_list[0]
# 		return True
# 	else:
# 		return False
#
# def get_number(token_list):
# 	x = token_list[0]
# 	if type(x) != type(0): return None
# 	del token_list[0]
# 	return Tree(x, None, None)
#
# def get_product(token_list):
# 	a = get_number(token_list)
# 	if get_token(token_list,'*'):
# 		b = get_number(token_list)
# 		return Tree('*',a,b)
# 	else:
# 		return a
#
# token_list = [9,'+',11,'end']
# tree = get_product(token_list)
# print_tree_postorder(tree)
# token_list=[9,'*',11,'end']
# tree=get_product(token_list)
# print_tree_postorder(tree)
# token_list = [9,11,'end']
# x = get_number(token_list)
#
# left = Tree(2)
# right = Tree(3)
# tree = Tree('+', Tree(1), (Tree('*', left, right)))
# a =100
# n =6
# N = 12
# d = 10
# tn = (n/2)*((2*a)+((n-1)*d))
# tnx = (N/2)*((2*a)+((N-1)*d))
# print (tn, 5*(tnx))

# year = int(input())
# days = 243
# diff = 256 - days
# if year == 1918:
# 	days = 229
# if year in range (1700,1918):
# 	if year%4==0:
# 		days = 244
# if year > 1918:
# 	if year%4==0 and not year%100==0:
# 		days = 244
# print('{}.09.{}'.format(diff,year))

# arr = list()
# count = 0
# for i in range(int(input())):
#     op, contact = input().split()
#     if op == "add":
#         arr.append(contact)
#     if op == "find":
#         for contact in arr:
#             count +=1
#         print(count)
# print(arr)

# n = int(input().strip())
# find_count = 0
# no_count = 0
# contacts = list()
# for a in range(n):
#     op, contact = input().strip().split(' ')
#     if op == "add":
#         contacts.append(contact)
#     if op == "find":
#         for word in contacts:
#             if word.find(contact) >= 0:
#                 find_count += 1
#             else: no_count = 0
#         print(find_count)
#
#         counts.append(count)
# for count in counts:
#     print(count)

# numSwaps = 0
# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
# for i in range(n-1):
#     for j in range(n-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
#             numSwaps += 1
# print('Array is sorted in {} swaps'.format(numSwaps))
# print('First Element: {}'.format(a[0]))
# print('Last Element: {}'.format(a[-1]))

# n = int(input())
# a = list()
# a_i = 0
# for a_i in range(n):
#     a_t = int(input())
#     a.append(a_t)
#     a_sort = sorted(a, key=int)
#     if len(a_sort) == 1:
#         median = a_sort[0]
#     if len(a_sort)%2 == 0 and len(a_sort)!= 1:
#         i = int(len(a_sort)/2)
#         median = (a_sort[i-1]+a_sort[i])/2
#     if len(a_sort)%2 != 0 and len(a_sort)!= 1:
#         i = int(len(a_sort)/2)
#         median = a_sort[i]
#     print("{0:.1f}".format(median))

#
#
# def median(a):
#     l = a[len(a) // 2];
#     r = a[(len(a) // 2) - 1]
#     if len(a) % 2 == 0:
#         med = (l + r) / 2.0
#
#     elif len(a) % 2 != 0:
#         med = l
#     return med
#
# if __name__ == '__main__':
#     heap = []
#     for _ in range(int(input())):
#         insort(heap, int(input()))
#         print(float(median(heap)))
# from bisect import *
# a = [5,2,45,346,564,2123,65]
# x = 346
# b = ['apple','zoo','xylophone','boy','car','yo-yo']
#
# print(bisect_left(a,x,lo=0,hi=len(a)))
# print(bisect_right(a,x,lo=0,hi=len(a)))
# print(bisect(a,x,lo=0,hi=len(a)))
# print(insort_left(a,x,lo=0,hi=len(a)))
# print(insort_right(a,x,lo=0,hi=len(a)))
# print(insort(a,x,lo=0,hi=len(a)))

# def index(a,x):
#     i = bisect_left(a,x)
#     if i!= len(a) and a[i] == x:
#         return i
#     raise ValueError
#
# def find_lt(a,x):
#     i = bisect_left(a,x)
#     if i:
#         return a[i-1]
#     raise ValueError
#
# def find_le(a,x):
#     i = bisect_right(a,x)
#     if i:
#         return a[i-1]
#     raise ValueError
#
# def find_gt(a,x):
#     i = bisect_right(a,x)
#     if i!= len(a):
#         return a[i]
#     raise ValueError
#
# def find_ge(a,x):
#     i = bisect_left(a,x)
#     if i!= len(a):
#         return a[i]
#     raise ValueError
#
# a = list(map(int,input().split()))
# x = int(input())
# print(index(a,x),',',find_lt(a,x),',',find_le(a,x),',',find_gt(a,x),',',find_ge(a,x))

# def grade(score, breakpoints=[60,70,80,90],grades='FDCBA'):
#     i = bisect(breakpoints,score)
#     return grades[i]
#
# print([grade(score) for score in [45,65,75,85,95,80,70,60,50]])

# data = [('red',1),('blue',3),('yellow',5),('black',0)]
# data.sort(key=lambda r: r[1])
# keys = [r[1] for r in data]
# print(data[bisect_left(keys,0)])
# print(data[bisect_left(keys,1)])
# print(data[bisect_left(keys,3)])
# print(data[bisect_left(keys,5)])

# berth = dict()
# berth['LB'] = 1,4,9,12,17,20,25,28,33,36,41,44,49,52,57,60,65,68
# berth['MB'] = 2,5,10,13,18,21,26,29,34,37,42,45,50,53,58,61,66,69
# berth['UB'] = 3,6,11,14,19,22,27,30,35,38,43,46,51,54,59,62,67,70
# berth['SLB'] = 7,15,23,31,39,47,55,63,71
# berth['SUB'] = 8,16,24,32,40,48,56,64,72
#
# val = int(input())
# for key,value in berth.items():
#     if val in value:
#         print(key)
#     if val not in value:
#         pass


# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(n-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 swapped = True
#                 print(arr)
#         if swapped == False:
#             break
# arr = list(map(int,input().split()))
# bubble_sort(arr)

# arr = list(map(int,input().strip().split()))
# n = len(arr)
# count = 0
# for i in range(n):
#     for j in range(n-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#             count+=1
# print(count)

# def bubble_sort(listt):
#     for i,num in enumerate(listt):
#         try:
#             if listt[i+1]<num:
#                 listt[i]=listt[i+1]
#                 listt[i+1]=num
#                 bubble_sort(listt)
#                 print(listt)
#         except IndexError:
#             pass
#
# listt = list(map(int,input().split()))
# bubble_sort(listt)
#
# print('Sorted array:')
# for i in range(0,len(listt)):
#     print(listt[i],end='')
# _end = '_end_'
# def trie(*contacts):
#     root = dict()
#     for contact in contacts:
#         current_dict = root
#         for num in contact:
#             current_dict = current_dict.setdefault(num,{})
#         current_dict[_end] = _end
#     return root
#
# def in_trie(trie, contact):
#     count = 0
#     current_dict = trie
#     for num in contact:
#         if num in current_dict:
#             current_dict = current_dict[num]
#             count+=1
#         else: return
#     else:
#         if _end in current_dict:
#             count+=1
#         else: return
#     return count
# trie = list(map(str,input().split()))
# contact = input()
# print(trie(trie))
# print(in_trie(trie(trie),contact))

# from collections import defaultdict
# count = 0
# class Trie:
#     def __init__(self):
#         self.root = defaultdict()
#
#     def insert(self,contacts):
#         current = self.root
#         for contact in contacts:
#             current = current.setdefault(contact,{})
#         current.setdefault('_end')
#
#     def search(self,contacts):
#         current = self.root
#         for contact in contacts:
#             if contact not in current:
#                 return False
#             current=current[contact]
#         if '_end' in current:
#             return True
#         return False
#
#     def starts_with(self,prefix):
#         count = 0
#         current = self.root
#         for contact in prefix:
#             if contact in current:
#                 count+=1
#             if contact not in current:
#                 count = 0
#             current = current[contact]
#         return count
#
# test = Trie()
# n = int(input())
# for i in range(n):
#     op, contact = input().split()
#     if op == 'add':
#         test.insert(contact)
#     if op == 'find':
#         print(test.starts_with(contact))

# n = int(input())
# contacts = {}
#
# def add_contact(contact):
#     j = 1
#     while(j<=len(contact)):
#         if (contact[0:j] not in contacts):
#             contacts[contact[0:j]]=set()
# contacts

# def ransom_note(magazine, ransom):
#     if len(ransom) > len(magazine):
#         return False
#     words = {}
#     for word in magazine:
#         words.setdefault(word,0)
#         words[word]+=1
#         print(words)
#     for word in ransom:
#         if word in words:
#             words[word]-=1
#             print(words)
#         else: return False
#     return all([x>=0 for x in words.values()])
#
# m, n = map(int, input().strip().split(' '))
# magazine = input().strip().split(' ')
# ransom = input().strip().split(' ')
# answer = ransom_note(magazine, ransom)
# if(answer):
#     print("Yes")
# else:
#     print("No")

# def anagram(str1,str2):
#     return (sorted(str1)==sorted(str2))
# print(anagram('cat','rat'))
#
# def palindrome(str):
#     return (str==str[::-1])
# print(palindrome('cow'))

# import re
# def palindrome(word):
#     return(word == word[::-1])
# def all_palindromes(string):
#     left,right=0,len(string)
#     j=right
#     res=[]
#     for a in range(len(string)):
#         while left<right-1:
#             temp=string[left:j]
#             j-=1
#             if palindrome(temp):
#                 if len(temp)>=3:
#                     res.append(temp)
#             if j<left:
#                 left+=1
#                 j=right
#     return list(res)
# n = int(input())
# for i in range(n):
#     words=input().strip()
#     if not words:
#         print('n/a')
#         break
#     symbol = words[-3::]
#     tweet = sorted(all_palindromes(words))
#     tweet_set = sorted(set(tweet))
#     cardinality=list()
#     for word in tweet:
#         if word in tweet_set:
#             count = 0
#             count+=1
#         cardinal = len(word)*count
#         cardinality.append(cardinal)
#     if sum(cardinality) in range(1,10):
#         text = 'Possible'
#     if sum(cardinality) in range(11,40):
#         text = 'Probable'
#     if sum(cardinality) in range(41,150):
#         text = 'Escalate'
#     if sum(cardinality)>150 or sum(cardinality)==0:
#         text = 'Ignore'
#     if len(tweet)<2:
#         text='Ignore'
#     if len(words)<=3:
#         text = 'Ignore'
#     # if re.findall('[0-9]', words):
#     if not(words.isalpha()):
#         text='Ignore'
#     spec = list("!@#$%^&*()-+")
#     for word in words:
#         if word in spec:
#             text='Ignore'
#     print(symbol,text)

# n = int(input())
# student_marks = [[input(),float(input())] for i in range(n)]
# second_lowest = sorted(list(set([score for name, score in student_marks])))[1]
# print('\n'.join(sorted(name for name,score in student_marks if score==second_lowest)))

# def unique(string):
#     string_set = set(string)
#     print(string_set)
#     count = 0
#     if len(string_set)==len(string):
#         return True
#     else:
#         return False
# string=input()
# if unique(string):
#     print('YES')
# else:
#     print('NO')

# def delete(string):
#     return(''.join(sorted(set(string),key=string.index)))
# string = input()
# print(delete(string))

# word = input()
# print('%20'.join(word.split()))

# def isSubstring(s1,s2):
#     if sorted(set(s1))==sorted(set(s2)):
#         return 'YES'
#     else:
#         return 'NO'
#
# s1 = input()
# s2 = input()
# print(isSubstring(s1,s2))

# class Node:
#     def __init__(self,initdata):
#         self.data = initdata
#         self.next = None
#
#     def getData(self):
#         return self.data
#
#     def getNext(self):
#         return self.next
#
#     def setData(self,newdata):
#         self.data = newdata
#
#     def setNext(self,newnext):
#         self.next = newnext
#
# class unorderedList:
#     def __init__(self):
#         self.head = None
#
#     def isEmpty(self):
#         return self.head==None
#
#     def add(self,item):
#         temp = Node(item)
#         temp.setNext(self.head)
#         self.head = temp
#
#     def addend(self,item):
#         if self.head == None:
#             self.head = Node(item)
#             return
#         current = self.head
#         while current.next != None:
#             current = current.next
#         current.next = Node(item)
#
#     def size(self):
#         current = self.head
#         count = 0
#         while current!= None:
#             count+=1
#             current=current.getNext()
#
#         return count
#
#     def search(self,item):
#         current = self.head
#         found = False
#         while current!=None and not found:
#             if current.getData() == item:
#                 found = True
#             else:
#                 current = current.getNext()
#         return found
#
#     def remove(self,item):
#         current = self.head
#         previous = None
#         found = False
#         while not found:
#             if current.getData()==item:
#                 found = True
#             else:
#                 previous = current
#                 current = current.getNext()
#         if previous ==None:
#             self.head = current.getNext()
#         else:
#             previous.setNext(current.getNext())
#
#     def printl(self):
#         current = self.head
#         while current:
#             print(current.data,end=" -> ")
#             current = current.next
#
#     def unduplicate(self):
#         current = second = self.head
#         while current!=None:
#             while second.next!= None:
#                 if second.next.data == current.getData():
#                     second.next = second.next.next
#                 else:
#                     second = second.next
#             current = second = current.next
#
#     def detectLoop(self):
#         s = set()
#         current = self.head
#         while current:
#             if current in s:
#                 return True
#             s.add(current)
#             current = current.next
#         return False
#
#     def index(self,item):
#         current = self.head
#         index = 0
#         if item > self.size():
#             print('Index out of bounds')
#         else:
#             while index<item:
#                 index+=1
#                 current = current.getNext()
#             print(current.data)
#
# mylist = unorderedList()
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.addend(100)
# mylist.add(26)
# mylist.addend(50)
# mylist.add(54)
# mylist.add(77)
# print(mylist.printl())
# print(mylist.index(2))

# s = input()
# print(any(c.isalnum() for c in s))
# print(any(c.isalpha() for c in s))
# print(any(c.isdigit() for c in s))
# print(any(c.islower() for c in s))
# print(any(c.isupper() for c in s))

# thickness = int(input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# import textwrap
# def wrap(string,max_width):
#     for i in range((len(string)//max_width)+1):
#         j = i*max_width
#         word = string[j:j+max_width]
#         print(word)
#     return ''
# if __name__ == '__main__':
#     string = input()
#     max_width = int(input())
#     print(wrap(string,max_width))
#     print()
#     print(textwrap.wrap(string,max_width))

# stack = ['ball','cat','dog']
# stack.append('zoo')
# stack.append('apple')
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)

# from collections import deque
# queue = deque(["ball",'cat','zoo','dog'])
# print(queue)
# queue.append("egg")
# print(queue)
# queue.append('fish')
# print(queue)
# print(queue.popleft())
# print(queue.popleft())
# print(queue)
#
# def match(expression):
#     stack = []
#     push,pop = '({[',')}]'
#     for c in expression:
#         if c in push:
#             stack.append(c)
#         elif c in pop:
#             if not len(stack):
#                 return False
#             else:
#                 stackTop = stack.pop()
#                 balance = push[pop.index(c)]
#                 if stackTop!=balance:
#                     return False
#         else:
#             return False
#     return not len(stack)
#
# t = int(input().strip())
# for a0 in range(t):
#     expression = input().strip()
#     if match(expression) == True:
#         print("YES")
#     else:
#         print("NO")

# def panagram(string):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     match = []
#     for i in range(len(string)):
#         if i in list(alphabet):
#             match.append(i)
#             print(match)
#     if len(match)==len(list(alphabet)):
#         return 's'

# string = input()
# string_form = sorted(set(string.replace(" ","").lower()))
# print(string_form)
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alpha = list(alphabet)
# match = []
# for letter in string_form:
#     if letter in alpha:
#         alpha.remove(letter)
#         print(alpha)
# if len(alpha) == 0:
#     print('panagram')
# else:
#     print('not panagram')
# avg = []
# scores = list()
# for i in range(4):
#     score = list(map(float,input().split()))
#     for number in score:
#         score = [number for number in score if number!=0]
#         average = sum(score)/len(score)
#         if average.is_integer():
#             average=int(average)
#         else:
#             average = "%.2f" % round(average,1)
#     avg.append(average)
# avg_sort = sorted(avg,key=float,reverse=True)
# print(*avg_sort)

# def merge(arr,left,middle,right):
#     n1=middle-left+1
#     n2=right-middle
#     L = [0]*(n1)
#     R = [0]*(n2)
#     for i in range(0,n1):
#         L[i]=arr[left+i]
#     for j in range(0,n2):
#         R[j]=arr[middle+1+j]
#     i=0
#     j=0
#     k=left
#     while i<n1 and j<n2:
#         if L[i]<=R[j]:
#             arr[k]=L[i]
#             i+=1
#         else:
#             arr[k]=R[j]
#             j+=1
#         k+=1
#     while i<n1:
#         arr[k]=L[i]
#         i+=1
#         k+=1
#     while j<n2:
#         arr[k]=R[j]
#         j+=1
#         k+=1
# def mergesort(arr,left,right):
#     if left<right:
#         middle = (left +(right-1))/2
#
#         mergesort(arr,left,middle)
#         mergesort(arr,middle+1,right)
#         merge(arr,left,middle,right)
#
# arr = [12,11,13,5,6,7]
# n = len(arr)
# print ("Given array is")
# for i in range(n):
#     print("%d" %arr[i])
# mergesort]]

# arr = list(map(int,input().split()))
# sort_arr = []
# for i in range(len(arr)):
#     i = min(arr)
#     sort_arr.append(i)
#     arr.remove(i)
# print(sort_arr)

# arr = list(map(int,input().split()))
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         i = min(arr)
#         arr[-1] = i

# def partition(arr,low,high):
#     pivot = arr[high]
#     i = (low-1)
#     for j in range(low,high):
#         if arr[j]<=pivot:
#             i+=1
#             arr[i],arr[j] =arr[j],arr[i]
#     arr[i+1],arr[high]=arr[high],arr[i+1]
#     return i+1
#
# def quickSort(arr, low, high):
#     if low<high:
#         pi = partition(arr,low,high)
#
#         quickSort(arr,low,pi-1)
#         quickSort(arr,pi+1,high)
#
# arr=[10,7,8,9,1,5]
# n=len(arr)
# quickSort(arr,0,n-1)
# for i in range(n):
#     print("%d" %arr[i],end=" ")

# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return 'Not prime'
#             break
#     return 'Prime'
# n = int(input())
# print(prime(n))

# def compare(field):
#     def c(l1,l2):
#         return (l1[field]>l2[field])-(li[field]<b[field])
#     return c
#
# l = [
#     ['Alicia',32],
#     ['John',40],
#     ['Mary',38],
#     ['Mark',35],
#     ['Jane',42]
# ]
# l.sort(key = lambda ll: ll[1])
# for link in l:
#     print(*link)

# def solve(arr, money):
#     for i in range(len(arr)):
#         for j in range(len(arr)-1):
#             if i !=j:
#                 if arr[i]+arr[j]==money and i<j:
#                     print(i+1,j+1)
# if __name__ == "__main__":
#     t = int(input().strip())
#     for a0 in range(t):
#         money = int(input().strip())
#         n = int(input().strip())
#         arr = list(map(int, input().strip().split(' ')))
#         solve(arr, money)

# t = int(input().strip())
# for a0 in range(t):
#     money = int(input())
#     n = int(input())
#     costlist = [int(x) for x in input().split()]
#     costhash = {}
#     for i in range(n):
#         costhash[costlist[i]]=costhash.get(costlist[i],"")+" "+str(i+1)
#     for i in costlist:
#         if (money-i) in costhash:
#             indice1 = costhash[i].split()
#             indice2 = costhash[money-i].split()
#             if (money-i)==i:
#                 print(indice1[0],indice1[1])
#                 break
#             else:
#                 print(indice1[0],indice2[0])
#                 break

# def fib(n):
#     if n<= 0: return 0
#     elif n==1: return 1
#     else: return fib(n-1)+fib(n-2)
#
# print(fib(40))
# scores = []
# score = []
# if scores == None:
#     print('0')
# for i in range(5):
#     scorestemp = [str(scores_t) for scores_t in input().strip().split()]
#     scores.append(scorestemp)
# for i in scores:
#     for j in scores:
#         if i!=j and i[0]==j[0] and i<j:
#                 avg = (int(i[1]) + int(j[1])) / 2
#                 if avg.is_integer():
#                     avg = int(avg)
#                 else:
#                     avg = "%.1f" % round(avg,1)
#                 i[1]=avg
#                 scores.remove(j)
#                 print(scores)
#     score.append(float(i[1]))
# print(max(score))

# a = float(input('Amount: '))
# b = int(input('Days: '))
# for i in range(b-1):
#     c = 2*a
#     a = c
# #     print('Day {}.'.format(i+2),a)
# import random
# n = int(input())
# for i in range(5):
#     print(random.randrange(1,n+1))
# import random
# s = input()
# for i in range(len(s)):
#     print(s[random.randrange(len(s))],end='')
# n = int(input())
# for i in range(1,n+1):
#     print(i*'#')
# print()
# for i in range(1,n+1):
#     print((n+1-i)*'#')

# days = int(input('Days worked: '))
# lessThanFive = int(input('Days where kids were less than 5: '))
# dailyWages = int(input('Amount per day: '))
# total = dailyWages*(days-lessThanFive) + (dailyWages/2)*lessThanFive
# tax= int(input('Tax: '))
# salary = ((1-(tax/100))*total)
# print("{salary:.2f}".format(**locals()))