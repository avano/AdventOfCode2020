import os

with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/input/{os.path.basename(__file__).replace('.py', '.txt')}",
    "r",
) as f:
    input_list = f.read()


def part1():
    count = 0
    for user_group in input_list.split("\n\n"):
        count += len(set(user_group.replace("\n", "")))

    return count


def part2():
    count = 0
    for user_group in input_list.split("\n\n"):
        expected_question_answer_count = user_group.strip().count("\n") + 1
        questions_answers = {}
        for user_answers in user_group.split("\n"):
            for question_answer in user_answers:
                if question_answer not in questions_answers:
                    questions_answers[question_answer] = 0
                questions_answers[question_answer] += 1
        for value in questions_answers.values():
            if value == expected_question_answer_count:
                count += 1

    return count
