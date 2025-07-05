import os
import random
import datetime
from subprocess import run
import shutil
import time

# Path to your local Git repository
repo_path = "C:/Users/Om Awchar/Documents/Leetcode C++"
os.chdir(repo_path)

# List of meaningful topics or filenames
file_topics = [
    "arrays_and_strings", "dynamic_programming", "binary_search",
    "sorting_algorithms", "graphs_and_trees", "backtracking",
    "bit_manipulation", "greedy_algorithms"
]

# Loop to generate 50 commits
for commit_num in range(1, 3):
    folder_name = f"Daily_Updates_{commit_num}"
    os.makedirs(folder_name, exist_ok=True)

    # Random number of files per commit
    num_files = random.randint(1, 5)

    # Create files with random topics
    for i in range(num_files):
        topic = random.choice(file_topics)
        file_path = f"{folder_name}/{topic}_{random.randint(1,1000)}.txt"
        with open(file_path, "w") as file:
            file.write(f"Commit #{commit_num}\n")
            file.write(f"Notes on {topic}\n")
            file.write(f"Generated at {datetime.datetime.now()}\n")

    # Git add and commit
    run(f"git add {folder_name}", shell=True)
    run(f'git commit -m "Commit #{commit_num}: Added {num_files} {folder_name} files."', shell=True)

    # Delete the folder
    shutil.rmtree(folder_name)

    # Commit the deletion
    run(f"git add -u", shell=True)
    run(f'git commit -m "Commit #{commit_num}: Deleted {folder_name} after updates."', shell=True)

    # Optional: Delay to avoid Git timestamp collisions
    time.sleep(1)

# Push to GitHub after all commits
run("git push origin main", shell=True)
