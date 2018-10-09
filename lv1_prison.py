x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]

def answer(x, y):
    set_x = set(x)
    set_y = set(y)
    ans = set_x ^ set_y
    return ans.pop()

def main():
    print(answer(x, y))

if __name__ == '__main__':
    main()
