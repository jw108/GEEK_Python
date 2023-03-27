

join_to_biggest = lambda a: int(''.join(sorted(map(str, a), reverse=True)))

if __name__ == '__main__':
    print(join_to_biggest([501, 2, 1, 80, 9]))