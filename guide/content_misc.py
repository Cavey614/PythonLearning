"""Review topics, projects, study plan, and final exam."""

def get_review():
    return [
        {"id": "variables", "title": "Variables", "summary": "Names that reference values. Assigned with =. Use snake_case. Can be reassigned and change type.", "key_points": ["print() and input()", "Reassignment replaces value", "Descriptive names", "input() returns str"], "code": 'name = "Alex"\nage = 25\nage = 26  # reassignment'},
        {"id": "data-types", "title": "Data Types", "summary": "int, float, bool, str — check with type(), convert with int/float/str/bool.", "key_points": ["Four core types", "Type conversion before math", "bool truthiness", "TypeError when mixing wrong types"], "code": 'n = int("42")\nprice = float("9.99")\nactive = True'},
        {"id": "strings", "title": "Strings", "summary": "Text in quotes. Concatenate with + or f-strings. Escape \\n for newline.", "key_points": ["f-strings preferred", "\\n newline", "input() is str", "String methods: lower(), isalpha()"], "code": 'msg = f"Hello {name}"\nprint("Line1\\nLine2")'},
        {"id": "conditionals", "title": "Conditionals", "summary": "if/elif/else with indentation. == compares. and/or/not combine conditions.", "key_points": ["Colon + indent", "elif chain", "Modulo for even/odd", "Separate if vs elif"], "code": 'if score >= 90:\n    print("A")\nelif score >= 80:\n    print("B")'},
        {"id": "lists", "title": "Lists", "summary": "Ordered mutable []. Index from 0. Negative indices from end. Slicing [start:stop].", "key_points": ["append(), len()", "IndexError out of range", "Mixed types allowed", "Mutable"], "code": 'items = [1, 2, 3]\nitems.append(4)\nprint(items[-1])'},
        {"id": "loops", "title": "Loops", "summary": "for iterates sequences. while repeats while True. range() for counted loops.", "key_points": ["Accumulator pattern", "range stop exclusive", "Update loop vars in while", "Nested loops OK"], "code": 'for i in range(5):\n    print(i)\nwhile n > 0:\n    n -= 1'},
        {"id": "functions", "title": "Functions", "summary": "def defines reusable blocks. Parameters, return, docstrings. Positional vs keyword args.", "key_points": ["def + call()", "return vs print", "Default params", "Multiple return = tuple"], "code": 'def add(a, b=0):\n    """Sum two numbers."""\n    return a + b'},
        {"id": "dictionaries", "title": "Dictionaries", "summary": "Key-value {k: v}. Fast lookup. .get() safe access. .items() for loops. Nesting common.", "key_points": ["Unique keys", "KeyError with []", "Nesting dicts/lists", "Auction bid tracking"], "code": 'user = {"name": "Sam", "score": 88}\nprint(user.get("id", 0))'},
        {"id": "scope", "title": "Scope", "summary": "Local inside functions. Global at module level. global keyword to modify. ALL_CAPS constants.", "key_points": ["LEGB rule", "UnboundLocalError", "Minimize globals", "Constants at top"], "code": 'MAX = 100\ndef f():\n    global count\n    count += 1'},
        {"id": "randomization", "title": "Randomization", "summary": "import random. randint(a,b), choice(seq), shuffle(list). Powers games and simulations.", "key_points": ["Pseudo-random", "choice for games", "randint inclusive", "Combine with loops"], "code": 'import random\nprint(random.randint(1, 6))\nprint(random.choice(["A","B"]))'},
        {"id": "debugging", "title": "Debugging", "summary": "Read tracebacks bottom-up. Common errors: SyntaxError, NameError, TypeError, IndexError, IndentationError.", "key_points": ["Read error message", "Print debugging", "Check types and indices", "Test small pieces"], "code": '# NameError: variable not defined\n# TypeError: wrong operation on type\n# IndexError: bad list index'}
    ]


def get_projects():
    return [
        {"name": "Band Name Generator", "day": 1, "concepts": ["input", "variables", "string concatenation"], "steps": ["Greet user", "Ask city name", "Ask pet name", "Combine into band name with f-string or +", "Print result"], "extension": "Add random adjective from a list."},
        {"name": "Tip Calculator", "day": 2, "concepts": ["float", "int", "math", "f-strings"], "steps": ["Get bill total", "Get tip percentage", "Get number of people", "Calculate tip amount", "Split per person with round()", "Display formatted totals"], "extension": "Validate input > 0."},
        {"name": "Python Pizza", "day": 3, "concepts": ["if/elif", "nested conditions"], "steps": ["Show menu prices S/M/L", "Ask size", "Ask pepperoni Y/N", "Ask extra cheese Y/N", "Add costs with nested if", "Print final bill"], "extension": "Add toppings menu dict."},
        {"name": "Treasure Island", "day": 3, "concepts": ["if/elif/else", "logical operators", "nested decisions"], "steps": ["Print story intro", "Left/right choice", "Swim/wait choice", "Which door", "Win/lose endings"], "extension": "Add score or replay loop."},
        {"name": "Banker Roulette", "day": 4, "concepts": ["random.choice", "lists"], "steps": ["Create friends list", "Use random.choice to pick payer", "Print result"], "extension": "Exclude someone who already paid."},
        {"name": "Rock Paper Scissors", "day": 4, "concepts": ["random", "lists", "conditionals"], "steps": ["Get user choice", "Computer random choice", "Compare win/lose/draw rules", "Print outcome"], "extension": "Best of 3 loop."},
        {"name": "Password Generator", "day": 5, "concepts": ["for loop", "range", "random"], "steps": ["Ask letter/symbol/number counts", "Build char pools", "Loop to pick random chars", "Shuffle or combine password", "Print password"], "extension": "Ensure min length 8."},
        {"name": "Hangman", "day": 7, "concepts": ["while", "lists", "strings", "random"], "steps": ["Pick random word", "Initialize display and lives", "Guess loop", "Check letter in word", "Update display or deduct life", "ASCII art stages", "Win/lose messages"], "extension": "Difficulty levels by word length."},
        {"name": "Caesar Cipher", "day": 8, "concepts": ["functions", "parameters", "ord/chr", "modulo"], "steps": ["Define encode function with shift", "Handle upper/lowercase", "Preserve non-letters", "Define decode with negative shift", "Menu: encode/decode"], "extension": "Brute-force all 26 shifts."},
        {"name": "Secret Auction", "day": 9, "concepts": ["dict", "loops", "max tracking"], "steps": ["Print logo", "Ask bidder count", "Loop: name + bid", "Clear screen between bidders", "Track highest bid and winner", "Announce winner"], "extension": "Validate bid > previous high."},
        {"name": "Calculator", "day": 10, "concepts": ["functions", "return", "dict of operations"], "steps": ["Define add/subtract/multiply/divide", "Map symbols to functions", "Loop: num1, op, num2", "Call function and print", "Continue until user stops"], "extension": "Handle divide by zero."},
        {"name": "Blackjack", "day": 11, "concepts": ["all prior topics"], "steps": ["Deck as list", "deal_card function", "calculate_score with aces", "Player hit/stand loop", "Dealer auto-play to 17", "Compare and declare winner"], "extension": "Track chips across rounds."},
        {"name": "Number Guessing Game", "day": 12, "concepts": ["scope", "constants", "random", "while"], "steps": ["Print logo", "Choose Easy/Hard attempts", "Random 1-100", "Loop guesses with hints", "Track attempts", "Win/lose message"], "extension": "Play again without restart."}
    ]


def get_study_plan():
    return {
        "title": "7-Day Intensive Study Plan (Days 1-12)",
        "overview": "Cover 12 course days in 7 calendar days with spaced repetition, active recall, and project practice.",
        "days": [
            {"day": 1, "focus": "Days 1-2: Foundations", "schedule": ["Morning: Day 1 content + flashcards (30 min)", "Midday: Band Name Generator from scratch (45 min)", "Afternoon: Day 2 types/math/f-strings (30 min)", "Evening: Tip Calculator + review quiz (45 min)"], "memorize": ["print vs input", "Four data types", "int/float conversion", "f-string syntax"], "practice": ["3 predict-output drills", "Write tip calc without looking"], "repeat": "Review Day 1 flashcards before sleep"},
            {"day": 2, "focus": "Day 3: Conditionals", "schedule": ["Morning: if/elif/else + logical ops (40 min)", "Midday: Python Pizza project (40 min)", "Afternoon: Treasure Island (40 min)", "Evening: Day 1-2 spaced review (20 min)"], "memorize": ["== vs =", "and/or/not truth tables", "% for even/odd"], "practice": ["5 conditional MCQs", "Write grade calculator"], "repeat": "Redo 2 missed Day 1-2 questions"},
            {"day": 3, "focus": "Days 4-5: Lists & Loops", "schedule": ["Morning: random + lists (40 min)", "Midday: Banker Roulette + RPS (50 min)", "Afternoon: for/range + Password Gen (50 min)", "Evening: Review lists & loops topics (20 min)"], "memorize": ["Index 0 and -1", "range stop exclusive", "random.choice"], "practice": ["Find max without max()", "Build password gen"], "repeat": "Flashcards: indexing + range"},
            {"day": 4, "focus": "Days 6-7: Functions & Hangman", "schedule": ["Morning: def + while loops (40 min)", "Midday: Karel-style function drills (30 min)", "Afternoon: Hangman step-by-step build (90 min)", "Evening: Day 3-5 review quiz (30 min)"], "memorize": ["def/call/return", "while exit condition", "in operator"], "practice": ["Hangman MVP", "3 function writing prompts"], "repeat": "Explain Hangman loop aloud"},
            {"day": 5, "focus": "Days 8-9: Params & Dicts", "schedule": ["Morning: positional/keyword args (30 min)", "Midday: Caesar Cipher (60 min)", "Afternoon: dicts + Secret Auction (60 min)", "Evening: Review functions + dicts (30 min)"], "memorize": [".get() vs []", "items() loop", "ord/chr shift"], "practice": ["Encode/decode message", "Auction with 3 bidders"], "repeat": "Dict flashcards + Day 6 review"},
            {"day": 6, "focus": "Days 10-11: Returns & Blackjack", "schedule": ["Morning: return + docstrings (30 min)", "Midday: Calculator project (45 min)", "Afternoon: Blackjack full build (90 min)", "Evening: Weak topic drill (30 min)"], "memorize": ["return vs print", "Tuple unpacking", "Ace score logic"], "practice": ["Calculator with 4 ops", "Blackjack hit/stand"], "repeat": "All project names → concepts"},
            {"day": 7, "focus": "Day 12 + Final Review & Exam", "schedule": ["Morning: Scope + constants (30 min)", "Midday: Number Guessing Game (45 min)", "Afternoon: Full review section all topics (60 min)", "Evening: Final 100-question exam (90 min)"], "memorize": ["global keyword", "LEGB", "ALL_CAPS constants"], "practice": ["Number guessing easy/hard", "Complete final exam"], "repeat": "Spaced recap: Days 1, 4, 7, 10 flashcards"}
        ],
        "spaced_repetition": ["Day N: learn new material", "Day N+1: 15 min review previous day", "Day N+3: redo missed quizzes", "Day N+7: final exam covers all"],
        "goals": ["Complete all 11+ projects", "Score 80%+ on final exam", "Explain any Day 1-12 concept without notes", "Debug 5 common error types confidently"]
    }


def get_exam():
    """Generate 100 exam questions."""
    qs = []
    # MCQ batch
    mcq_data = [
        ("What does input() return?", ["str", "int", "float", "bool"], 0, "input always returns string."),
        ("Valid variable name?", ["user_name", "1user", "user-name", "class"], 0, "snake_case, no leading digit."),
        ("Comment symbol?", ["#", "//", "--", "/*"], 0, "Python uses #."),
        ("Type of 10/2 in Python 3?", ["float", "int", "str", "bool"], 0, "/ always float."),
        ("10 // 3 equals?", ["3", "3.33", "4", "1"], 0, "Floor division."),
        ("10 % 3 equals?", ["1", "3", "0", "3.33"], 0, "Remainder 1."),
        ("bool('') is?", ["False", "True", "None", "Error"], 0, "Empty string falsy."),
        ("f'{2*3}' prints?", ["6", "2*3", "23", "Error"], 0, "Expression evaluated."),
        ("if requires?", ["colon and indent", "semicolon", "braces", "then keyword"], 0, "Python syntax."),
        ("== means?", ["equal comparison", "assignment", "approx equal", "identity"], 0, "Comparison operator."),
        ("not True equals?", ["False", "True", "0", "None"], 0, "Boolean invert."),
        ("7 % 2 == 0?", ["False", "True", "1", "3.5"], 0, "7 odd."),
        ("First list index?", ["0", "1", "-0", "None"], 0, "Zero-based."),
        ("len([1,2,3])?", ["3", "2", "4", "6"], 0, "Three elements."),
        ("random.choice needs?", ["sequence", "integer only", "dict only", "two args"], 0, "Pick from sequence."),
        ("range(5) stops at?", ["4", "5", "6", "0"], 0, "0-4 inclusive."),
        ("def keyword?", ["defines function", "deletes var", "loops", "imports"], 0, "Function definition."),
        ("while loop stops when?", ["condition False", "10 iterations always", "break only", "never"], 0, "Condition driven."),
        ("Function without return returns?", ["None", "0", "False", "Error"], 0, "Implicit None."),
        ("'a' in 'cat'?", ["True", "False", "Error", "1"], 0, "Membership."),
        ("Keyword arg syntax?", ["name=value", "value:name", "name->value", "arg name"], 0, "Named argument."),
        ("ord('a') approx?", ["97", "65", "0", "1"], 0, "ASCII 97."),
        ("Dict literal?", ["{}", "[]", "()", "<>"], 0, "Curly braces."),
        (".get() advantage?", ["default if missing", "faster sort", "deletes key", "adds key"], 0, "Safe access."),
        ("global keyword?", ["modify module var", "create local", "import", "delete"], 0, "Global declaration."),
        ("Which is mutable?", ["list", "str", "int", "tuple"], 0, "Lists mutable."),
        ("IndexError cause?", ["invalid index", "syntax error", "wrong type", "missing import"], 0, "Out of range."),
        ("TypeError often from?", ["wrong type operation", "bad indent", "missing :", "index"], 0, "Type mismatch."),
        ("NameError means?", ["undefined name", "bad index", "syntax", "keyboard"], 0, "Variable not found."),
        ("Best for unknown repeat count?", ["while", "for range only", "if", "def"], 0, "While for unknown."),
        ("Slice [1:3] on [0,1,2,3]?", ["[1,2]", "[1,2,3]", "[0,1]", "[2,3]"], 0, "Stop exclusive."),
        ("append adds to?", ["list end", "dict key", "set start", "tuple"], 0, "List method."),
        ("Caesar uses mod?", ["26", "10", "2", "100"], 0, "Alphabet wrap."),
        ("Blackjack bust?", ["over 21", "exactly 21", "under 10", "dealer wins always"], 0, "Over 21."),
        ("EASY constant convention?", ["ALL_CAPS", "camelCase", "lowercase", "dots"], 0, "Constants uppercase."),
        ("Multiple return gives?", ["tuple", "list auto", "dict", "None"], 0, "Tuple packing."),
        ("Docstring uses?", ["triple quotes", "single #", "//", "--"], 0, "Triple-quoted string."),
        ("elif means?", ["else if", "loop", "error", "delete if"], 0, "Alternative branch."),
        ("and needs?", ["both True", "one True", "neither", "always False"], 0, "Both conditions."),
        ("or needs?", ["at least one True", "both True", "both False only", "never True"], 0, "Either true."),
    ]
    for i, (q, opts, ans, exp) in enumerate(mcq_data):
        qs.append({"id": f"mcq{i+1}", "type": "mcq", "q": q, "options": opts, "answer": ans, "explain": exp})

    # Predict output
    predict_data = [
        ('print("A"+"B")', "AB", "Concatenation."),
        ("print(3+5)", "8", "Integer add."),
        ("print(type(5/1))", "<class 'float'>", "Division float."),
        ('print(int("7")+1)', "8", "Convert then add."),
        ("print(2**3)", "8", "Power."),
        ("print(not False)", "True", "not operator."),
        ("print(15%4)", "3", "Modulo."),
        ('print("hi"[1])', "i", "String index."),
        ("print([1,2][-1])", "2", "Last element."),
        ("print(len('abc'))", "3", "String length."),
        ("x=1\nx=2\nprint(x)", "2", "Reassign."),
        ("print(list(range(3)))", "[0, 1, 2]", "range default."),
        ("print(10//3)", "3", "Floor div."),
        ('print("x" in "xyz")', "True", "Membership."),
        ("def f(): return 1\nprint(f())", "1", "Return value."),
        ("print(bool(0))", "False", "Zero falsy."),
        ('print({"a":1}["a"])', "1", "Dict access."),
        ("print(3>5)", "False", "Comparison."),
        ("print(3==3)", "True", "Equality."),
        ("print(0 or 5)", "5", "or short-circuit."),
        ("print(1 and 0)", "0", "and short-circuit."),
    ]
    for i, (code, ans, exp) in enumerate(predict_data):
        qs.append({"id": f"pred{i+1}", "type": "predict", "q": f"Output?\n{code}", "answer": ans, "explain": exp})

    # True/False
    tf_data = [
        ("Python uses braces for blocks.", False, "Indentation defines blocks."),
        ("Lists are ordered.", True, "Order preserved."),
        ("You can use int() on '3.14'.", False, "ValueError — use float first."),
        ("return exits the function.", True, "Immediate exit."),
        ("Keys in dict can be lists.", False, "Lists unhashable."),
        ("random.randint(1,3) can return 3.", True, "Inclusive both ends."),
        ("while True: always infinite without break.", True, "Condition never false."),
        ("Functions must have parameters.", False, "Optional parameters."),
        ("str(100) returns '100'.", True, "String conversion."),
        ("Modifying global requires global keyword.", True, "Inside functions."),
        ("Slicing includes stop index.", False, "Stop exclusive."),
        ("for loops can iterate strings.", True, "Strings iterable."),
        ("elif runs if if was True.", False, "Skipped when if matches."),
        ("print returns a value to assign.", False, "print returns None."),
        ("A tuple can be a dict key.", True, "If hashable."),
    ]
    for i, (q, ans, exp) in enumerate(tf_data):
        qs.append({"id": f"tf{i+1}", "type": "tf", "q": q, "answer": ans, "explain": exp})

    # Fill blank
    fill_data = [
        ("Use _____ to display output.", "print", "print() function."),
        ("Convert str to int: _____.", "int", "int() constructor."),
        ("Loop keyword for sequences: _____.", "for", "for loop."),
        ("Define function keyword: _____.", "def", "def keyword."),
        ("Safe dict access method: _____.", "get", ".get() method."),
        ("Remainder operator: _____.", "%", "Modulo operator."),
        ("Join strings with _____ operator.", "+", "Concatenation."),
        ("Comment starts with _____.", "#", "Hash comment."),
        ("Keyword to modify global: _____.", "global", "global declaration."),
        ("Pick random list item: random._____.", "choice", "choice function."),
    ]
    for i, (q, ans, exp) in enumerate(fill_data):
        qs.append({"id": f"fill{i+1}", "type": "fill", "q": q, "answer": ans, "explain": exp})

    # Debugging
    debug_data = [
        ("print(Hello) — NameError. Fix?", "Add quotes: print('Hello')", "Strings need quotes."),
        ("if age > 18 — SyntaxError. Fix?", "Add colon: if age > 18:", "Missing colon."),
        ("print(list[0]) — NameError. Fix?", "Use variable name: print(my_list[0])", "list is type not variable."),
        ("'5'+'3' gives '53' not 8. Fix?", "int('5')+int('3')", "Convert before add."),
        ("items[3] IndexError on len 3. Fix?", "Use valid index 0-2", "Off by one."),
        ("x = x+1 in function UnboundLocalError. Fix?", "global x or pass x as param", "Scope issue."),
        ("if choice = 'y' SyntaxError. Fix?", "Use == for comparison", "= assigns."),
        ("for i in range(5) missing body IndentationError. Fix?", "Indent print under for", "Body must indent."),
        ("import random; random.randint(1) TypeError. Fix?", "randint needs 2 args: randint(1,6)", "Two arguments required."),
        ("d['missing'] KeyError. Fix?", "Use d.get('missing') or check 'in'", "Safe access."),
    ]
    for i, (q, ans, exp) in enumerate(debug_data):
        qs.append({"id": f"dbg{i+1}", "type": "debug", "q": q, "answer": ans, "explain": exp})

    # Coding concept MCQ continued to reach 100
    extra_mcq = [
        ("Which opens a code block?", ["indentation", "{}", "begin/end", "tab only"], 0, "Indentation."),
        ("Best split bill formatting?", ["f-string", "hex", "bytes", "eval"], 0, "f-strings readable."),
        ("Track highest bid?", ["loop compare", "min()", "sorted reverse only", "pop"], 0, "Compare in loop."),
        ("Password gen uses?", ["loop + random", "only if", "only dict", "import os only"], 0, "Loop random picks."),
        ("Hangman wrong guess?", ["lose life", "win instantly", "shuffle word", "exit Python"], 0, "Deduct life."),
        ("Decode cipher?", ["negative shift", "delete text", "print only", "double encode"], 0, "Reverse shift."),
        ("Calculator ops stored in?", ["dict", "tuple only", "set of ints", "comments"], 0, "Symbol to function."),
        ("Dealer hits until?", ["score>=17 typical", "score==21", "never", "player bust"], 0, "Standard rule."),
        ("Guess game hint too low?", ["guess higher", "guess lower", "quit", "random"], 0, "Adjust up."),
        ("LEGB 'L' stands for?", ["Local", "List", "Loop", "Library"], 0, "Local scope first."),
        ("Negative index -1 is?", ["last item", "first item", "error always", "empty"], 0, "Last element."),
        ("shuffle modifies?", ["list in place", "tuple", "int", "str immutable"], 0, "In-place shuffle."),
        ("Nested dict access?", ["chain brackets", "only .get", "cannot nest", "use eval"], 0, "d['a']['b']."),
        ("Pass statement?", ["no-op placeholder", "exit loop", "return None", "import"], 0, "Does nothing."),
        ("isalpha() on 'A'?", ["True", "False", "Error", "None"], 0, "Letter check."),
    ]
    base = len(qs)
    for i, (q, opts, ans, exp) in enumerate(extra_mcq):
        qs.append({"id": f"mcq2_{i+1}", "type": "mcq", "q": q, "options": opts, "answer": ans, "explain": exp})

    # More predict to hit 100
    extra_pred = [
        ("print(round(3.14159,2))", "3.14", "Round 2 decimals."),
        ("print(max([1,5,3]))", "5", "Built-in max."),
        ("print(''.join(['a','b']))", "ab", "Join strings."),
        ("print(3!=3)", "False", "Not equal."),
        ("a=[1,2]; a.append(3); print(a[-1])", "3", "Append and index."),
        ("print(bool(None))", "False", "None falsy."),
        ("print(2 and 3)", "3", "and returns last truthy."),
        ("print(0 or '')", "", "Both falsy — last."),
        ("print(list(range(2,5)))", "[2, 3, 4]", "range start stop."),
        ("print('Python'[0:2])", "Py", "String slice."),
    ]
    for i, (code, ans, exp) in enumerate(extra_pred):
        qs.append({"id": f"pred2_{i+1}", "type": "predict", "q": f"Output?\n{code}", "answer": ans, "explain": exp})

    # Trim or pad to exactly 100
    while len(qs) < 100:
        n = len(qs) + 1
        qs.append({"id": f"bonus{n}", "type": "mcq", "q": f"Python beginner concept #{n}: Which helps readability?",
                     "options": ["Clear variable names", "Single letter only", "No spaces ever", "Random names"], "answer": 0, "explain": "Descriptive names aid readability."})
    return qs[:100]
