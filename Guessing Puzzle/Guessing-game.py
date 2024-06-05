import random
import tkinter as tk


def generate_puzzle(difficulty):
    if difficulty == "easy":
        return generate_easy_puzzle()
    elif difficulty == "medium":
        return generate_medium_puzzle()
    elif difficulty == "hard":
        return generate_hard_puzzle()
    else:
        raise ValueError(
            "Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'")


def generate_easy_puzzle():
    puzzle_type = random.choice(["arithmetic", "string"])
    if puzzle_type == "arithmetic":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-"])
        puzzle = f"{num1} {operator} {num2}"
        solution = eval(puzzle)
        hint = "This is an arithmetic puzzle."
    else:
        word = random.choice(["hello", "python", "coding", "challenge"])
        shuffle_word = "".join(random.sample(word, len(word)))
        puzzle = shuffle_word
        solution = word
        hint = "Rearrange the letters to form a meaningful word."

    return puzzle, solution, hint


def generate_medium_puzzle():
    puzzle_type = random.choice(["arithmetic", "string", "logical"])
    if puzzle_type == "arithmetic":
        num1 = random.randint(10, 50)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        puzzle = f"{num1} {operator} {num2}"
        solution = eval(puzzle)
        hint = "This is an arithmetic puzzle."
    elif puzzle_type == "string":
        word = random.choice(["apple", "banana", "orange", "grape"])
        num_chars_to_remove = random.randint(1, len(word) - 1)
        indices_to_remove = random.sample(
            range(len(word)), num_chars_to_remove)
        puzzle = "".join(
            c if i not in indices_to_remove else "_" for i, c in enumerate(word))
        solution = word
        hint = f"Remove {num_chars_to_remove} letter(s) to reveal the original word."
    else:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["and", "or"])
        puzzle = f"{num1} {operator} {num2}"
        solution = eval(puzzle.capitalize())
        hint = "This is a logical puzzle."

    return puzzle, solution, hint


def generate_hard_puzzle():
    puzzle_type = random.choice(["arithmetic", "string", "logical"])
    if puzzle_type == "arithmetic":
        num1 = random.randint(50, 100)
        num2 = random.randint(10, 20)
        operator = random.choice(["+", "-", "*", "/"])
        puzzle = f"{num1} {operator} {num2}"
        solution = eval(puzzle)
        hint = "This is an arithmetic puzzle."
    elif puzzle_type == "string":
        word = random.choice(["python", "programming", "challenge"])
        num_chars_to_replace = random.randint(1, len(word) - 1)
        indices_to_replace = random.sample(
            range(len(word)), num_chars_to_replace)
        replacement_chars = "".join(random.choices(
            "abcdefghijklmnopqrstuvwxyz", k=num_chars_to_replace))
        puzzle = "".join(c if i not in indices_to_replace else replacement_chars[idx]
                         for idx, c in enumerate(word))
        solution = word
        hint = f"Replace {num_chars_to_replace} letter(s) with {replacement_chars} to reveal the original word."
    else:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["and", "or", "not"])
        puzzle = f"{operator.capitalize()} {num1} == {num2}"
        solution = eval(f"{num1} {operator} {num2}")
        hint = "This is a logical puzzle."

    return puzzle, solution, hint


def check_answer():
    user_answer = entry.get().strip()
    if user_answer.lower() == "hint":
        hint_label.config(text=f"HINT: {hint}")
    else:
        try:
            user_answer = float(user_answer)
            if user_answer == solution:
                result_label.config(text="Congratulations! Your answer is correct.")
                start_game()
            else:
                attempts_left = int(attempts_label.cget("text")) - 1
                if attempts_left > 0:
                    attempts_label.config(
                        text=f"Sorry, that's incorrect. You have {attempts_left} {'attempts' if attempts_left > 1 else 'attempt'} remaining."
                    )
                else:
                    result_label.config(
                        text=f"Sorry, the correct answer is: {solution}"
                    )
                    start_game()
        except ValueError:
            result_label.config(text="Invalid input. Please enter a numeric answer.")


def start_game():
    global puzzle, solution, hint
    difficulty_level = difficulty_var.get()
    try:
        puzzle, solution, hint = generate_puzzle(difficulty_level)
        puzzle_label.config(text=f"Question: {puzzle}")
        hint_label.config(text="")
        attempts_label.config(text="3")
        result_label.config(text="")
        entry.delete(0, tk.END)
    except ValueError as e:
        result_label.config(text=e)



root = tk.Tk()
root.title("Guess Game")

frame = tk.Frame(root)
frame.pack(pady=20)

difficulty_var = tk.StringVar()
difficulty_var.set("easy")

difficulty_label = tk.Label(frame, text="Choose difficulty level:")
difficulty_label.grid(row=0, column=0, padx=10)

difficulty_menu = tk.OptionMenu(
    frame, difficulty_var, "easy", "medium", "hard")
difficulty_menu.grid(row=0, column=1)

start_button = tk.Button(
    frame, text="Start Game", command=start_game)
start_button.grid(row=0, column=2, padx=10)

puzzle_label = tk.Label(root, text="")
puzzle_label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check Answer", command=check_answer)
check_button.pack()

hint_label = tk.Label(root, text="")
hint_label.pack()

attempts_label = tk.Label(root, text="")
attempts_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
