import pandas as pd

# Day 2 - My AI Learning Tracker
data = {
    "skill": ["Python", "SQL", "Git", "RAG", "FastAPI", "Docker"],
    "hours_spent": [1.5, 0, 0.5, 0, 0, 0],
    "status": ["Done", "Pending", "Done", "Pending", "Pending", "Pending"],
    "importance": [10, 8, 9, 10, 9, 7]
}

df = pd.DataFrame(data)

print("=== MY AI JOURNEY DATA ===")
print(df)

print("\n=== QUICK STATS ===")
print(f"Total skills tracked: {len(df)}")
print(f"Completed: {len(df[df['status']=='Done'])}")
print(f"Total hours so far: {df['hours_spent'].sum()}")

print("\n=== MOST IMPORTANT SKILL TO LEARN NEXT ===")
pending = df[df['status'] == 'Pending'].sort_values(by='importance', ascending=False)
print(pending.head(1))

# This is what you will do in real AI jobs - save data
df.to_csv("my_progress.csv", index=False)
print("\n✅ Saved progress to my_progress.csv - Open it!")

# Load a real CSV from internet (no download needed)
print("\n=== REAL WORLD DATA ===")
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
real_df = pd.read_csv(url)
print(real_df.head())
print(f"Shape: {real_df.shape} - {real_df.shape[0]} rows, {real_df.shape[1]} columns")