"""Simple command-line chatbot implemented in Python."""

from __future__ import annotations

import datetime as _dt
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class ReplyRule:
    """Represents a keyword rule and a set of possible responses."""

    keywords: tuple[str, ...]
    responses: tuple[str, ...]


RULES: tuple[ReplyRule, ...] = (
    ReplyRule(
        keywords=("hello", "hi", "hey"),
        responses=(
            "Hello! How can I help you today?",
            "Hi there 👋 Ask me anything.",
        ),
    ),
    ReplyRule(
        keywords=("name", "who are you"),
        responses=(
            "I'm PyBuddy, your simple Python chatbot.",
            "You can call me PyBuddy 🤖.",
        ),
    ),
    ReplyRule(
        keywords=("time", "clock"),
        responses=(
            "The current time is {time}.",
            "Right now it's {time}.",
        ),
    ),
    ReplyRule(
        keywords=("date", "day"),
        responses=(
            "Today's date is {date}.",
            "It's {date} today.",
        ),
    ),
    ReplyRule(
        keywords=("help", "what can you do"),
        responses=(
            "I can chat, tell you the time/date, and respond to simple keywords.",
            "Try saying hello, asking my name, or asking for the time/date.",
        ),
    ),
)

DEFAULT_RESPONSES: tuple[str, ...] = (
    "I'm not sure I understand yet, but I'm learning.",
    "Could you rephrase that?",
    "Interesting! Tell me more.",
)

EXIT_COMMANDS = {"exit", "quit", "bye"}


def _format_response(template: str) -> str:
    """Fill dynamic placeholders used in responses."""

    now = _dt.datetime.now()
    return template.format(time=now.strftime("%H:%M:%S"), date=now.strftime("%Y-%m-%d"))


def generate_reply(message: str) -> str:
    """Return a chatbot reply based on simple keyword matching."""

    normalized = message.strip().lower()
    if not normalized:
        return "Please type something so I can respond."

    for rule in RULES:
        if any(keyword in normalized for keyword in rule.keywords):
            return _format_response(random.choice(rule.responses))

    return random.choice(DEFAULT_RESPONSES)


def chat_loop() -> None:
    """Run the interactive chatbot loop."""

    print("PyBuddy: Hi! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in EXIT_COMMANDS:
            print("PyBuddy: Goodbye! 👋")
            break

        print(f"PyBuddy: {generate_reply(user_input)}")


if __name__ == "__main__":
    chat_loop()
