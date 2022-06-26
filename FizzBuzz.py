#FizzBuzz_2
def fizz_buzz(number):
    response = ''
    if number % 3 == 0 and number % 5 == 0:
        response = 'FizzBuzz'
    elif number % 3 == 0:
        response = 'Fizz'
    elif number % 5 == 0:
        response = 'Buzz'
    else:
        response = number
    return response

def main():
    for x in range(1,101):
        response = fizz_buzz(x)
        if len(str(x)) > 2 :
            print(x,":   ",response,sep="")
        else:
            print(x,":    ",response,sep="")

main()
