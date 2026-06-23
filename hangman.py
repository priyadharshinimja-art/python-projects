"""
╔══════════════════════════════════════════════════════════╗
║           HANGMAN GAME — CodeAlpha Internship            ║
║                      Task 1                              ║
╚══════════════════════════════════════════════════════════╝

Author  : CodeAlpha Intern
Domain  : Python Programming
Concepts: random, while loop, if-else, strings, lists
"""

import random


# ── Constants ──────────────────────────────────────────────────────────────────

WORD_LIST = ["python", "hangman", "laptop", "keyboard", "science"]
MAX_WRONG = 6

HANGMAN_STAGES = [
    # 0 wrong guesses
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    # 1 wrong guess
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # 2 wrong guesses
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # 3 wrong guesses
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # 4 wrong guesses
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # 5 wrong guesses
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    # 6 wrong guesses — DEAD
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]


# ── Display Helpers ─────────────────────────────────────────────────────────────

def display_board(wrong_guesses: int, guessed_letters: set, secret_word: str) -> None:
    """Render the current game state to the console."""
    print(HANGMAN_STAGES[wrong_guesses])

    # Show revealed letters and blanks
    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print(f"  Word: {display_word}\n")
    print(f"  Wrong guesses left : {MAX_WRONG - wrong_guesses}")
    print(f"  Letters guessed    : {', '.join(sorted(guessed_letters)) or 'None'}\n")


def get_player_guess(guessed_letters: set) -> str:
    """Prompt the player for a single, new alphabetic letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("  ⚠  Please enter exactly one letter.")
        elif not guess.isalpha():
            print("  ⚠  Letters only, please.")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess


# ── Core Game Loop ──────────────────────────────────────────────────────────────

def play_hangman() -> None:
    """Run one full round of Hangman."""
    secret_word     = random.choice(WORD_LIST)
    guessed_letters: set = set()
    wrong_guesses   = 0

    print("\n" + "=" * 56)
    print("        Welcome to HANGMAN!  (CodeAlpha — Task 1)")
    print("=" * 56)
    print(f"\n  A secret word with {len(secret_word)} letters has been chosen.")
    print(f"  You have {MAX_WRONG} incorrect guesses before it's game over.\n")

    while wrong_guesses < MAX_WRONG:
        display_board(wrong_guesses, guessed_letters, secret_word)

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"  🎉  Congratulations! You guessed the word: '{secret_word.upper()}'")
            print(f"  You finished with {wrong_guesses} wrong guess(es).\n")
            return

        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"\n  ✅  Nice! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            remaining = MAX_WRONG - wrong_guesses
            if remaining > 0:
                print(f"\n  ❌  '{guess}' is NOT in the word.  ({remaining} guess(es) left)\n")

    # Game over — show final state
    display_board(wrong_guesses, guessed_letters, secret_word)
    print(f"  💀  Game Over! The word was: '{secret_word.upper()}'\n")


def main() -> None:
    """Entry point — supports replaying."""
    while True:
        play_hangman()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing Hangman! — CodeAlpha\n")
            break


if __name__ == "__main__":
    main()
