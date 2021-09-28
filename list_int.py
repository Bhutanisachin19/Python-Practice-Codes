#python code tht returen only int from a list

my_list = [1,2,"hello","1.5",5.0,5,"one",96,4.5]
int_list = []
for i in my_list:
 if(type(i) == int):
  int_list.append(i)


for a in int_list:
 print(a)

