#FizzBuzz_3
def fizz_buzz(number):
    fizz_or_buzz = '' #Response Value

    if number % 3 == 0 and number % 5 == 0:
        fizz_or_buzz = 'FizzBuzz'
    elif number % 3 == 0:
        fizz_or_buzz = 'Fizz'
    elif number % 5 == 0:
        fizz_or_buzz = 'Buzz'
    else:
        fizz_or_buzz = number
    return fizz_or_buzz

def main():
    #Setting up the range to itterate through
    for x in range(1,101):
        fizz_or_buzz = fizz_buzz(x)
        #line up the messages
        if len(str(x)) > 2 :
            print(x,":   ",fizz_or_buzz,sep="")
        else:
            print(x,":    ",fizz_or_buzz,sep="")

main()
