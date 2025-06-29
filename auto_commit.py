import os
import random
import datetime
from subprocess import run

# Path to your local repository
repo_path = "C:/Users/Om Awchar/Documents/Leetcode C++"

# Change directory to the repo
os.chdir(repo_path)

# List of C++ topics/problems to simulate updates
cpp_topics = [
    "Arrays and Strings", "Dynamic Programming", "Binary Search", "Sorting Algorithms",
    "Graphs and Trees", "Backtracking", "Bit Manipulation", "Greedy Algorithms"
]

# Number of contributions for the day
contributions = random.randint(15, 20)

for i in range(contributions):
    # Pick a random topic
    topic = random.choice(cpp_topics)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Generate file and commit message
    file_name = f"{topic.replace(' ', '_')}_notes.txt"
    commit_message = f"Added notes on {topic} at {timestamp}"

    # Append a note to the topic file
    with open(file_name, "a") as file:
        file.write(f"Update on {topic} - {timestamp}\n")
        file.write(f"Key points about {topic}...\n\n")  # Add more details here as needed

    # Git add, commit
    run(f"git add {file_name}", shell=True)
    run(f'git commit -m "{commit_message}"', shell=True)

# Push changes to GitHub
run("git push origin main", shell=True)
