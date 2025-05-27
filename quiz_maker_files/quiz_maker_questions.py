def load_questions():
    try:
        with open("quiz_creator_questions.txt", "r", encoding="utf-8") as file:
            content = file.read().strip().split("-" * 40)

        questions = []
        for block in content:
            lines = [line.strip() for line in block.strip().split("\n") if line.strip()]
            if len(lines) < 6:
                continue

            question_text = lines[0][len("Question: "):]
            options = [
                lines[1][len("a) "):],
                lines[2][len("b) "):],
                lines[3][len("c) "):],
                lines[4][len("d) "):]
            ]
            correct = lines[5][len("Correct Answer: "):].upper()

            questions.append({
                "question": question_text,
                "options": options,
                "correct": correct
            })
        return questions
    except FileNotFoundError:
        return []
