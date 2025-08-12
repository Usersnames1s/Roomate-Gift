import tkinter as tk
import random

# --- Global click counters ---
wait_count = 0
decorate_count = 0

# --- Function to check total clicks and trigger tunnel ---
def update_story():
    total = wait_count + decorate_count
    if total >= 3:
        story.set(
            "...\n...\n...hmm. It's sure been a while.\n"
            "When is my roommate getting here... when is anybody getting here?\n\n"
            "You stare into the black microwave—your face blurry in the reflection.\n"
            "It hums softly.\nThen... a glow appears behind the bed."
        )
        left_button.config(text="Go check behind the bed ☁", command=enter_tunnel)
        right_button.pack_forget()

# --- Button actions ---
def wait_for_roommate():
    global wait_count
    wait_count += 1
    dots = "." * (wait_count + 2)
    story.set(f"{dots}\nYou check your phone. Still no messages. Still no roommate.")
    update_story()

def decorate_room():
    global decorate_count
    decorate_count += 1
    decorations = [
        "★ You lay down your hot pink fur rug.",
        "★ You hang up your rhinestone mirror and polaroid string.",
        "★ You fluff your glitter pillow throne."
    ]
    if decorate_count <= len(decorations):
        line = decorations[decorate_count - 1]
        story.set(f"{line}\n♡ You step back...\nYou're kinda thriving.")
    update_story()

# --- Tunnel transition ---
def enter_tunnel():
    story.set(
        "☁ You duck behind the bed.\n"
        "The glow isn't from a charger or a plug.\n"
        "It's coming from... the wall?\n\n"
        "You reach forward. The wall opens.\nWarm mist curls around your fingers."
    )
    left_button.pack_forget()
    right_button.pack_forget()
    root.after(3000, hallway_scene)

# --- Hallway scene ---
def hallway_scene():
    story.set(
        "✿ You step into a narrow, velvet-lined hallway lit by chandeliers.\n\n"
        "From the door on the **left**, you catch the scent of frosting… and was that a cupcake meowing?\n"
        "From the door on the **right**, you hear cards shuffle and a stethoscope-like click.\n"
        "In the **center**, a misty wet door pulses gently... but stays closed.\n\n"
        "'We've missed you, Tahlia,' a voice whispers from the walls."
    )
    left_button.config(text="Listen at the left door ♡", command=hello_kitty_scene)
    right_button.config(text="Lean into the sounds on the right ♧", command=doc_mcstuffins_scene)
    middle_button.config(text="Touch the misty door ☂", command=locked_door_scene)
    left_button.pack(pady=10)
    right_button.pack(pady=10)
    middle_button.pack(pady=5)

# --- Room scenes ---
def hello_kitty_scene():
    story.set("❀ A sparkle-pink kitchen glows with sugar-dusted sunlight. Piping bags swirl themselves mid-air.\n\nHello Kitty turns, eyes twinkling: 'Tahlia! Can you still remember how to bake?'")

    left_button.config(text="Take the quiz 🍓", command=start_baking_quiz)
    right_button.pack_forget()
    middle_button.pack_forget()
    left_button.pack(pady=10)

quiz_question = 0

def start_baking_quiz():
    global quiz_question
    quiz_question = 0
    show_baking_question()

def show_baking_question():
    questions = [
        ("🧁 What comes first when baking a cake?", ["🌟 Crack the eggs", "🍚 Add sugar", "🔥 Bake it"]),
        ("🍥 When do you frost a cake?", ["🧁 After it cools", "🔥 In the oven", "🌈 Before you bake"]),
        ("🍓 What makes it rise?", ["🥚 Baking powder", "🧂 Salt", "❄ Glitter"])
    ]

    if quiz_question < len(questions):
        q_text, options = questions[quiz_question]
        story.set(q_text)
        left_button.config(text=options[0], command=lambda: answer_baking(True))
        right_button.config(text=options[1], command=lambda: answer_baking(False))
        middle_button.config(text=options[2], command=lambda: answer_baking(False))
        left_button.pack(pady=5)
        right_button.pack(pady=5)
        middle_button.pack(pady=5)
    else:
        story.set("Hello Kitty giggles: 'See? You’ve still got your sparkle.'\nShe hands you a cupcake with your name swirled in icing.\n\n'Every moment matters, Tahlia. That’s the real recipe.'")
        hide_buttons()

def answer_baking(correct):
    global quiz_question
    if correct:
        story.set("✅ Sweet! That’s right.")
    else:
        story.set("🍰 Oops! That might taste funny...")

    quiz_question += 1
    root.after(1500, show_baking_question)

tahlia_hand = []
doc_hand = []

def doc_mcstuffins_scene():
    story.set(
        "♧ You step into a velvet-draped den glowing with candlelight.\n"
        "Nameplates shimmer on the marble poker table:\n"
        "• Mr. Fordge Worthington III 🐒 lounges with velvet shades\n"
        "• Ms. Dorphie 'The Flop' Delmare 🐬 sharpens a plastic blade below the table\n\n"
        "At the head? Doc McStuffins in a velvet blazer and glossy scrubs, stethoscope aglow, puffing a candy-pink cigar.\n\n"
        "Without looking up, she grins:\n'Tahlia, honey… I’m off the clock. But I’m always in the game.'"
    )
    left_button.config(text="😳 Ask what she’s doing here", command=start_blackjack)
    left_button.pack(pady=10)
    right_button.pack_forget()
    middle_button.pack_forget()

def start_blackjack():
    global tahlia_hand, doc_hand
    tahlia_hand = [random.randint(2, 11), random.randint(2, 11)]
    doc_hand = [random.randint(7, 11), random.randint(7, 11)]
    story.set(
        "🚬 Doc leans forward, tapping ash into a gold tray.\n"
        "'I’ll tell you why I’m here... if you beat me in blackjack.'\n\n"
        "She deals. Two cards slide across the table.\n"
    )
    root.after(2000, update_blackjack_story)

def update_blackjack_story():
    total = sum(tahlia_hand)
    story.set(f"Your hand: {tahlia_hand} (Total: {total})\n\nWhat’s the move?")
    left_button.config(text="♦ Hit", command=blackjack_hit)
    right_button.config(text="♠ Stay", command=blackjack_stay)
    left_button.pack(pady=5)
    right_button.pack(pady=5)
    middle_button.pack_forget()

def blackjack_hit():
    tahlia_hand.append(random.randint(2, 11))
    if sum(tahlia_hand) > 21:
        story.set(f"💥 You draw again... and bust!\nYour hand: {tahlia_hand} (Total: {sum(tahlia_hand)})")
        root.after(2000, doc_blackjack_lose)
    else:
        update_blackjack_story()

def blackjack_stay():
    t_total = sum(tahlia_hand)
    d_total = sum(doc_hand)

    # Show both hands with totals
    story.set(
        f"🃏 Your hand: {tahlia_hand} (Total: {t_total})\n"
        f"🩺 Doc's hand: {doc_hand} (Total: {d_total})\n"
    )

    if t_total > 21:
        root.after(1500, doc_blackjack_lose)
    elif d_total > 21 or t_total > d_total:
        point_diff = t_total - d_total
        story.set(
            f"🃏 Your hand: {tahlia_hand} (Total: {t_total})\n"
            f"🩺 Doc's hand: {doc_hand} (Total: {d_total})\n\n"
            f"✨ You win by {point_diff} point{'s' if point_diff != 1 else ''}!"
        )
        root.after(2500, doc_blackjack_win)
    else:
        point_diff = d_total - t_total
        story.set(
            f"🃏 Your hand: {tahlia_hand} (Total: {t_total})\n"
            f"🩺 Doc's hand: {doc_hand} (Total: {d_total})\n\n"
            f"💥 Doc wins by {point_diff} point{'s' if point_diff != 1 else ''}!"
        )
        root.after(2500, doc_blackjack_lose)

def doc_blackjack_lose():
    story.set(
        "🚬 Doc chuckles, cigar between two fingers.\n\n"
        "'Oop—deal’s a deal, baby. But I was gonna tell you anyway.'\n\n"
        "'Life isn’t set in stone. Sometimes you bust, sometimes you draw a joker and rewrite the rules.'\n\n"
        "She pushes a joker card across the table with a smirk.\n'Keep this. Change the game when you're ready.'"
    )
    hide_buttons()

def doc_blackjack_win():
    story.set(
        "🃏 Doc laughs softly and taps her cigar on the tray.\n\n"
        "'Well I'll be... you came ready.'\n\n"
        "'But don’t get too comfy, champ. Life can flip the deck in a heartbeat.'\n\n"
        "She places her stethoscope in front of you gently.\n"
        "'Follow your rhythm. That’s how you find your way home.\nAnd if you ever need a crew... you’ve still got us.'"
    )
    hide_buttons()

def locked_door_scene():
    story.set("☂ You touch the cool surface. It hums beneath your fingers.\nLetters shimmer faintly above your hand:\n'Not Yet.'")
    left_button.config(text="← Step away quietly", command=hallway_scene)
    left_button.pack(pady=10)
    right_button.pack_forget()
    middle_button.pack_forget()

def hide_buttons():
    left_button.pack_forget()
    right_button.pack_forget()
    middle_button.pack_forget()

# --- GUI Setup ---
root = tk.Tk()
root.title("★ Tahlia’s Dorm Dream ★")
root.configure(bg="#FF69B4")  # Hot pink backdrop

story = tk.StringVar()
story.set(
    "✿ You enter your dorm.\nThe lights are soft. One bed is untouched.\n"
    "But your name sparkles above the other:\n♡ Tahlia ♡\n\n"
    "Time to settle in... or wait for whoever’s missing?"
)

label = tk.Label(
    root,
    textvariable=story,
    wraplength=550,
    justify="left",
    font=("Georgia", 14, "italic"),
    bg="#FF69B4",
    fg="#FFDDEE"
)
label.pack(padx=30, pady=30)

left_button = tk.Button(
    root,
    text="❧ Decorate your side",
    command=decorate_room,
    bg="#FFDDEE",
    fg="#C71585",
    font=("Georgia", 12)
)
left_button.pack(pady=10)

right_button = tk.Button(
    root,
    text="☁ Wait for your roommate",
    command=wait_for_roommate,
    bg="#FFDDEE",
    fg="#C71585",
    font=("Georgia", 12)
)
right_button.pack(pady=10)

middle_button = tk.Button(root, font=("Georgia", 12))

root.mainloop()