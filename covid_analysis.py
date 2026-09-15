import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("dataset/day_wise.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values("Date")


# ==========================================
# 2. BASIC DATASET INFORMATION
# ==========================================

print("===================================")
print("       COVID-19 DATA ANALYSIS")
print("===================================")

print("\nDataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())


# ==========================================
# 3. COVID-19 STATISTICS
# ==========================================

print("\n===================================")
print("       COVID-19 STATISTICS")
print("===================================")

print("\nTotal Confirmed Cases:", df["Confirmed"].max())
print("Total Deaths:", df["Deaths"].max())
print("Total Recovered:", df["Recovered"].max())
print("Maximum Active Cases:", df["Active"].max())


# ==========================================
# 4. CONFIRMED CASES TREND
# ==========================================

plt.figure(figsize=(10, 5))

plt.plot(df["Date"], df["Confirmed"])

plt.title("COVID-19 Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/confirmed_cases.png")
plt.show()


# ==========================================
# 5. DEATHS TREND
# ==========================================

plt.figure(figsize=(10, 5))

plt.plot(df["Date"], df["Deaths"])

plt.title("COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Deaths")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/confirmed_cases.png")
plt.show()


# ==========================================
# 6. DAILY NEW CASES
# ==========================================

plt.figure(figsize=(10, 5))

plt.plot(df["Date"], df["New cases"])

plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/confirmed_cases.png")
plt.show()


# ==========================================
# 7. DAILY NEW DEATHS
# ==========================================

plt.figure(figsize=(10, 5))

plt.plot(df["Date"], df["New deaths"])

plt.title("Daily New COVID-19 Deaths")
plt.xlabel("Date")
plt.ylabel("New Deaths")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/confirmed_cases.png")
plt.show()


# ==========================================
# 8. IMPORTANT COVID-19 INSIGHTS
# ==========================================

max_new_cases = df.loc[df["New cases"].idxmax()]
max_new_deaths = df.loc[df["New deaths"].idxmax()]
max_new_recovered = df.loc[df["New recovered"].idxmax()]
max_active = df.loc[df["Active"].idxmax()]


print("\n===================================")
print("       COVID-19 KEY INSIGHTS")
print("===================================")

print("\nHighest New Cases:")
print("Date:", max_new_cases["Date"].date())
print("Cases:", max_new_cases["New cases"])

print("\nHighest New Deaths:")
print("Date:", max_new_deaths["Date"].date())
print("Deaths:", max_new_deaths["New deaths"])

print("\nHighest New Recoveries:")
print("Date:", max_new_recovered["Date"].date())
print("Recovered:", max_new_recovered["New recovered"])

print("\nPeak Active Cases:")
print("Date:", max_active["Date"].date())
print("Active Cases:", max_active["Active"])

print("\n===================================")
print("          ANALYSIS COMPLETE")
print("===================================")
# ==========================================
# 9. COVID-19 SUMMARY DASHBOARD
# ==========================================

# ==========================================
# 9. COVID-19 SUMMARY DASHBOARD
# ==========================================

summary_data = {
    "Confirmed": df["Confirmed"].max(),
    "Deaths": df["Deaths"].max(),
    "Recovered": df["Recovered"].max(),
    "Active": df["Active"].max()
}

colors = ["blue", "red", "green", "orange"]

plt.figure(figsize=(10, 6))

bars = plt.bar(
    summary_data.keys(),
    summary_data.values(),
    color=colors
)

plt.title("COVID-19 Overall Summary")
plt.xlabel("Category")
plt.ylabel("Number of Cases")

# Show values on top of bars
for bar in bars:
    value = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"{int(value):,}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("graphs/confirmed_cases.png")
plt.show()

# ==========================================
# 10. FINAL ANALYSIS
# ==========================================

total_confirmed = df["Confirmed"].max()
total_deaths = df["Deaths"].max()
total_recovered = df["Recovered"].max()
peak_active = df["Active"].max()

death_rate = (total_deaths / total_confirmed) * 100
recovery_rate = (total_recovered / total_confirmed) * 100

print("\n===================================")
print("          FINAL ANALYSIS")
print("===================================")

print(f"\nOverall Confirmed Cases: {total_confirmed:,}")
print(f"Overall Deaths: {total_deaths:,}")
print(f"Overall Recovered: {total_recovered:,}")
print(f"Peak Active Cases: {peak_active:,}")

print(f"\nDeath Rate: {death_rate:.2f}%")
print(f"Recovery Rate: {recovery_rate:.2f}%")

print("\n===================================")
print("       PROJECT COMPLETED")
print("===================================")