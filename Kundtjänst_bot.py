
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

    # --- Problem ---
     (["problem",  "issue", "error", "bug", "not working", "broken", "doesn't work", "fail"], [
    "I'm sorry you're having a problem. Can you describe it?",
    "Let me help you fix that. What seems to be wrong?"
        ]),

    # --- Return ---
     (["return", "refund", "send back", "give back", "exchange", "wrong item", "cancel order"], [
    "I can help with returns. Do you want a refund or exchange?",
    "Sure, let's start your return process."
           ]),

    # --- Delivery ---
     ([ "delivery", "shipping", "where is my order", "track", "tracking", "when will it arrive", "late", "delay"], [
    "You can track your order using your tracking number.",
    "Let me help you check your delivery status."
           ]),

    # --- Ending ---
     (["bye", "goodbye", "see you", "thanks", "thank you", "thx", "ok bye"], [
    "Goodbye! Have a great day!",
    "You're welcome! Let me know if you need anything else."
           ]),
    ]

fallback_responses = [
    
    ]