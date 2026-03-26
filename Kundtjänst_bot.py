
import random

rules = [
    # --- Greetings ---
    (["hello", "hi", "hey", "howdy"], [
        "Hello! How can i help you today?", 
        "Hi there! Tell me, what can i help you with today?"
        ]),

    # --- Wants to order ---
    (["buy", "order", "purchase", "place order", "checkout", "get", "pay"], [
        "Do you want me to help you with the order",
        "Do you need any help with the ordering?",
        "Do you need help finding the product?"
        ]),

    # --- Has ordered ---
     (["bought", "ordered", "purchased", "placed order", "checked out", "got", "paid"], [
        "Nice! Do you want me to track your order?",
        "Great! I can check where your package is.",
        "Your order is confirmed! Need help with delivery updates?"
        ]),

    # --- Return ---
     (["return", "refund", "send back", "give back", "exchange", "wrong item", "cancel order"], [
        "I can help with returns. Do you want a refund or exchange?",
        "Sure, let's start your return process."
        ]),

    # --- Delivery ---
     (["delivery", "shipping", "where is my order", "track", "tracking", "when will it arrive", "late", "delay"], [
        "You can track your order using your tracking number.",
        "Let me help you check your delivery status."
        ]),

  # --- Problem ---
     (["problem", "issue", "error", "bug", "not working", "broken", "doesn't work", "fail"], [
       "I'm sorry you're having a problem. Can you describe it?",
       "Let me help you fix that. What seems to be wrong?"
        ])

    # --- Ending ---
     (["bye", "goodbye", "see you", "thanks", "thank you", "thx", "ok bye", "untill next time"], [
       "Goodbye! Have a great day!",
       "You're welcome! Let me know if you need anything else."
        ]),
    ]


fallback_responses = [
    "I´m not sure I understand. Could you rephrase your question?",
    "Sorry, I couldnt find an answer to that. Can you try asking in a different way?",
    "I didn´t quite understand that. Could you provide more details?",
    "Could you clarify what you need help with? For example: shipping, tracking or returns?",
    "Go on, I am listening."
    ]

def find_response(message):
    """
    Searches through the rules and returns a matching response.
    Converts the message to lowercase for easier matching.
    """
    message = message.lower()

    for keyword_list, response_list in rules:
        for keyword in keyword_list:
            if keyword in message:
                return random.choice(response_list)

    
    return random.choice(fallback_responses)


def run_bot():
    """
    Starts the chatbot and keeps the conversation going
    until the user types a farewell word.
    """
    print("=" * 50)
    print("   Hello! How can I help you?")
    print("   (Type 'bye' to exit)")
    print("=" * 50)

    farewell_words = ["bye", "goodbye"]

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        response = find_response(user_input)
        print(f"Anna: {response}")

        if any(word in user_input.lower() for word in farewell_words):
            break

if __name__ == "__main__":
    run_bot()