letters = ["A","B","C","D"]
A = letters[3]
D = letters[0]

letters[3] = D
letters[0] = A

print(letters)


numbers = [1,2,3,4,5]
numbers.append(6)
numbers.remove(3)
numbers.insert(0,-1)
numbers.remove(5)

print(numbers)

fruits = ["มะนาว","มะม่วง","ลำไย","ส้ม","แก้วมังกร"]
fruits.insert(3,"มะเขือเทศ")
fruits.insert(0,"Shinchan")
fruits.remove("มะม่วง")
fruits.insert(2,"Ultraman")
order_2 = fruits[2]
order_4 = fruits[4]
fruits[2] = order_4
fruits[4] = order_2


print(fruits)