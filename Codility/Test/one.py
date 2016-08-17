def solution(N):
    # write your code in Python 2.7
    number_list = range(1,N+1)
    for num in number_list:
        if num % 105 == 0:
            print 'FizzBuzzWoof'
        elif num % 35 == 0:
            print 'BuzzWoof'
        elif num % 21 == 0:
            print 'FizzWoof'
        elif num % 15 == 0:
            print 'FizzBuzz'
        elif num % 7 == 0:
            print 'Woof'
        elif num % 5 == 0:
            print 'Buzz'
        elif num % 3 == 0:
            print 'Fizz'
        else:
            print num


solution(25)