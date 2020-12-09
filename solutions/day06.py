import os


def solve(f):
    data = f.read()

    return part1(data), part2(data)


def part1(data):
    count = 0
    for user_group in data.split("\n\n"):
        count += len(set(user_group.replace("\n", "")))

    return count


def part2(data):
    count = 0
    for user_group in data.split("\n\n"):
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
