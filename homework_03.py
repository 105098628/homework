import random

num = random.randint(1, 100)
guess = 0

start = 1
end = 100

while True:
    guess = int(input('請輸入{}~{}之間的數字來猜數 : '.format(start, end)))
    if guess == num:
        print('你猜對了，數字是 : ', num)
        break
    elif guess > num:
        end = guess
    else:
        start = guess