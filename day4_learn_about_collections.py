from collections import Counter
from collections import deque
from collections import namedtuple

# without Counter function, we write these many line to find the count of each element in a list
lst = [1,2,3,4,5,1,3,5,6,2,1,4,3]
cnt= {}
for i in lst:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] = cnt[i]+1
print(cnt)
print(type(cnt))
print(cnt[1])

# with Counter function from Collections module. It's just a single line of code
cnt1 = Counter(lst)
print(cnt1) # gives Counter({1: 3, 3: 3, 2: 2, 4: 2, 5: 2, 6: 1})

print("Top Most common/frequency numbers: ", cnt1.most_common(3))
print("Print the list of all elements in the counter object: ",list(cnt1.elements()))

deduct = {3:3}
cnt1.subtract(deduct)
print("Subtract deduct from cnt1:", cnt1)

s = 'mississippi'
cnt_s= Counter(s)
print(cnt_s)

alien_0={"color":"green","speed":"medium"}
print(alien_0["color"])
print(alien_0["speed"])
alien_0["points"]=5
print(alien_0)
alien_age = alien_0.get("age","no value assigned")
print(alien_age)

languages = ['python','ruby', 'python', 'Go','c', 'java', 'java']
count_languages= Counter(languages)
print(count_languages)

lst = [1,1,2,3,3,4,4,4,4]
cnt_2=Counter(lst)
print(cnt_2)

example_tuple= ("python","Go","ruby")
print(example_tuple[1])
courses=namedtuple("courses","tech,rating")
a=courses("python",5)
print(a.tech,a.rating)

new_list = deque(["apple","kiwi","orange","banana"])
print(new_list.popleft())
print(new_list.append("mango"))
print(new_list)
