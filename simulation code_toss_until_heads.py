#random number generator for toss until heads task, created by Robin, for Preshil, in 2021
import random
#task 1
n=500 #number of trials
list_all=[] #to contain all the toss outcomes
list_count_h=[] #to contain the number of heads in each trial
list_count_t=[] #to contain the number of tails in each trial
for i in range(n):
    alist=[random.randint(0,1)] #the first toss outcome here
    while alist[-1]!=1:
        alist.append(random.randint(0,1))
    list_all.append(alist)
    list_count_h.append(alist.count(1))
    list_count_t.append(alist.count(0))
total_head=sum(list_count_h) #the total number of heads for all the trials
total_tail=sum(list_count_t) #the total number of tails for all the trials
print('In task 1, the {} outcomes are: {}'.format(n, list_all))
print('There are {} heads and {} tails totally'.format(total_head, total_tail))

#task 2
list_all_2=[]
list_count_head=[]
list_count_tail=[]
for i in range(n):
    alist_2=[random.randint(0,1)]
    if alist_2[0]!=1:
        alist_2.append(random.randint(0,1))
    list_all_2.append(alist_2)
    list_count_head.append(alist_2.count(1))
    list_count_tail.append(alist_2.count(0))
total_2_head=sum(list_count_head) #the total number of heads for all the trials
total_2_tail=sum(list_count_tail) #the total number of tails for all the trials
print('In task 2, the {} outcomes are: {}'.format(n, list_all_2))
print('There are {} heads and {} tails totally'.format(total_2_head, total_2_tail))