"""Days 1-12 study content."""

def get_days():
    return [
        {
            "day": 1,
            "title": "Working with Variables",
            "topics": ["Printing", "Comments", "Debugging intro", "String Manipulation", "Variables", "input()", "Variable Naming", "Band Name Generator"],
            "objectives": [
                "Use print() to display text and variables",
                "Write comments with # for notes and debugging",
                "Understand basic debugging: read error messages",
                "Manipulate strings with \\n and concatenation (+)",
                "Create and reassign variables",
                "Get user input with input()",
                "Follow Python naming conventions",
                "Build the Band Name Generator project"
            ],
            "explanations": [
                {"title": "Printing with print()", "body": "The print() function sends output to the console. You can print strings, numbers, and variables. Each print() call creates a new line by default.", "code": 'print("Hello, World!")\nprint(42)\nname = "Angela"\nprint(name)'},
                {"title": "Comments", "body": "Comments start with # and are ignored by Python. Use them to explain WHY code exists, not WHAT every line does.", "code": '# This program greets the user\nprint("Hi")  # inline comment'},
                {"title": "Debugging Intro", "body": "When code fails, Python shows a traceback. Read from bottom to top: the last line tells you the error type and message. Common Day 1 errors: SyntaxError (typo), NameError (undefined variable).", "code": '# NameError example:\n# print(greeting)  # greeting not defined yet\ngreeting = "Hello"\nprint(greeting)'},
                {"title": "String Manipulation", "body": "Strings use quotes. \\n creates a new line. Use + to concatenate (join) strings. input() always returns a string.", "code": 'print("Line 1\\nLine 2")\nprint("Hello" + " " + "World")\nprint("Score: " + "100")'},
                {"title": "Variables", "body": "Variables store values. Use = to assign. You can reassign: the old value is replaced.", "code": 'x = 5\nx = x + 1\nprint(x)  # 6'},
                {"title": "input()", "body": "input() pauses and waits for the user to type and press Enter. It always returns a string.", "code": 'name = input("What is your name? ")\nprint("Hello " + name)'},
                {"title": "Variable Naming", "body": "Use snake_case: lowercase with underscores. Names must start with a letter or _. Be descriptive: user_age not x.", "code": 'city_name = "London"\nuser_age = 25\n# Bad: 2name = "error"  # SyntaxError'}
            ],
            "beginner_examples": [
                {"title": "Hello User", "code": 'print("Welcome to Python!")\nname = input("Your name: ")\nprint("Hello, " + name + "!")'},
                {"title": "Multi-line Art", "code": 'print("* * *\\n * * \\n  *  ")'}
            ],
            "real_world": [
                "Receipt printers concatenate item names and prices as strings before printing.",
                "Login forms use input() to collect usernames — always validate and convert types later.",
                "Debug logs use print() during development before switching to proper logging."
            ],
            "mistakes": [
                "Forgetting quotes around text: print(Hello) causes NameError.",
                "Using wrong quote types inconsistently — pick single or double and stay consistent.",
                "Expecting input() to return a number — it always returns str.",
                "Variable names with spaces or starting with numbers."
            ],
            "best_practices": [
                "Use descriptive variable names: favorite_city not fc.",
                "One statement per line for readability.",
                "Add comments for tricky logic, not obvious prints.",
                "Test small snippets in the Python shell or a .py file."
            ],
            "memory_tricks": [
                "print = 'put on screen'",
                "input = 'I need input from human'",
                "snake_case looks like a snake on the ground: words_connected_low"
            ],
            "takeaways": [
                "print() outputs; input() reads strings from the user.",
                "Variables label values; = assigns.",
                "Strings concatenate with +; \\n adds new lines.",
                "Comments (#) and clear names make code maintainable."
            ],
            "flashcards": [
                {"q": "What does print() do?", "a": "Displays output to the console."},
                {"q": "What type does input() return?", "a": "Always a string (str)."},
                {"q": "How do you write a comment?", "a": "Start the line with #."},
                {"q": "What is string concatenation?", "a": "Joining strings with the + operator."}
            ],
            "predict": [
                {"code": 'print("A" + "B")', "answer": "AB", "explain": "+ joins strings without adding space."},
                {"code": 'x = 3\nx = 5\nprint(x)', "answer": "5", "explain": "Reassignment replaces the old value."}
            ],
            "fill_blank": [
                {"text": "To get user input use the _____ function.", "answer": "input", "alt": ["input()"]},
                {"text": "Comments in Python start with _____.", "answer": "#", "alt": []}
            ],
            "mcq": [
                {"q": "Which is a valid variable name?", "options": ["my_var", "2cool", "my-var", "class"], "answer": 0, "explain": "Names use letters, numbers, underscores; cannot start with a digit or use hyphens."},
                {"q": "print(type(input('hi'))) outputs?", "options": ["<class 'str'>", "<class 'int'>", "hi", "None"], "answer": 0, "explain": "input() always returns a string."}
            ],
            "true_false": [
                {"q": "Python variables must declare a type before use.", "answer": False, "explain": "Python is dynamically typed; types are inferred at runtime."},
                {"q": "You can reassign a variable to a different type.", "answer": True, "explain": "x = 5 then x = 'hello' is valid."}
            ],
            "matching": {"pairs": [["print()", "Display output"], ["input()", "Read user text"], ["#", "Comment"], ["+", "Concatenate strings"]]},
            "day_test": [
                {"type": "mcq", "q": "What symbol starts a comment?", "options": ["#", "//", "/*", "--"], "answer": 0, "explain": "Python uses # for comments."},
                {"type": "predict", "q": "Output?\nprint('Hi\\nThere')", "answer": "Hi\nThere", "explain": "\\n is a newline escape."},
                {"type": "tf", "q": "input() returns an integer if the user types digits.", "answer": False, "explain": "Always str; convert with int()."}
            ]
        },
        {
            "day": 2,
            "title": "Understanding Data Types",
            "topics": ["int", "float", "bool", "str", "Type Checking/Conversion", "Math Operations", "round()", "f-strings", "Tip Calculator"],
            "objectives": [
                "Identify int, float, bool, and str types",
                "Use type() and convert with int(), float(), str()",
                "Perform math: +, -, *, /, //, **, %",
                "Round numbers with round()",
                "Format strings with f-strings",
                "Build the Tip Calculator"
            ],
            "explanations": [
                {"title": "Data Types", "body": "int = whole numbers. float = decimals. bool = True/False. str = text. type() reveals the type.", "code": 'print(type(42))       # int\nprint(type(3.14))     # float\nprint(type(True))     # bool\nprint(type("hi"))     # str'},
                {"title": "Type Errors & Conversion", "body": "Mixing str and int causes TypeError. Convert explicitly: int('5'), float('3.5'), str(100).", "code": 'age = int(input("Age: "))  # convert input\nprice = float("9.99")'},
                {"title": "Math Operations", "body": "/ always returns float. // is floor division. ** is exponent. % is modulo (remainder).", "code": 'print(10 / 3)   # 3.333...\nprint(10 // 3)  # 3\nprint(2 ** 3)   # 8\nprint(10 % 3)   # 1'},
                {"title": "round()", "body": "round(number, ndigits) rounds to nearest. round(2.675, 2) can surprise due to float precision — use Decimal for money in production.", "code": 'bill = 123.456\nprint(round(bill, 2))  # 123.46'},
                {"title": "f-strings", "body": "Prefix f before quotes to embed expressions in {}. Cleaner than concatenation.", "code": 'name = "Sam"\nscore = 95\nprint(f"{name} scored {score}%")'}
            ],
            "beginner_examples": [
                {"title": "BMI Calculator snippet", "code": 'height = float(input("Height m: "))\nweight = float(input("Weight kg: "))\nbmi = weight / (height ** 2)\nprint(f"Your BMI is {bmi:.1f}")'},
                {"title": "Split bill", "code": 'total = float(input("Bill: "))\npeople = int(input("People: "))\nprint(f"Each pays ${total/people:.2f}")'}
            ],
            "real_world": [
                "E-commerce stores use float for prices but round for display.",
                "Forms convert input strings to int/float before calculations.",
                "f-strings power email templates: f'Hello {user.name}'."
            ],
            "mistakes": [
                "Forgetting int() on input before math: '5' + '3' = '53' not 8.",
                "Using / when you need integer division — use //.",
                "Comparing floats with == — use round or math.isclose."
            ],
            "best_practices": [
                "Convert input immediately after reading.",
                "Use f-strings for formatted output.",
                "Use meaningful names: bill_amount not b."
            ],
            "memory_tricks": [
                "int = Integer = whole. float = floating decimal point.",
                "f-string = 'formatted string' — put f before quotes.",
                "// = floor division — double slash 'cuts down'."
            ],
            "takeaways": [
                "Four core types: int, float, bool, str.",
                "Always convert input before numeric operations.",
                "f-strings are the preferred formatting method.",
                "round() controls decimal display."
            ],
            "flashcards": [
                {"q": "What does int('7') return?", "a": "The integer 7."},
                {"q": "Result of 10 % 3?", "a": "1 (remainder)."},
                {"q": "What prefix creates an f-string?", "a": "f before the opening quote: f\"...\""}
            ],
            "predict": [
                {"code": 'print(type(10 / 2))', "answer": "<class 'float'>", "explain": "Division / always returns float in Python 3."},
                {"code": 'print(f"{2+2}")', "answer": "4", "explain": "Expressions inside {} are evaluated."}
            ],
            "fill_blank": [
                {"text": "Convert a string to integer with _____.", "answer": "int", "alt": ["int()"]},
                {"text": "The modulo operator symbol is _____.", "answer": "%", "alt": []}
            ],
            "mcq": [
                {"q": "Which converts '3.14' to float?", "options": ["float('3.14')", "int('3.14')", "str(3.14)", "bool('3.14')"], "answer": 0, "explain": "float() parses decimal strings."},
                {"q": "10 // 3 equals?", "options": ["3", "3.33", "4", "1"], "answer": 0, "explain": "// is floor division."}
            ],
            "true_false": [
                {"q": "bool('False') is False.", "answer": False, "explain": "Non-empty strings are truthy; bool('False') is True."},
                {"q": "f'{5*2}' prints 10.", "answer": True, "explain": "Expression 5*2 evaluates to 10."}
            ],
            "matching": {"pairs": [["int()", "Whole number"], ["float()", "Decimal"], ["str()", "Text"], ["bool()", "True/False"]]},
            "day_test": [
                {"type": "mcq", "q": "Type of 5 + 5.0?", "options": ["float", "int", "str", "bool"], "answer": 0, "explain": "int + float promotes to float."},
                {"type": "predict", "q": "print(int('9') + 1)", "answer": "10", "explain": "int converts then adds."},
                {"type": "fill", "q": "round(4.567, 2) = ?", "answer": "4.57", "explain": "Rounded to 2 decimal places."}
            ]
        },
        {
            "day": 3,
            "title": "Control Flow & Logical Operators",
            "topics": ["if/else", "modulo %", "nesting/elif", "multiple ifs", "Python Pizza", "and/or/not", "Treasure Island"],
            "objectives": [
                "Write if, elif, else blocks with proper indentation",
                "Use % to test even/odd and cycles",
                "Nest conditions and combine with and/or/not",
                "Understand multiple independent if vs elif chain",
                "Complete Python Pizza and Treasure Island logic"
            ],
            "explanations": [
                {"title": "if / else", "body": "Run code only when a condition is True. else runs when the if condition is False. Indentation (4 spaces) defines blocks.", "code": 'age = 18\nif age >= 18:\n    print("Adult")\nelse:\n    print("Minor")'},
                {"title": "Modulo %", "body": "Returns remainder. number % 2 == 0 means even. Useful for cycles and wrapping values.", "code": 'for i in range(5):\n    print(i % 2)  # 0,1,0,1,0'},
                {"title": "elif and Nesting", "body": "elif checks another condition if previous failed. Nest if inside if for multi-step decisions.", "code": 'score = 85\nif score >= 90:\n    grade = "A"\nelif score >= 80:\n    grade = "B"\nelse:\n    grade = "C"'},
                {"title": "Multiple ifs vs elif", "body": "Separate if statements can all run. elif chain stops after first match.", "code": '# Multiple ifs — both can print\n# elif — only one branch runs'},
                {"title": "Logical Operators", "body": "and = both True. or = either True. not = flips boolean.", "code": 'if age >= 18 and has_id:\n    print("Enter")\nif is_weekend or is_holiday:\n    print("Relax")'}
            ],
            "beginner_examples": [
                {"title": "Odd or Even", "code": 'n = int(input("Number: "))\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")'},
                {"title": "Leap year check (simplified)", "code": 'year = int(input("Year: "))\nif year % 4 == 0:\n    print("Leap year")\nelse:\n    print("Not leap")'}
            ],
            "real_world": [
                "Payment systems: if balance >= amount and card_valid: process.",
                "Traffic lights: elif chains for state machines.",
                "Games: modulo for cycling through sprite frames."
            ],
            "mistakes": [
                "Missing colon after if/elif/else.",
                "Wrong indentation — Python uses indentation for blocks.",
                "Using = instead of == for comparison.",
                "Confusing elif chain with separate if statements."
            ],
            "best_practices": [
                "Keep conditions readable; extract complex logic to variables.",
                "Prefer elif over nested if when branches are mutually exclusive.",
                "Use parentheses for clarity in compound conditions."
            ],
            "memory_tricks": [
                "== compares, = assigns — 'double equals checks equality'",
                "elif = 'else if' — next chance",
                "not flips True↔False like a light switch"
            ],
            "takeaways": [
                "Indentation defines code blocks.",
                "% gives remainder — key for even/odd.",
                "and/or/not combine boolean expressions.",
                "elif stops after first true branch."
            ],
            "flashcards": [
                {"q": "What does 7 % 2 equal?", "a": "1"},
                {"q": "Difference between if and elif?", "a": "elif only runs if previous conditions were False."},
                {"q": "What operator checks equality?", "a": "=="}
            ],
            "predict": [
                {"code": 'x = 10\nif x > 5:\n    print("A")\nif x > 8:\n    print("B")', "answer": "A\nB", "explain": "Two separate ifs — both conditions true."},
                {"code": 'print(not True)', "answer": "False", "explain": "not inverts boolean."}
            ],
            "fill_blank": [
                {"text": "The else clause runs when the if condition is _____.", "answer": "False", "alt": ["false"]},
                {"text": "Combine two conditions that must both be true with _____.", "answer": "and", "alt": []}
            ],
            "mcq": [
                {"q": "Which is valid?", "options": ["if x == 5:", "if x = 5:", "if x === 5:", "if x == 5"], "answer": 0, "explain": "Colon required; == for comparison."},
                {"q": "5 % 2 == 0 is?", "options": ["False", "True", "1", "Error"], "answer": 0, "explain": "5 % 2 is 1, not 0."}
            ],
            "true_false": [
                {"q": "An if block can exist without else.", "answer": True, "explain": "else is optional."},
                {"q": "elif runs even if the if was True.", "answer": False, "explain": "elif skipped when if matches."}
            ],
            "matching": {"pairs": [["==", "Equal to"], ["and", "Both true"], ["or", "Either true"], ["not", "Invert boolean"]]},
            "day_test": [
                {"type": "mcq", "q": "Best for mutually exclusive grades?", "options": ["if/elif/else chain", "three separate ifs", "while loop", "for loop"], "answer": 0, "explain": "elif ensures one grade only."},
                {"type": "predict", "q": "if False:\n  print('x')\nelse:\n  print('y')", "answer": "y", "explain": "else runs when if is False."},
                {"type": "tf", "q": "not (5 > 3) is True", "answer": False, "explain": "5>3 is True; not True is False."}
            ]
        },
        {
            "day": 4,
            "title": "Randomization & Lists",
            "topics": ["random module", "lists", "indexing/slicing", "IndexError", "Banker Roulette", "Rock Paper Scissors"],
            "objectives": [
                "Import random and use randint, choice, shuffle",
                "Create and modify lists",
                "Access elements by index; slice sublists",
                "Avoid and handle IndexError",
                "Build Banker Roulette and Rock Paper Scissors"
            ],
            "explanations": [
                {"title": "random module", "body": "import random gives pseudo-random numbers. randint(a,b) inclusive. choice(list) picks one item. shuffle mutates list in place.", "code": 'import random\nprint(random.randint(1, 6))\nprint(random.choice(["rock", "paper", "scissors"]))'},
                {"title": "Lists", "body": "Ordered, mutable collections in []. Can hold mixed types. len() gets length.", "code": 'fruits = ["apple", "banana", "cherry"]\nfruits.append("date")\nprint(fruits[0])'},
                {"title": "Indexing & Slicing", "body": "Index from 0. Negative index from end: -1 is last. slice [start:stop:step] — stop excluded.", "code": 'nums = [10, 20, 30, 40]\nprint(nums[1])    # 20\nprint(nums[-1])   # 40\nprint(nums[1:3])  # [20, 30]'},
                {"title": "IndexError", "body": "Accessing invalid index raises IndexError. Valid indices: 0 to len-1.", "code": 'items = ["a", "b"]\n# items[5]  # IndexError\nif len(items) > 2:\n    print(items[2])'}
            ],
            "beginner_examples": [
                {"title": "Dice roll", "code": 'import random\nroll = random.randint(1, 6)\nprint(f"You rolled {roll}")'},
                {"title": "First and last", "code": 'scores = [88, 92, 76]\nprint(f"First: {scores[0]}, Last: {scores[-1]}")'}
            ],
            "real_world": [
                "Shuffle playlists with random.shuffle.",
                "A/B testing picks random variant with choice.",
                "Leaderboards store scores in lists sorted by index or sort()."
            ],
            "mistakes": [
                "Off-by-one: last index is len(list)-1 not len(list).",
                "Modifying list while iterating.",
                "Forgetting import random."
            ],
            "best_practices": [
                "Use choice for fair random selection from options.",
                "Check bounds before indexing user-provided positions.",
                "Use descriptive list names: player_names not n."
            ],
            "memory_tricks": [
                "Index 0 = first — 'computers count from zero'",
                "-1 = last item — 'go back one from the end'",
                "[1:3] includes index 1,2 not 3 — 'stop is exclusive'"
            ],
            "takeaways": [
                "Lists are ordered and mutable.",
                "random.choice and randint power games.",
                "Negative indices access from the end.",
                "IndexError means index out of range."
            ],
            "flashcards": [
                {"q": "Index of first list element?", "a": "0"},
                {"q": "What does random.choice do?", "a": "Returns one random element from a sequence."},
                {"q": "nums[-1] gets?", "a": "The last element."}
            ],
            "predict": [
                {"code": 'a = [1,2,3]\nprint(a[1:])', "answer": "[2, 3]", "explain": "Slice from index 1 to end."},
                {"code": 'print(["a","b"][1])', "answer": "b", "explain": "Index 1 is second element."}
            ],
            "fill_blank": [
                {"text": "Lists are written with _____ brackets.", "answer": "[", "alt": ["[]", "square"]},
                {"text": "Import random with: import _____.", "answer": "random", "alt": []}
            ],
            "mcq": [
                {"q": "len([1,2,3])?", "options": ["3", "2", "4", "Error"], "answer": 0, "explain": "Three elements."},
                {"q": "Valid index for ['x']?", "options": ["0", "1", "-2", "2"], "answer": 0, "explain": "Only index 0 exists."}
            ],
            "true_false": [
                {"q": "Lists can contain different data types.", "answer": True, "explain": "[1, 'a', True] is valid."},
                {"q": "Slicing includes the stop index.", "answer": False, "explain": "Stop is exclusive."}
            ],
            "matching": {"pairs": [["append()", "Add to end"], ["len()", "List length"], ["randint()", "Random integer"], ["choice()", "Random pick"]]},
            "day_test": [
                {"type": "mcq", "q": "Pick random list item?", "options": ["random.choice", "random.randint", "list.pick", "random.select"], "answer": 0, "explain": "choice selects from sequence."},
                {"type": "predict", "q": "print([0,1,2][-2])", "answer": "1", "explain": "-2 is second from end."},
                {"type": "tf", "q": "Index 3 is valid for length-3 list.", "answer": False, "explain": "Valid: 0,1,2 only."}
            ]
        },
        {
            "day": 5,
            "title": "Loops",
            "topics": ["for loops", "highest score", "range()", "Password Generator"],
            "objectives": [
                "Iterate with for item in sequence",
                "Use range() for counted loops",
                "Find max without max() to understand loops",
                "Build Password Generator with loops and random"
            ],
            "explanations": [
                {"title": "for loops", "body": "for variable in iterable: runs once per item. Works with lists, strings, range(), etc.", "code": 'for letter in "Python":\n    print(letter)'},
                {"title": "Finding highest score", "body": "Initialize a tracker, loop and compare each value.", "code": 'scores = [21, 55, 43, 89, 12]\nhighest = 0\nfor s in scores:\n    if s > highest:\n        highest = s\nprint(highest)'},
                {"title": "range()", "body": "range(n) → 0..n-1. range(start, stop). range(start, stop, step).", "code": 'for i in range(5):\n    print(i)  # 0-4\nfor j in range(2, 10, 2):\n    print(j)  # 2,4,6,8'}
            ],
            "beginner_examples": [
                {"title": "Sum numbers", "code": 'total = 0\nfor n in [1, 2, 3, 4]:\n    total += n\nprint(total)  # 10'},
                {"title": "Multiplication table", "code": 'n = 7\nfor i in range(1, 11):\n    print(f"{n} x {i} = {n*i}")'}
            ],
            "real_world": [
                "Email batch sends loop over recipient lists.",
                "Report generators iterate rows in CSV data.",
                "Password generators loop to append random chars."
            ],
            "mistakes": [
                "Off-by-one with range — range(5) is 0-4 not 1-5.",
                "Forgetting to update accumulator in max/sum loops.",
                "Infinite loops when range step is wrong sign."
            ],
            "best_practices": [
                "Use meaningful loop variables: for score in scores.",
                "Prefer sum(), max(), min() when learning is done — know the loop logic first.",
                "Keep loop bodies focused — extract complex logic to functions."
            ],
            "memory_tricks": [
                "for = 'for each item do this'",
                "range stop is exclusive — same as slicing",
                "highest starts low (0 or first item) then climbs"
            ],
            "takeaways": [
                "for loops iterate sequences.",
                "range() generates number sequences.",
                "Accumulators solve max/sum/count problems.",
                "Loops + random build password generators."
            ],
            "flashcards": [
                {"q": "range(3) produces?", "a": "0, 1, 2"},
                {"q": "How to loop a list?", "a": "for item in my_list:"},
                {"q": "range(1,5) includes 5?", "a": "No — stop is exclusive."}
            ],
            "predict": [
                {"code": 's=0\nfor i in range(1,4):\n  s+=i\nprint(s)', "answer": "6", "explain": "1+2+3=6."},
                {"code": 'print(list(range(0,10,3)))', "answer": "[0, 3, 6, 9]", "explain": "Step by 3."}
            ],
            "fill_blank": [
                {"text": "A _____ loop repeats for each item in a sequence.", "answer": "for", "alt": []},
                {"text": "range(5) generates numbers from 0 to _____.", "answer": "4", "alt": []}
            ],
            "mcq": [
                {"q": "How many iterations: for _ in range(10)?", "options": ["10", "9", "11", "0"], "answer": 0, "explain": "0 through 9 = 10 times."},
                {"q": "Best to find max in list manually?", "options": ["Loop with if > tracker", "while True", "print(max)", "if/else only"], "answer": 0, "explain": "Classic accumulator pattern."}
            ],
            "true_false": [
                {"q": "You can nest for loops.", "answer": True, "explain": "Common for grids and combinations."},
                {"q": "range(5,5) runs once.", "answer": False, "explain": "Empty range — zero iterations."}
            ],
            "matching": {"pairs": [["for", "Iterate items"], ["range()", "Number sequence"], ["+=", "Add and assign"], ["len()", "Count items"]]},
            "day_test": [
                {"type": "mcq", "q": "range(2,8,2) yields?", "options": ["2,4,6", "2,4,6,8", "2,3,4,5,6,7", "2,8"], "answer": 0, "explain": "Even numbers below 8."},
                {"type": "predict", "q": "x=1\nfor i in range(3):\n  x*=2\nprint(x)", "answer": "8", "explain": "1*2*2*2=8."},
                {"type": "tf", "q": "for loops require range().", "answer": False, "explain": "Can iterate any iterable."}
            ]
        },
        {
            "day": 6,
            "title": "Functions & While Loops",
            "topics": ["Functions", "def", "code blocks", "while loops", "Karel"],
            "objectives": [
                "Define functions with def and call them",
                "Understand indentation as code blocks",
                "Use while loops for condition-based repetition",
                "Apply functions to Karel-style problems"
            ],
            "explanations": [
                {"title": "Functions with def", "body": "Functions bundle reusable code. def name(): defines; call with name(). Parameters come in parentheses.", "code": 'def greet():\n    print("Hello!")\n\ngreet()'},
                {"title": "Code Blocks", "body": "Indented lines belong to the function, loop, or if above them. Consistent 4-space indentation is required.", "code": 'def double(n):\n    result = n * 2\n    return result'},
                {"title": "while loops", "body": "Repeats while condition is True. Must eventually become False or infinite loop.", "code": 'count = 0\nwhile count < 3:\n    print(count)\n    count += 1'}
            ],
            "beginner_examples": [
                {"title": "Square function", "code": 'def square(n):\n    return n * n\nprint(square(5))  # 25'},
                {"title": "Countdown", "code": 'n = 5\nwhile n > 0:\n    print(n)\n    n -= 1\nprint("Blastoff!")'}
            ],
            "real_world": [
                "Game main loops: while game_running: update().",
                "Retry logic: while not success and attempts < 3.",
                "Karel teaches decomposition — turn_left() as reusable steps."
            ],
            "mistakes": [
                "Forgetting colon after def and while.",
                "Infinite while — condition never becomes False.",
                "Not calling function — defining doesn't run it."
            ],
            "best_practices": [
                "Functions should do one thing well.",
                "Use while for unknown iteration count; for for known sequences.",
                "Update loop variables inside while body."
            ],
            "memory_tricks": [
                "def = 'define' a function",
                "while = 'while this is true, keep going'",
                "Call function = use its name with ()"
            ],
            "takeaways": [
                "def creates reusable blocks.",
                "while repeats until condition is False.",
                "Indentation defines scope of blocks.",
                "Functions reduce duplication (DRY)."
            ],
            "flashcards": [
                {"q": "Keyword to define a function?", "a": "def"},
                {"q": "while runs until?", "a": "Condition becomes False."},
                {"q": "Does def run the function?", "a": "No — you must call it."}
            ],
            "predict": [
                {"code": 'def f():\n  return 1\nprint(f())', "answer": "1", "explain": "Call returns 1."},
                {"code": 'i=0\nwhile i<2:\n  i+=1\nprint(i)', "answer": "2", "explain": "Loop while 0,1 then stops at 2."}
            ],
            "fill_blank": [
                {"text": "Define a function with the _____ keyword.", "answer": "def", "alt": []},
                {"text": "A _____ loop repeats while a condition is true.", "answer": "while", "alt": []}
            ],
            "mcq": [
                {"q": "Infinite loop risk?", "options": ["while True: pass without break", "for i in range(3)", "def f(): return", "if True: print(1)"], "answer": 0, "explain": "True never becomes False."},
                {"q": "Function purpose?", "options": ["Reuse code", "Store files", "Compile Python", "Delete variables"], "answer": 0, "explain": "DRY principle."}
            ],
            "true_false": [
                {"q": "Functions must have return.", "answer": False, "explain": "Returns None implicitly if no return."},
                {"q": "while 0: runs forever.", "answer": False, "explain": "0 is falsy — loop never runs."}
            ],
            "matching": {"pairs": [["def", "Define function"], ["while", "Conditional loop"], ["return", "Send value back"], ["()", "Call function"]]},
            "day_test": [
                {"type": "mcq", "q": "Call function named jump?", "options": ["jump()", "call jump", "def jump", "jump;"], "answer": 0, "explain": "Name followed by parentheses."},
                {"type": "predict", "q": "def hi():\n  print('Hi')\nhi()", "answer": "Hi", "explain": "Function call executes body."},
                {"type": "tf", "q": "Indentation is optional in Python.", "answer": False, "explain": "Indentation is syntactically required."}
            ]
        },
        {
            "day": 7,
            "title": "Hangman Project",
            "topics": ["Hangman steps", "Word selection", "Guessing loop", "Lives", "Display", "Win/Lose"],
            "objectives": [
                "Plan Hangman before coding",
                "Use random word + list of letters",
                "Implement guess loop with lives",
                "Display progress and ASCII art stages",
                "Handle win/lose conditions"
            ],
            "explanations": [
                {"title": "Project Steps Overview", "body": "1) Pick random word. 2) Create placeholder display (_ _ _). 3) Loop: ask letter, check in word, update display or lose life. 4) Win when all letters guessed; lose at 0 lives.", "code": '# Pseudocode:\n# word = random.choice(words)\n# lives = 6\n# while not won and lives > 0:\n#     guess = input(...)\n#     # update state'},
                {"title": "Tracking Guessed Letters", "body": "Keep a list or string of guessed letters to prevent duplicate guesses and validate input.", "code": 'guessed = []\nif letter in guessed:\n    print("Already guessed")\nelse:\n    guessed.append(letter)'},
                {"title": "Building the Display", "body": "Loop through word chars: show letter if guessed else underscore.", "code": 'display = ""\nfor char in word:\n    display += char if char in guessed else "_"\n    display += " "'}
            ],
            "beginner_examples": [
                {"title": "Check letter in word", "code": 'word = "python"\nletter = "p"\nif letter in word:\n    print("Found!")\nelse:\n    print("Miss")'},
                {"title": "Lives counter", "code": 'lives = 6\nlives -= 1\nprint(f"Lives left: {lives}")'}
            ],
            "real_world": [
                "Word games share guess/validate/display pattern.",
                "Limited attempts model API rate limits or login tries.",
                "State machines (win/lose/playing) appear in many apps."
            ],
            "mistakes": [
                "Not lowercasing input — 'P' vs 'p' mismatch.",
                "Forgetting to check already-guessed letters.",
                "Modifying loop variable instead of game state."
            ],
            "best_practices": [
                "Break into functions: display_word(), check_guess(), update_lives().",
                "Use constants for MAX_LIVES and WORD_LIST.",
                "Test with short words first."
            ],
            "memory_tricks": [
                "Hangman = loop + list + if + lives — combine Days 1-6",
                "underscore display = 'hidden answer template'",
                "lives-- each wrong guess"
            ],
            "takeaways": [
                "Hangman combines loops, lists, strings, conditionals.",
                "Track game state: word, guessed, lives, won.",
                "Decompose into small functions.",
                "Validate user input every iteration."
            ],
            "flashcards": [
                {"q": "How pick random word?", "a": "random.choice(word_list)"},
                {"q": "Check if letter in word?", "a": "letter in word"},
                {"q": "Typical starting lives?", "a": "6 (varies by implementation)"}
            ],
            "predict": [
                {"code": 'word="cat"\nprint("a" in word)', "answer": "True", "explain": "'a' is in 'cat'."},
                {"code": 'lives=3\nlives-=1\nprint(lives)', "answer": "2", "explain": "Decrement lives."}
            ],
            "fill_blank": [
                {"text": "Use _____ to check membership in a string.", "answer": "in", "alt": []},
                {"text": "Hangman uses a _____ loop for repeated guesses.", "answer": "while", "alt": []}
            ],
            "mcq": [
                {"q": "Prevent duplicate guesses with?", "options": ["List of guessed letters", "print twice", "random.shuffle", "del word"], "answer": 0, "explain": "Track what's been tried."},
                {"q": "Win condition?", "options": ["All letters revealed", "lives > 100", "word deleted", "input empty"], "answer": 0, "explain": "All chars in guessed set."}
            ],
            "true_false": [
                {"q": "Hangman requires OOP.", "answer": False, "explain": "Procedural approach works fine."},
                {"q": "'in' works on strings.", "answer": True, "explain": "Substring/char membership."}
            ],
            "matching": {"pairs": [["random.choice", "Pick word"], ["while", "Game loop"], ["in", "Letter check"], ["lives", "Attempts left"]]},
            "day_test": [
                {"type": "mcq", "q": "Show hidden word progress?", "options": ["Loop chars show _ or letter", "print word always", "delete word", "input only"], "answer": 0, "explain": "Classic display pattern."},
                {"type": "predict", "q": "print('hello' in 'help')", "answer": "False", "explain": "'hello' not substring of 'help'."},
                {"type": "tf", "q": "Guess same letter twice should cost 2 lives.", "answer": False, "explain": "Usually penalize once or ignore duplicate."}
            ]
        },
        {
            "day": 8,
            "title": "Function Parameters",
            "topics": ["Parameters", "Positional vs keyword args", "Caesar Cipher"],
            "objectives": [
                "Define functions with parameters",
                "Use positional and keyword arguments",
                "Understand default parameter values",
                "Build Caesar Cipher encode/decode"
            ],
            "explanations": [
                {"title": "Function Parameters", "body": "Parameters receive arguments when called. They act as local variables.", "code": 'def greet(name):\n    print(f"Hello {name}")\n\ngreet("Angela")'},
                {"title": "Positional vs Keyword", "body": "Positional: order matters. Keyword: name=value, order flexible.", "code": 'def describe(pet, age):\n    print(f"{pet} is {age}")\n\ndescribe("dog", 3)\ndescribe(age=5, pet="cat")'},
                {"title": "Caesar Cipher Logic", "body": "Shift each letter by n positions in alphabet. Wrap z→a using modulo. decode uses negative shift.", "code": 'def shift_char(char, amount):\n    if char.isalpha():\n        base = ord("a") if char.islower() else ord("A")\n        return chr((ord(char)-base+amount)%26+base)\n    return char'}
            ],
            "beginner_examples": [
                {"title": "Add two numbers", "code": 'def add(a, b):\n    return a + b\nprint(add(2, 3))'},
                {"title": "Default parameter", "code": 'def power(base, exp=2):\n    return base ** exp\nprint(power(5))  # 25'}
            ],
            "real_world": [
                "API functions use keyword args for clarity: requests.get(url, timeout=5).",
                "Encryption demos teach param passing and string processing.",
                "Formatting functions: format_price(amount, currency='USD')."
            ],
            "mistakes": [
                "Argument order wrong for positional params.",
                "Mutable default args (list=[]) — use None instead.",
                "Confusing parameter names at call site."
            ],
            "best_practices": [
                "Use keyword args for optional settings.",
                "Keep parameter count small; use dict for many options.",
                "Name parameters clearly: shift_amount not n."
            ],
            "memory_tricks": [
                "Positional = position in line matters",
                "Keyword = key=name unlocks order",
                "Caesar shift = alphabet carousel with % 26"
            ],
            "takeaways": [
                "Parameters make functions flexible.",
                "Keyword args improve readability.",
                "Caesar cipher applies modular arithmetic to chars.",
                "ord/chr convert char ↔ ASCII code."
            ],
            "flashcards": [
                {"q": "Positional args rely on?", "a": "Order of arguments."},
                {"q": "Keyword arg syntax?", "a": "name=value at call site."},
                {"q": "Wrap alphabet with?", "a": "Modulo 26."}
            ],
            "predict": [
                {"code": 'def f(a,b=10):\n  return a+b\nprint(f(5))', "answer": "15", "explain": "b defaults to 10."},
                {"code": 'def g(x,y):\n  return x*y\nprint(g(y=2,x=3))', "answer": "6", "explain": "Keyword order flexible."}
            ],
            "fill_blank": [
                {"text": "Values passed to functions are called _____.", "answer": "arguments", "alt": ["args"]},
                {"text": "Caesar cipher shifts letters along the _____.", "answer": "alphabet", "alt": []}
            ],
            "mcq": [
                {"q": "describe(age=4, pet='bird') uses?", "options": ["Keyword arguments", "Positional only", "Global vars", "Import"], "answer": 0, "explain": "Named at call site."},
                {"q": "ord('a') returns?", "options": ["97", "0", "'a'", "Error"], "answer": 0, "explain": "ASCII/Unicode code point."}
            ],
            "true_false": [
                {"q": "Functions can have default parameter values.", "answer": True, "explain": "def f(x=1): valid."},
                {"q": "Keyword args must come before positional.", "answer": False, "explain": "Positional first, then keyword."}
            ],
            "matching": {"pairs": [["parameter", "Function variable"], ["argument", "Call-time value"], ["ord()", "Char to code"], ["chr()", "Code to char"]]},
            "day_test": [
                {"type": "mcq", "q": "Decode = encode with?", "options": ["Negative shift", "Same shift", "print", "input"], "answer": 0, "explain": "Reverse the shift amount."},
                {"type": "predict", "q": "def h(n=2):\n return n**2\nprint(h(3))", "answer": "9", "explain": "3 overrides default."},
                {"type": "tf", "q": "More params always means better code.", "answer": False, "explain": "Simplicity wins when possible."}
            ]
        },
        {
            "day": 9,
            "title": "Dictionaries",
            "topics": ["Dictionaries", "Nesting", "Secret Auction"],
            "objectives": [
                "Create dicts with keys and values",
                "Access, add, update, delete entries",
                "Nest dicts and lists",
                "Build Secret Auction bidding logic"
            ],
            "explanations": [
                {"title": "Dictionaries", "body": "Key-value pairs in {key: value}. Keys are unique. Access with brackets or .get().", "code": 'student = {"name": "Lee", "score": 92}\nprint(student["name"])\nprint(student.get("grade", "N/A"))'},
                {"title": "Adding & Updating", "body": "Assign new key to add. Existing key overwrites.", "code": 'bids = {}\nbids["Alice"] = 100\nbids["Bob"] = 150\nbids["Alice"] = 120  # update'},
                {"title": "Nesting", "body": "Values can be lists, dicts, etc. Travel log: country → cities visited.", "code": 'travel = {"France": ["Paris", "Lyon"], "Japan": ["Tokyo"]}'},
                {"title": "Secret Auction Pattern", "body": "Loop bidders: name + bid amount. Track highest bid and winner. Clear screen between bidders (os.system).", "code": '# winner = \"\"\n# high = 0\n# for each bidder:\n#   if bid > high: high = bid; winner = name'}
            ],
            "beginner_examples": [
                {"title": "Phone book", "code": 'contacts = {"Mom": "555-0100", "Dad": "555-0101"}\nprint(contacts["Mom"])'},
                {"title": "Loop dict items", "code": 'scores = {"Ana": 90, "Ben": 85}\nfor name, score in scores.items():\n    print(f"{name}: {score}")'}
            ],
            "real_world": [
                "JSON APIs map directly to Python dicts.",
                "User profiles: {id, name, settings: {...}}.",
                "Auction/eBay highest bid tracking."
            ],
            "mistakes": [
                "KeyError when key missing — use .get() or check 'in'.",
                "Using mutable objects as keys (lists can't be keys).",
                "Confusing keys and values in .items() loop."
            ],
            "best_practices": [
                "Use descriptive keys: user_name not n.",
                ".get(key, default) for safe access.",
                "dict.items() for key-value iteration."
            ],
            "memory_tricks": [
                "dict = real dictionary: word → definition",
                "curly braces {} hold key: value pairs",
                "items() gives both key AND value"
            ],
            "takeaways": [
                "Dicts map keys to values — fast lookup.",
                "Nesting models real-world structured data.",
                "Auction finds max via loop over bids dict.",
                ".get() avoids KeyError."
            ],
            "flashcards": [
                {"q": "Syntax for dict?", "a": "{key: value}"},
                {"q": "Safe access missing key?", "a": "dict.get(key, default)"},
                {"q": "Loop key and value?", "a": "for k, v in d.items():"}
            ],
            "predict": [
                {"code": 'd={"a":1}\nd["b"]=2\nprint(len(d))', "answer": "2", "explain": "Two keys now."},
                {"code": 'print({"x":10}.get("y",0))', "answer": "0", "explain": "Default when key missing."}
            ],
            "fill_blank": [
                {"text": "Dict entries use key _____ value separator.", "answer": ":", "alt": []},
                {"text": "Method to loop keys and values: _____.", "answer": "items", "alt": ["items()"]}
            ],
            "mcq": [
                {"q": "Valid dict key?", "options": ["'name'", "[1,2]", "{1:2}", "3.14"], "answer": 0, "explain": "Strings, numbers, tuples OK; lists not."},
                {"q": "Find highest bid in dict values?", "options": ["Loop and compare", "dict.sort()", "keys only", "del dict"], "answer": 0, "explain": "Track max while iterating."}
            ],
            "true_false": [
                {"q": "Dict keys must be strings.", "answer": False, "explain": "Immutable hashable types work."},
                {"q": "Nesting dicts is valid.", "answer": True, "explain": "Common for JSON-like data."}
            ],
            "matching": {"pairs": [["{}", "Dictionary literal"], [".get()", "Safe lookup"], [".items()", "Key-value pairs"], ["KeyError", "Missing key with []"]]},
            "day_test": [
                {"type": "mcq", "q": "Add new entry?", "options": ["d[key]=value", "d.add()", "d.push()", "append d"], "answer": 0, "explain": "Bracket assignment."},
                {"type": "predict", "q": "d={'a':1,'b':2}\nprint(d['a'])", "answer": "1", "explain": "Key lookup."},
                {"type": "tf", "q": "Lists can be dict keys.", "answer": False, "explain": "Lists are unhashable."}
            ]
        },
        {
            "day": 10,
            "title": "Return Values & Calculator",
            "topics": ["return", "Multiple returns", "Docstrings", "Calculator project"],
            "objectives": [
                "Return values from functions",
                "Return multiple values as tuples",
                "Write docstrings for documentation",
                "Build multi-operation Calculator"
            ],
            "explanations": [
                {"title": "return", "body": "return sends a value back to caller and exits the function immediately.", "code": 'def add(n1, n2):\n    return n1 + n2\nresult = add(3, 4)\nprint(result)  # 7'},
                {"title": "Multiple Return Values", "body": "Return comma-separated values — Python packs them as a tuple.", "code": 'def min_max(nums):\n    return min(nums), max(nums)\nlo, hi = min_max([1, 5, 3])'},
                {"title": "Docstrings", "body": "First string in function is docstring — documents purpose. Access via help() or __doc__.", "code": 'def multiply(a, b):\n    """Return product of a and b."""\n    return a * b'},
                {"title": "Calculator Project", "body": "Loop: show operations, take input, call operation functions, continue until user stops.", "code": 'def add(a,b): return a+b\ndef subtract(a,b): return a-b\n# operations dict maps symbols to functions'}
            ],
            "beginner_examples": [
                {"title": "Is even function", "code": 'def is_even(n):\n    return n % 2 == 0\nprint(is_even(4))  # True'},
                {"title": "Unpack tuple return", "code": 'def divide(a, b):\n    return a // b, a % b\nq, r = divide(17, 5)'}
            ],
            "real_world": [
                "Functions return status codes + data: (True, result) or (False, error).",
                "Docstrings power auto-generated API docs.",
                "Calculators map operators to functions in a dict."
            ],
            "mistakes": [
                "Printing instead of returning — caller gets None.",
                "Code after return never runs (unreachable).",
                "Forgetting to unpack multiple returns."
            ],
            "best_practices": [
                "Return values; let caller decide to print.",
                "Write docstrings for public functions.",
                "Calculator: separate ops into pure functions."
            ],
            "memory_tricks": [
                "return = 'send back' the result",
                "tuple unpack: a, b = func() catches multiple",
                '"""triple quotes""" = function manual'
            ],
            "takeaways": [
                "return provides function output.",
                "Multiple values returned as tuple.",
                "Docstrings document behavior.",
                "Calculator combines dict + functions + loop."
            ],
            "flashcards": [
                {"q": "Function without return returns?", "a": "None"},
                {"q": "Docstring delimiter?", "a": "Triple quotes \"\"\" ... \"\"\""},
                {"q": "Unpack (3, 5)?", "a": "a, b = func() gives a=3, b=5"}
            ],
            "predict": [
                {"code": 'def f():\n  return 1\n  return 2\nprint(f())', "answer": "1", "explain": "First return exits."},
                {"code": 'def g():\n  pass\nprint(g())', "answer": "None", "explain": "No return → None."}
            ],
            "fill_blank": [
                {"text": "_____ sends a value back from a function.", "answer": "return", "alt": []},
                {"text": "Documentation string inside function uses _____ quotes.", "answer": "triple", "alt": ['"""', "three"]}
            ],
            "mcq": [
                {"q": "Calculator pattern stores ops in?", "options": ["Dict of symbol→function", "Global only", "Comments", "CSV"], "answer": 0, "explain": "operations['+'] = add"},
                {"q": "help(func) shows?", "options": ["Docstring", "Bytecode", "Memory", "Imports"], "answer": 0, "explain": "Docstring documentation."}
            ],
            "true_false": [
                {"q": "print and return are the same.", "answer": False, "explain": "print displays; return gives value to caller."},
                {"q": "return can send back multiple values.", "answer": True, "explain": "As a tuple."}
            ],
            "matching": {"pairs": [["return", "Output value"], ["docstring", "Function docs"], ["tuple unpack", "Multiple returns"], ["None", "No explicit return"]]},
            "day_test": [
                {"type": "mcq", "q": "Best for reusable math?", "options": ["return result", "print only", "global var", "pass"], "answer": 0, "explain": "Caller uses returned value."},
                {"type": "predict", "q": "def h():\n return 2,3\nprint(h())", "answer": "(2, 3)", "explain": "Tuple returned."},
                {"type": "tf", "q": "Docstrings must be on line 2.", "answer": False, "explain": "First statement in body."}
            ]
        },
        {
            "day": 11,
            "title": "Blackjack Project",
            "topics": ["Blackjack rules", "Cards", "Score", "Hit/Stand", "Dealer", "Ace handling"],
            "objectives": [
                "Model cards and deck with lists/random",
                "Calculate hand value with Ace logic",
                "Implement hit/stand game loop",
                "Compare player vs dealer hands",
                "Apply all Days 1-10 concepts"
            ],
            "explanations": [
                {"title": "Blackjack Overview", "body": "Goal: get closer to 21 than dealer without busting. Face cards = 10, Ace = 1 or 11. Player hits or stands; dealer hits until 17+.", "code": '# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]\n# deal from random.choice(cards)'},
                {"title": "Hand Score with Aces", "body": "Sum cards; if ace count > 0 and total <= 11, add 10 (switch ace from 1 to 11). Repeat if multiple aces.", "code": 'def score(hand):\n    s = sum(hand)\n    if 11 in hand and s <= 11:\n        s += 10\n    return s'},
                {"title": "Game Loop", "body": "Deal 2 cards each. Loop: hit (append card, check bust) or stand. Dealer draws while score < 17. Compare scores.", "code": 'while True:\n    choice = input("h to hit, s to stand: ")\n    if choice == "s":\n        break'}
            ],
            "beginner_examples": [
                {"title": "Deal one card", "code": 'import random\ncards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]\nhand = [random.choice(cards), random.choice(cards)]\nprint(hand)'},
                {"title": "Simple bust check", "code": 'def score(h):\n    return sum(h)\nif score(hand) > 21:\n    print("Bust")'}
            ],
            "real_world": [
                "State machines model game phases: deal, play, settle.",
                "Score calculation with special rules mirrors pricing rules.",
                "Random sampling simulates shuffled decks."
            ],
            "mistakes": [
                "Ace always 11 — causes instant bust.",
                "Not looping dealer draws to 17.",
                "Comparing hands before player stands."
            ],
            "best_practices": [
                "Functions: deal_card(), calculate_score(), compare().",
                "Constants for deck and thresholds.",
                "Test ace edge cases: A+A, A+10."
            ],
            "memory_tricks": [
                "Blackjack = 21 — combine random + list + while + functions",
                "Ace flex: 1 or 11 — 'Ace adapts'",
                "Dealer stands on 17"
            ],
            "takeaways": [
                "Blackjack integrates the full beginner toolkit.",
                "Ace handling is the trickiest logic.",
                "Dealer follows fixed rules; player chooses.",
                "Modular functions keep game readable."
            ],
            "flashcards": [
                {"q": "Face card value?", "a": "10"},
                {"q": "Player bust means?", "a": "Score over 21 — lose"},
                {"q": "Dealer hits until?", "a": "Score >= 17 (typical rule)"}
            ],
            "predict": [
                {"code": 'hand=[10,11]\nprint(sum(hand))', "answer": "21", "explain": "11 is Ace as 11 in simplified deck."},
                {"code": 'print(21>21)', "answer": "False", "explain": "Not bust at exactly 21."}
            ],
            "fill_blank": [
                {"text": "Going over 21 is called a _____.", "answer": "bust", "alt": []},
                {"text": "Deal cards with random._____(cards).", "answer": "choice", "alt": ["choice()"]}
            ],
            "mcq": [
                {"q": "Best structure for deck?", "options": ["List of card values", "Single int", "Empty dict", "while only"], "answer": 0, "explain": "List + random.choice."},
                {"q": "After stand, who plays?", "options": ["Dealer", "Player again", "Nobody", "Random"], "answer": 0, "explain": "Dealer turn follows."}
            ],
            "true_false": [
                {"q": "Blackjack requires classes.", "answer": False, "explain": "Procedural solution works."},
                {"q": "Ace can count as 1 or 11.", "answer": True, "explain": "Pick best for hand."}
            ],
            "matching": {"pairs": [["Hit", "Take another card"], ["Stand", "Keep hand"], ["Bust", "Over 21"], ["21", "Blackjack target"]]},
            "day_test": [
                {"type": "mcq", "q": "Player at 20 should usually?", "options": ["Stand", "Hit", "Deal", "Shuffle"], "answer": 0, "explain": "High bust risk on hit."},
                {"type": "predict", "q": "scores: player 22", "answer": "Bust/Lose", "explain": "Over 21 loses."},
                {"type": "tf", "q": "Dealer always hits on 20.", "answer": False, "explain": "Stands at 17+."}
            ]
        },
        {
            "day": 12,
            "title": "Scope & Number Guessing Game",
            "topics": ["Namespaces", "Block scope", "Global vars", "Global constants", "Number Guessing Game"],
            "objectives": [
                "Understand local vs global scope",
                "Use global keyword to modify globals",
                "Define module-level constants",
                "Build Number Guessing Game with attempts/lives",
                "Apply logo art and difficulty levels"
            ],
            "explanations": [
                {"title": "Namespaces & Scope", "body": "Variables exist in namespaces. Local = inside function. Global = module level. Python looks local first, then enclosing, global, builtin (LEGB).", "code": 'count = 0  # global\n\ndef increment():\n    global count\n    count += 1'},
                {"title": "Block Scope", "body": "if/for/while blocks share the same function/module scope — Python has no separate block scope like C.", "code": 'if True:\n    message = "hi"\nprint(message)  # works at same level'},
                {"title": "Global Constants", "body": "Constants in ALL_CAPS at top: MAX_LIVES = 5. Convention — don't reassign.", "code": 'EASY_ATTEMPTS = 10\nHARD_ATTEMPTS = 5\nLOGO = "🎯"'},
                {"title": "Number Guessing Game", "body": "Pick random 1-100. User guesses; hint higher/lower. Track attempts. Easy vs hard mode sets max attempts.", "code": 'import random\nanswer = random.randint(1, 100)\nattempts = 0\nwhile attempts < max_attempts:\n    guess = int(input("Guess: "))\n    attempts += 1'}
            ],
            "beginner_examples": [
                {"title": "Local shadows global", "code": 'x = 1\ndef f():\n    x = 2  # local\n    print(x)\nf()  # 2\nprint(x)  # 1'},
                {"title": "Guessing hints", "code": 'if guess < answer:\n    print("Too low")\nelif guess > answer:\n    print("Too high")\nelse:\n    print("Correct!")'}
            ],
            "real_world": [
                "Config constants: API_URL, MAX_RETRIES at module level.",
                "Games use scope for score visible across functions via global or return.",
                "Avoid globals in large apps — prefer passing parameters."
            ],
            "mistakes": [
                "Using global when return parameter would be cleaner.",
                "UnboundLocalError: assign to name makes it local without global.",
                "Reassigning constants — breaks convention."
            ],
            "best_practices": [
                "Minimize global; prefer function args and returns.",
                "Use ALL_CAPS for true constants.",
                "Encapsulate game state in functions."
            ],
            "memory_tricks": [
                "LEGB = Local Enclosing Global Builtin — search order",
                "global keyword = 'I mean THE global one'",
                "ALL_CAPS = 'do not touch' constant"
            ],
            "takeaways": [
                "Local vars die when function ends (unless returned).",
                "global needed to modify module-level vars inside functions.",
                "Constants configure game difficulty.",
                "Number guessing combines scope, random, while, if."
            ],
            "flashcards": [
                {"q": "Modify global inside function?", "a": "Use global keyword before name."},
                {"q": "Constant naming convention?", "a": "ALL_CAPS_WITH_UNDERSCORES"},
                {"q": "LEGB stands for?", "a": "Local, Enclosing, Global, Builtin"}
            ],
            "predict": [
                {"code": 'n=5\ndef f():\n  n=1\n  print(n)\nf()\nprint(n)', "answer": "1\n5", "explain": "Local n doesn't change global."},
                {"code": 'def g():\n  return 42\nprint(g())', "answer": "42", "explain": "Return to caller."}
            ],
            "fill_blank": [
                {"text": "Keyword to modify a global variable: _____.", "answer": "global", "alt": []},
                {"text": "Constants are usually written in _____.", "answer": "ALL_CAPS", "alt": ["uppercase", "all caps"]}
            ],
            "mcq": [
                {"q": "UnboundLocalError often from?", "options": ["Assigning to name before global decl", "Using print", "import random", "Comments"], "answer": 0, "explain": "Assignment makes name local."},
                {"q": "Best practice for game score?", "options": ["Return/pass as param vs excessive global", "Only globals", "No variables", "Delete score"], "answer": 0, "explain": "Limit global state."}
            ],
            "true_false": [
                {"q": "Python has block-only scope like Java.", "answer": False, "explain": "Function/module scope only."},
                {"q": "random.randint(1,100) inclusive both ends.", "answer": True, "explain": "Both endpoints included."}
            ],
            "matching": {"pairs": [["local", "Inside function"], ["global", "Module level"], ["global keyword", "Modify module var"], ["ALL_CAPS", "Constant convention"]]},
            "day_test": [
                {"type": "mcq", "q": "Too high/too low game uses?", "options": ["if/elif/else", "only for", "dict only", "import os"], "answer": 0, "explain": "Compare guess to answer."},
                {"type": "predict", "q": "EASY=10\nprint(EASY)", "answer": "10", "explain": "Constant access."},
                {"type": "tf", "q": "Every function variable is global.", "answer": False, "explain": "Default is local."}
            ]
        }
    ]
