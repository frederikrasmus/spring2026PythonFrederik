
# Solution from video https://www.youtube.com/watch?v=XKu_SEDAykw&t=379s
# [1, 2, 4, 4] => sum = 8
# [1, 2, 3, 9] => sum = 8


def simple_solution(l):
    """ Loops through all numbers - linier search"""
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 8:
                #print(l[i] + l[j])
                return True
            #print(l[i] + l[j])
        # print('=====')
    return False


def has_pair_with_sum(l, sum):

    low = 0
    high = len(l)-1

    while low < high:

        s = l[low] + l[high]

        if s == sum:
            return True
        elif s > sum:
            high -= 1
        elif s < sum:
            low += 1

    return False


def has_pair_with_sum_ordered(l, sum):
    comp = set()
    for i in l:
        if i in comp:
            return True
        comp.add(sum - i)

    return False


# what if return should be all possiple pairs that sum to 8


def main():
    res = simple_solution([1, 2, 4, 4])
    print(res)

    res = has_pair_with_sum([1, 2, 4, 9], 8)
    print(res)


if __name__ == "__main__":
    main()
