"""A beginner-friendly interactive phishing risk analyzer."""


QUESTIONS = (
    ("Did the email create a sense of urgency or threaten consequences?", 2),
    ("Did the email ask for passwords, payment information, or other personal data?", 3),
    ("Does the email contain suspicious links or attachments?", 3),
    ("Is the sender's address or name different from the organization it claims to be?", 2),
    ("Was the email from an unexpected or unknown sender?", 1),
    ("Does the email contain unusual spelling, grammar, or formatting?", 1),
)


def get_risk_rating(score):
    """Convert a numeric score to a low, medium, or high rating."""
    if score >= 6:
        return "high"
    if score >= 3:
        return "medium"
    return "low"


def calculate_risk_score(answers):
    """Calculate a score from answers that are True/False or yes/no strings."""
    score = 0
    for answer, (_, points) in zip(answers, QUESTIONS):
        if isinstance(answer, str):
            answer = answer.strip().lower() in ("y", "yes", "true")
        if answer:
            score += points
    return score


def ask_questions():
    """Ask the user each question and return a risk score."""
    answers = []
    print("Phishing Risk Analyzer")
    print("Answer each question with yes or no.\n")

    for question, _ in QUESTIONS:
        while True:
            answer = input(question + " ").strip().lower()
            if answer in ("y", "yes"):
                answers.append(True)
                break
            if answer in ("n", "no"):
                answers.append(False)
                break
            print("Please answer yes or no.")

    return calculate_risk_score(answers)


def main():
    score = ask_questions()
    rating = get_risk_rating(score)
    print(f"\nYour phishing risk rating is: {rating.upper()} (score: {score})")


if __name__ == "__main__":
    main()
