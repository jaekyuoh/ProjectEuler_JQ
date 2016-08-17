import math

def is_prime(num):
    for k in xrange(2, int(math.sqrt(num))+1):
        if num % k == 0:
            return False
    return True

def solution(N, P, Q):
    # write your code in Python 2.7

    prime_list = []
    #find Primes upto N
    for i in xrange(2,N+1):
        if is_prime(i):
            prime_list.append(i)

    print prime_list

    # prime_multi_list = []
    # for j in xrange(0,len(prime_list)):
    #     for j_prime in xrange(0,len(prime_list)):
    #         prime_multi_list.append(prime_list[j] * prime_list[j_prime])
    # print prime_multi_list
    #
    #
    # result_list = []
    # for k in range(0,len(P)): # M
    #     temp_set = set()
    #     for kk in range(0,len(prime_multi_list)):
    #         if P[k]<=prime_multi_list[kk] <= Q[k]:
    #             temp_set.add(prime_multi_list[kk])
    #     result_list.append(len(temp_set))

    #TEST
    prime_multi_set = set()
    for j in xrange(0, len(prime_list)):
        for j_prime in xrange(0, len(prime_list)):
            prime_multi_set.add(prime_list[j] * prime_list[j_prime])
    print prime_multi_set

    result_list = []
    for k in range(0, len(P)):  # M
        temp_set = set(range(P[k],Q[k]+1))
        result_list.append(len(temp_set.intersection(prime_multi_set)))

    return result_list

print solution(26,[1,4,16],[26,10,20])
print is_prime(26)