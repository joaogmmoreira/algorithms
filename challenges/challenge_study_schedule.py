def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    count = 0

    for student_schedule in permanence_period:
        if not isinstance(
            student_schedule[0], int
        ) or not isinstance(student_schedule[1], int):
            return None

        if student_schedule[0] <= target_time <= student_schedule[1]:
            count += 1

    return count
