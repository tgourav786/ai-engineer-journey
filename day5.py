import sqlite3
import pandas as pd

# 1. Create a database in memory
conn = sqlite3.connect("ai_engineer.db")

# 2. Load real data
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
df.to_sql("iris", conn, index=False, if_exists="replace")

print("Database created with 150 flowers!\n")

# 3. Your first 4 SQL queries
queries = {
    "Count by species": "SELECT species, COUNT(*) as total FROM iris GROUP BY species",
    "Average sepal length": "SELECT species, ROUND(AVG(sepal_length),2) as avg_length FROM iris GROUP BY species",
    "Big flowers": "SELECT * FROM iris WHERE sepal_length > 6.5 LIMIT 5",
    "AI Engineer style filter": "SELECT species, sepal_length, petal_length FROM iris WHERE petal_length < 1.5 ORDER BY sepal_length DESC LIMIT 5"
}

for title, q in queries.items():
    print(f"--- {title} ---")
    print(f"SQL: {q}")
    result = pd.read_sql(q, conn)
    print(result.to_string(index=False))
    print()

conn.close()
print("✅ Day 5 done - You know SQL now!")