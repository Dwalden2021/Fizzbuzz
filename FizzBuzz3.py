#FizzBuzz

def fizz_buzz(number):
    answer = ''
    if number % 3 == 0 and number % 5 == 0:
        answer = 'FizzBuzz'
    elif number % 3 == 0:
        answer = 'Fizz'
    elif number % 5 == 0:
        answer = 'Buzz'
    else:
        answer = number
    return answer

def main():
    for x in range(1,101):
        answer = fizz_buzz(x)
        print(answer)

main()
