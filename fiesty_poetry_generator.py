import random

# Define a list of feisty words and phrases
feisty_words = [
    "sassy", "bold", "fearless", "fierce", "fiery",
    "rebellious", "defiant", "spunky", "audacious", "daring"
]

# Define a list of poem templates
poem_templates = [
    "With a {word1} heart and a {word2} mind,\nI conquer the world, one battle at a time.",
    "In the face of adversity, I stand {word1},\nNo challenge too great, my spirit {word2}.",
    "A {word1} soul, unyielding and true,\nI blaze my path, in all that I do.",
    "With {word1} eyes and a {word2} grin,\nI face the world, determined to win.",
    "In a {word1} dance, I take my stand,\nUnstoppable force, with a {word2} hand."
]

def generate_feisty_poem():
    # Select a random template
    template = random.choice(poem_templates)
    # Select random feisty words
    word1 = random.choice(feisty_words)
    word2 = random.choice(feisty_words)
    # Generate the poem
    poem = template.format(word1=word1, word2=word2)
    return poem

if __name__ == "__main__":
    poem = generate_feisty_poem()
    print(poem)
