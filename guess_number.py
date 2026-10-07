import random

def main():
    # 1. 电脑随机生成一个 1-100 的整数
    answer = random.randint(1, 100)
    count = 0  # 记录猜的次数

    print("=== 猜数字小游戏 ===")
    print("我已经想好了一个 1-100 之间的数字，快来猜吧！")

    # 2. 循环让用户猜测，直到猜中
    while True:
        try:
            guess = int(input("请输入你猜的数字："))
        except ValueError:
            print("请输入一个整数！")
            continue

        count += 1  # 每猜一次计数 +1

        # 3. 判断大小
        if guess > answer:
            print("大了")
        elif guess < answer:
            print("小了")
        else:
            print(f"恭喜你猜中了！答案是 {answer}")
            print(f"你一共猜了 {count} 次。")
            break  # 猜中后跳出循环

if __name__ == "__main__":
    main()