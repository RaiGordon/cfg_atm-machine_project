pin_attempt = ""
line_divider = "\n••••••••••••••••••••\n"
goodbye = (f"{line_divider} GOODBYE {line_divider}")
curr_bal_msg = "Your current balance is £"
curr_balance = 100
remaining_attempts = 2
yes = "yes"
no = "no"
re_try = "yes"
bad_pin = (f"{line_divider}ERROR: You entered the wrong pin. {line_divider}")
bad_length = (f"{line_divider}ERROR: Your pin must be 4 digits. {line_divider}")


#----------------EXCEPTION CLASSES----------------#

class BadPinTryAgain(Exception):
    pass
class BadPinEndProgram(Exception):
    pass
class BadLength(Exception):
    pass

#----------------SERVICES OPTIONS FUNCTION----------------#
# gives user for choice between withdraw and exit

def options():
    global re_try
    options = int(input(f"{line_divider}What would you like to do? \n \n (1) Withdraw Cash \n (2) Exit \n Choose option: "))
    if options == 2:
        print(goodbye)
        re_try = no
        return
    elif options == 1:
        withdraw()
        return
    else:
        print(f"{line_divider}please enter a valid choice")


#----------------WITHDRAW CASH FUNCTION----------------#
    #  check curr bal > than withdrawal amt request
    #  if curr bal < withdrawal amt :- raise insufficient funds error msg
    #  If withdrawal amt <= curr bal :- deduct amt
    #  Finally:- end program

def withdraw():
    global re_try
    global curr_balance

    try:
        withdrawal_amt = int(input(f"{line_divider}How much cash would you like to withdraw?: "))
        assert curr_balance >= withdrawal_amt
    except AssertionError:
        print(f"{line_divider}You have insufficient funds.")
        print(f"Your balance is £{curr_balance}{line_divider}\nGoodbye")
        re_try = no
    else:
        curr_balance = curr_balance - withdrawal_amt
        print(f"{line_divider}{curr_bal_msg}{curr_balance}")
        options()
    finally:
        re_try = no

#----------------CHECK PIN FUNCT---------------#
# Length of pin input must be 4 digits
# if pin correct :- call options() function
# if pin incorrect :- raise exception errors


def check_pin(pin_attempt):
    global tries
    global remaining_attempts
    correct_pin = "2021"
    # pin_attempt = input("Enter your pin: ")

    assert len(str(pin_attempt)) == 4

    if pin_attempt == correct_pin:
        options()
    else:
        if pin_attempt != correct_pin:
            if remaining_attempts == 2 or remaining_attempts == 1:
                raise BadPinTryAgain
            elif remaining_attempts == 0:
                raise BadPinEndProgram

#----------------START PROGRAM---------------#
#  Allow 3 tries of pin entry only.
#  Length of pin < 4 digits error
#  1 (or) 2 bad pin attempts :- error (count tries remaining,
#  3 bad pins entered error :- terminate program

while remaining_attempts >=0 and re_try == yes:
    try:
        check_pin(input("Enter your pin: "))

    except AssertionError:
        remaining_attempts -= 1
        print (bad_length)
        pin_attempt = ""

    except BadPinTryAgain:
        remaining_attempts -= 1
        print(bad_pin)
        pin_attempt = ""
        print(pin_attempt)

    except BadPinEndProgram:
        status = (f"{line_divider}PIN ENTERED INCORRECTLY 3 TIMES.\n \nGOODBYE.{line_divider}")
        print(status)