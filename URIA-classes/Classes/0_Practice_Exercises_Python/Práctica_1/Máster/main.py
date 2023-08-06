import os
import subprocess

exercises = {
    0: (("Hello world", lambda o: o, None), ),
    1: ((246, lambda o: int(o) if o.isdigit() else False, 2), ),
    2: ((34, lambda o: round(float(o)) if o.replace(".", "").isdigit() else False, 2), ),
    3: ((11, lambda o: int(float(o)), 6), (12, lambda o: int(o), 23)),
    4: ((123, lambda o: int(float(o)), "100\n20\n3"), (90, lambda o: int(float(o)), "10\n10\n10")),
    5: (("odd", lambda o: o.lower(), 7), ("even", lambda o: o.lower(), 14)),
    6: (("Ptaeolebm 4ou", lambda o: o[::10], "Bob\n42\nBuilder"), ),
    7: ((1087, lambda o: round(float(o)) if o.replace(".", "").isdigit() else False, 18.6), ),
    8: (("Enter Paco's ageThey are the same age.", lambda o: o, 20), ("Enter Paco's ageJuan is older than Paco", lambda o: o, 15)),
    9: (("Je sie 0as 61102.0", lambda o: o[::15] + o[-5:], None), ),
		10: ((12, lambda o: int(float(o)), "4\n6"),),
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
    return f"{os.getcwd()}/exercise{exercise_no}.py"


def check_error(process):
    return not process.returncode == 0


def format_std(input):
    return input.decode("utf-8").strip()


def get_error(process):
    return format_std(process.stderr)


def get_output(process):
    return format_std(process.stdout)


def choose_exercise():
    n = input("Which exercise number would you like to run?\n0-10\n")
    if not n.isdigit() or int(n) < 0 or int(n) > 10:
        print("Valid exercise numbers are between 0 and 10.")
        exit()
    return int(n)


def run_or_check():
    resp = input("Just run the file, or execute tests? Default is run.\nrun/test\n").lower()
    return resp == "test"


if __name__ == "__main__":
    exercise_no = choose_exercise()
    check_code = run_or_check()
    if check_code:
        check_exercise(exercise_no)
    else:
        print("\n\nRunning code...\n")
        os.system(f"python {exercise_filename(exercise_no)}")
