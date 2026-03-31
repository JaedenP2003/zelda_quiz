from django.shortcuts import redirect, render

CHARACTERS = {
    "link": {
        "name": "Link",
        "title": "The Courageous Hero",
        "description": "You act when others hesitate. You are brave, dependable, and willing to carry a heavy burden without needing attention.",
        "image": "https://zelda.nintendo.com/",
    },
    "zelda": {
        "name": "Princess Zelda",
        "title": "The Wise Strategist",
        "description": "You value wisdom, understanding, and careful planning. You think ahead and want your choices to actually matter.",
        "image": "https://zelda.nintendo.com/",
    },
    "midna": {
        "name": "Midna",
        "title": "The Clever Trickster",
        "description": "You are sharp, adaptable, and hard to read. You solve problems creatively and usually have a backup plan.",
        "image": "https://zelda.nintendo.com/",
    },
    "ganondorf": {
        "name": "Ganondorf",
        "title": "The Dominant Force",
        "description": "You are ambitious, intense, and not afraid to take control. You value strength and refuse to be ignored.",
        "image": "https://zelda.nintendo.com/",
    },
    "sheik": {
        "name": "Sheik",
        "title": "The Silent Tactician",
        "description": "You are disciplined, observant, and strategic. You prefer precision over noise and focus over chaos.",
        "image": "https://zelda.nintendo.com/",
    },
    "urbosa": {
        "name": "Urbosa",
        "title": "The Confident Leader",
        "description": "You are powerful, calm, and naturally respected. You lead with confidence and protect the people around you.",
        "image": "https://zelda.nintendo.com/",
    },
    "daruk": {
        "name": "Daruk",
        "title": "The Loyal Guardian",
        "description": "You are warm, fearless, and dependable. Others know they can count on you when things get rough.",
        "image": "https://zelda.nintendo.com/",
    },
    "revali": {
        "name": "Revali",
        "title": "The Proud Challenger",
        "description": "You are competitive, talented, and driven to stand out. You set high standards and expect excellence.",
        "image": "https://zelda.nintendo.com/",
    },
}

QUESTIONS = [
    {
        "id": "q1",
        "text": "You are put in charge of an important mission. What matters most to you?",
        "answers": [
            {"value": "a", "text": "Finishing it no matter what"},
            {"value": "b", "text": "Understanding the bigger picture"},
            {"value": "c", "text": "Finding the smartest angle"},
            {"value": "d", "text": "Making sure everyone follows your lead"},
        ],
    },
    {
        "id": "q2",
        "text": "A serious problem appears with no warning. What is your first move?",
        "answers": [
            {"value": "a", "text": "Step in immediately"},
            {"value": "b", "text": "Pause and study it"},
            {"value": "c", "text": "Look for a hidden option"},
            {"value": "d", "text": "Take command before things get worse"},
        ],
    },
    {
        "id": "q3",
        "text": "What kind of strength do you respect most?",
        "answers": [
            {"value": "a", "text": "Courage"},
            {"value": "b", "text": "Wisdom"},
            {"value": "c", "text": "Cleverness"},
            {"value": "d", "text": "Power"},
        ],
    },
    {
        "id": "q4",
        "text": "In a group, you usually become the one who...",
        "answers": [
            {"value": "a", "text": "Gets things moving"},
            {"value": "b", "text": "Keeps everyone focused"},
            {"value": "c", "text": "Finds creative solutions"},
            {"value": "d", "text": "Pushes the group to be stronger"},
        ],
    },
    {
        "id": "q5",
        "text": "Which setting feels most like home?",
        "answers": [
            {"value": "a", "text": "A wide open field with room to move"},
            {"value": "b", "text": "An ancient library or hidden ruins"},
            {"value": "c", "text": "A mysterious place full of secrets"},
            {"value": "d", "text": "A throne room or battlefield"},
        ],
    },
    {
        "id": "q6",
        "text": "What usually frustrates you the most?",
        "answers": [
            {"value": "a", "text": "Watching people freeze up"},
            {"value": "b", "text": "Careless decisions"},
            {"value": "c", "text": "Boring, obvious solutions"},
            {"value": "d", "text": "Being underestimated"},
        ],
    },
    {
        "id": "q7",
        "text": "How do you want others to see you?",
        "answers": [
            {"value": "a", "text": "Reliable"},
            {"value": "b", "text": "Intelligent"},
            {"value": "c", "text": "Interesting"},
            {"value": "d", "text": "Impressive"},
        ],
    },
    {
        "id": "q8",
        "text": "You find a powerful artifact. What do you do with it?",
        "answers": [
            {"value": "a", "text": "Use it only if it helps protect others"},
            {"value": "b", "text": "Study it before making any move"},
            {"value": "c", "text": "Test its limits carefully"},
            {"value": "d", "text": "Claim it before someone else does"},
        ],
    },
    {
        "id": "q9",
        "text": "What kind of role fits you best?",
        "answers": [
            {"value": "a", "text": "Hero on the front line"},
            {"value": "b", "text": "Planner behind the scenes"},
            {"value": "c", "text": "Wildcard with unexpected ideas"},
            {"value": "d", "text": "Leader at the center of it all"},
        ],
    },
    {
        "id": "q10",
        "text": "Pick the phrase that sounds most like you.",
        "answers": [
            {"value": "a", "text": "Do what needs to be done."},
            {"value": "b", "text": "Think first, then act."},
            {"value": "c", "text": "There is always another way."},
            {"value": "d", "text": "I was made for more than ordinary."},
        ],
    },
]

SCORING = {
    "q1": {
        "a": {"link": 2, "daruk": 1},
        "b": {"zelda": 2, "sheik": 1},
        "c": {"midna": 2, "revali": 1},
        "d": {"ganondorf": 1, "urbosa": 2},
    },
    "q2": {
        "a": {"link": 2, "daruk": 1},
        "b": {"zelda": 2, "sheik": 2},
        "c": {"midna": 2, "revali": 1},
        "d": {"urbosa": 2, "ganondorf": 1},
    },
    "q3": {
        "a": {"link": 2, "daruk": 2},
        "b": {"zelda": 2, "sheik": 1},
        "c": {"midna": 2, "revali": 1},
        "d": {"ganondorf": 2, "urbosa": 1},
    },
    "q4": {
        "a": {"link": 2, "daruk": 1},
        "b": {"zelda": 2, "sheik": 2},
        "c": {"midna": 2, "revali": 1},
        "d": {"urbosa": 2, "ganondorf": 2},
    },
    "q5": {
        "a": {"link": 2, "revali": 1},
        "b": {"zelda": 2, "sheik": 1},
        "c": {"midna": 2, "ganondorf": 1},
        "d": {"urbosa": 1, "daruk": 2},
    },
    "q6": {
        "a": {"link": 1, "daruk": 2},
        "b": {"zelda": 2, "sheik": 1},
        "c": {"midna": 2, "revali": 1},
        "d": {"ganondorf": 2, "urbosa": 2},
    },
    "q7": {
        "a": {"link": 2, "daruk": 2},
        "b": {"zelda": 2, "sheik": 1},
        "c": {"midna": 2, "revali": 1},
        "d": {"urbosa": 2, "ganondorf": 2},
    },
    "q8": {
        "a": {"link": 2, "daruk": 1},
        "b": {"zelda": 2, "sheik": 2},
        "c": {"midna": 2, "revali": 1},
        "d": {"ganondorf": 2, "urbosa": 1},
    },
    "q9": {
        "a": {"link": 2, "daruk": 1},
        "b": {"zelda": 2, "sheik": 2},
        "c": {"midna": 2, "revali": 2},
        "d": {"urbosa": 2, "ganondorf": 2},
    },
    "q10": {
        "a": {"link": 2, "daruk": 1},
        "b": {"zelda": 2, "sheik": 1},
        "c": {"midna": 2, "revali": 2},
        "d": {"ganondorf": 2, "urbosa": 2},
    },
}


def build_empty_scores():
    return {key: 0 for key in CHARACTERS.keys()}


def calculate_results(post_data):
    scores = build_empty_scores()

    for question in QUESTIONS:
        qid = question["id"]
        answer = post_data.get(qid)

        if not answer:
            continue

        if qid in SCORING and answer in SCORING[qid]:
            for character, points in SCORING[qid][answer].items():
                scores[character] += points

    winner_slug = max(scores, key=scores.get)
    total_points = sum(scores.values()) if sum(scores.values()) > 0 else 1

    percentages = []
    for slug, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        percent = round((score / total_points) * 100)
        percentages.append(
            {
                "slug": slug,
                "name": CHARACTERS[slug]["name"],
                "score": score,
                "percent": percent,
            }
        )

    return winner_slug, scores, percentages


def home(request):
    return render(request, "quiz/home.html")


def quiz_view(request):
    if request.method == "POST":
        cleaned_answers = {}

        for question in QUESTIONS:
            qid = question["id"]
            cleaned_answers[qid] = request.POST.get(qid)

        request.session["quiz_answers"] = cleaned_answers
        return redirect("result")

    return render(request, "quiz/quiz.html", {"questions": QUESTIONS})


def result_view(request):
    answers = request.session.get("quiz_answers")

    if not answers:
        return redirect("quiz")

    winner_slug, scores, percentages = calculate_results(answers)
    winner = CHARACTERS[winner_slug]

    context = {
        "winner_slug": winner_slug,
        "winner": winner,
        "percentages": percentages[:4],
    }
    return render(request, "quiz/result.html", context)


def character_detail(request, slug):
    character = CHARACTERS.get(slug)

    if not character:
        return redirect("home")

    related_traits = {
        "link": ["Bravery", "Loyalty", "Action"],
        "zelda": ["Wisdom", "Leadership", "Insight"],
        "midna": ["Cleverness", "Adaptability", "Mystery"],
        "ganondorf": ["Ambition", "Power", "Control"],
        "sheik": ["Discipline", "Stealth", "Strategy"],
        "urbosa": ["Confidence", "Leadership", "Protection"],
        "daruk": ["Loyalty", "Warmth", "Fearlessness"],
        "revali": ["Pride", "Skill", "Competition"],
    }

    return render(
        request,
        "quiz/character_detail.html",
        {
            "slug": slug,
            "character": character,
            "traits": related_traits.get(slug, []),
        },
    )