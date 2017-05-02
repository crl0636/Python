def array_pair_sum(nums):
    return sum(sorted(nums)[::2])

if __name__ == '__main__':
    nums = [1,4,3,2]
    result = array_pair_sum(nums)
    print result