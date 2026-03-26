TASKS = [

    # EASY
    {
        "id": 1,
        "difficulty": "easy",
        "email": "My payment failed and money was deducted. Please help immediately.",
        "urgency": 9,
        "customer_type": "premium",
        "sentiment": "angry",
        "correct_action": "escalate",
        "acceptable_actions": ["reply"]
    },

    # EASY
    {
        "id": 2,
        "difficulty": "easy",
        "email": "Thank you for your great service!",
        "urgency": 2,
        "customer_type": "normal",
        "sentiment": "happy",
        "correct_action": "ignore",
        "acceptable_actions": ["reply"]
    },

    # MEDIUM
    {
        "id": 3,
        "difficulty": "medium",
        "email": "I have an issue with my order but it's not urgent.",
        "urgency": 5,
        "customer_type": "normal",
        "sentiment": "neutral",
        "correct_action": "reply",
        "acceptable_actions": ["ignore"]
    },

    # MEDIUM
    {
        "id": 4,
        "difficulty": "medium",
        "email": "I am a premium user and I need help with billing.",
        "urgency": 6,
        "customer_type": "premium",
        "sentiment": "neutral",
        "correct_action": "escalate",
        "acceptable_actions": ["reply"]
    },

    # HARD
    {
        "id": 5,
        "difficulty": "hard",
        "email": "This is unacceptable service. I want this fixed now.",
        "urgency": 7,
        "customer_type": "normal",
        "sentiment": "angry",
        "correct_action": "escalate",
        "acceptable_actions": ["reply"]
    },

    # HARD 
    {
        "id": 6,
        "difficulty": "hard",
        "email": "Just checking on my issue, no rush though.",
        "urgency": 4,
        "customer_type": "premium",
        "sentiment": "neutral",
        "correct_action": "reply",
        "acceptable_actions": ["ignore"]
    }
]