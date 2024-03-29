import os
import subprocess

identity = lambda i: i
as_int = lambda i: int(float(i))

exercises = {
    0: (('Cris', identity, None),),
    1: ((179.75, identity, None),),
    2: (("Mara", identity, None),),
    3: ((5, as_int, None),),
    4: ((75, as_int, None),),
    5: (("# Some bots are known to be trouble, particularly those designed to copy", identity, None),),
    6: (("Antonio es la persona más mayor. Tiene 85 años\nVictor es la persona más joven. Tiene 9 años", identity, None),),
		7: (("Antonio es la persona más mayor. Tiene 85 años\nVictor es la persona más joven. Tiene 9 años", identity, None),),
		8:((datetime.date.today(),identity,None),),
		9:(( "{'t': 4, 'r': 3, 'e': 3, 's': 4, ' ': 2, 'i': 2, 'g': 1}", identity ,None),),
    10: ((),),
}

def check_exercise(exercise_no):
    print(f"\nChecking exercise number {exercise_no}.")
    exercise, results = run_tests(exercise_no)
    display_feedback(*results, exercise)


def run_tests(exercise_no):
    exercise = exercises[exercise_no]
    processes = [process_exercise(exercise_no, input) for desired, parse, input in exercise]
    errors = [check_error(process) for process in processes]
    outputs = [get_output(process) for process in processes]
    checks = [desired == parse(output) for output, (desired, parse, input) in zip(outputs, exercise)]
    return exercise, (errors, outputs, checks)


def display_feedback(errors, outputs, checks, exercise):
    for error, output, check, (desired, parse, input) in zip(errors, outputs, checks, exercise):
        if error:
            print("\nOh no! Error!\n" + "*" * 40 + "\n")
            print(error)
        else:
            print(f"\n\nInput given to file:\t{input}")
            print(f"Output expected:\t\t{desired}")
            print(f"Output received:\t\t{output}\n")
            if check:
                print("Correct output received.")
            else:
                print("Incorrect output.")
                # print(parse(output))
    
    if all(checks):
        message = "All tests passed. Well done!"
        colour = "\033[92m"
    else:
        message = "Not all tests have passed."
        colour = "\033[93m"

    print(colour, end="")
    print(f"\n\n{'*' * (len(message) + 6)}")
    print(f"*{' ' * (len(message) + 4)}*")
    print(f"*  {message}  *")
    print(f"*{' ' * (len(message) + 4)}*")
    print(f"{'*' * (len(message) + 6)}")


def process_exercise(exercise_no, input=None):
    kwargs = { "shell": True, "capture_output": True }
    if input:
        kwargs["input"] = bytes(str(input), "utf-8")
    filename = exercise_filename(exercise_no)
    return subprocess.run(f"python {filename}", **kwargs)


def exercise_filename(exercise_no):
    return f"{os.getcwd()}/exercise{exercise_no:02}.py"


def check_error(process):
    return not process.returncode == 0


def format_std(input):
    return input.decode("utf-8").strip()


def get_error(process):
    return format_std(process.stderr)


def get_output(process):
    return format_std(process.stdout)


def choose_exercise():
    n = input(f"Which exercise number would you like to run?\n0-{total}\n")
    if not n.isdigit() or int(n) < 0 or int(n) > total:
        print(f"Valid exercise numbers are between 0 and {total}.")
        exit()
    return int(n)


def run_or_check():
    resp = input("Just run the file, or execute tests? Default is run.\nrun/test\n").lower()
    return resp == "test"


if __name__ == "__main__":
    # for i in range(11, 8, -1):
    #     os.rename(exercise_filename(i), exercise_filename(i + 1))


    total = 11
    exercise_no = choose_exercise()
    check_code = run_or_check()
    if check_code:
        check_exercise(exercise_no)
    else:
        print("\n\nRunning code...\n")
        os.system(f"python {exercise_filename(exercise_no)}")
