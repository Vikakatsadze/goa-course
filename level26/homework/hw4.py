# 5) იმუშავეთ  extend  გუნქციაზე და დაწერეთ 5-5 მაგალითი

# 1
girl_names = ["tea", "lizi", "tako", "mari", "lizi", "sopia"]
boy_names = ["gela", "giorgi", "lasha", "guga", "nika", "dachi"]
girl_names.extend(boy_names)
print(girl_names)

# 2
things = ["phone", "computer", "book", "pen"]
things2 = ["cup", "plate", "coffee"]
things.extend(things2)
print(things)
# 3
nums = [1, 2, 3, 4, 5, 6]
nums2 = [7, 8, 9, 10, 11, 12]
nums.extend(nums2)
print(nums)

#4
tf = ["math", "physics"]
tf2 = ["literature", "pe"]
tf.extend(tf2)
print(tf)


#5
true = [True, False]
false = [3>1, 2<1]
true.extend(false)
print(true)