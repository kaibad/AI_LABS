def water_jug_problem():
    jug_a = 4  
    jug_b = 3 
    target = 2  
    current_a = 0
    current_b = 0
    actions = []
    def is_valid_state(a, b):
        return 0 <= a <= jug_a and 0 <= b <= jug_b
    def perform_action(action):
        nonlocal current_a, current_b
        actions.append(action)
        if action == "fill_a":
            current_a = jug_a
        elif action == "fill_b":
            current_b = jug_b
        elif action == "empty_a":
            current_a = 0
        elif action == "empty_b":
            current_b = 0
        elif action == "pour_a_to_b":
            to_pour = min(current_a, jug_b - current_b)
            current_a -= to_pour
            current_b += to_pour
        elif action == "pour_b_to_a":
            to_pour = min(current_b, jug_a - current_a)
            current_b -= to_pour
            current_a += to_pour
    while current_a != target and current_b != target:
        if current_a == 0:
            perform_action("fill_a")
        elif current_b == jug_b:
            perform_action("empty_b")
        elif current_a > 0 and current_b < jug_b:
            perform_action("pour_a_to_b")
        else:
            perform_action("pour_b_to_a")
    while current_a != target:
        if current_a == 0:
            perform_action("fill_a")
        else:
            perform_action("pour_a_to_b")

    while current_b != target:
        if current_b == jug_b:
            perform_action("empty_b")
        else:
            perform_action("pour_a_to_b")
    print("Sequence of actions:")
    for action in actions:
        print(action)
water_jug_problem()
print("Name:KailashBadu\nRollNo:-09")

