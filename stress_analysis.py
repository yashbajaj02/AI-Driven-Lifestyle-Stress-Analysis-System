# ============================================
# AI-DRIVEN LIFESTYLE STRESS ANALYSIS SYSTEM
# (COLOR OPTIMIZED VERSION)
# ============================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)

# ============================================
# 1. USER INPUT
# ============================================

print("ENTER YOUR LIFESTYLE DETAILS\n")

sleep = float(input("Sleep hours per day: "))
screen = float(input("Screen time per day (hours): "))
work = float(input("Work/Study hours per day: "))
activity_week = float(input("Physical activity per week (hours): "))

activity = activity_week / 7   # per day conversion

# ============================================
# 2. STRESS SCORE CALCULATION (1–100)
# ============================================

raw_score = (
    70
    + 4 * screen
    + 3 * work
    - 5 * sleep
    - 6 * activity
)

stress_score = int(max(1, min(100, round(raw_score))))

print("\n--------------------------------")
print("STRESS SCORE:", stress_score, "/100")

# ============================================
# 3. STRESS LEVEL (EVERY 5 POINTS)
# ============================================

stress_band = (stress_score - 1) // 5 + 1

levels = {
    1: "Very Relaxed", 2: "Relaxed", 3: "Calm", 4: "Balanced",
    5: "Mild Stress", 6: "Noticeable Stress", 7: "Elevated Stress",
    8: "High Stress", 9: "Very High Stress", 10: "Critical Stress",
    11: "Extreme Stress", 12: "Burnout Risk", 13: "Severe Burnout",
    14: "Mental Overload", 15: "Emergency Level", 16: "Collapse Risk",
    17: "Health Risk Zone", 18: "Severe Health Risk",
    19: "Psychological Alert", 20: "Immediate Attention Needed"
}

level_name = levels[stress_band]
print("STRESS LEVEL:", level_name)

# ============================================
# 4. AI SUGGESTION ENGINE
# ============================================

solutions = {
    range(1,5): [
        "Maintain current routine",
        "Light meditation",
        "Healthy sleep cycle",
        "Social interaction"
    ],
    range(5,9): [
        "Daily walking",
        "Reduce screen time",
        "Breathing exercises",
        "Relaxing music"
    ],
    range(9,13): [
        "Regular exercise",
        "Time management",
        "Improve sleep quality",
        "Limit social media"
    ],
    range(13,17): [
        "Yoga & mindfulness",
        "Strict work breaks",
        "Talk to family/friends",
        "Digital detox"
    ],
    range(17,21): [
        "Professional counseling",
        "Medical consultation",
        "Guided meditation",
        "Immediate lifestyle change"
    ]
}

print("\nAI RECOMMENDED STRESS RELEASE OPTIONS:")
for band_range, advice in solutions.items():
    if stress_band in band_range:
        for i, opt in enumerate(advice, 1):
            print(f"{i}. {opt}")

# ============================================
# 5. PIE CHART – DAILY TIME DISTRIBUTION
# ============================================

labels = ['Sleep', 'Screen', 'Work', 'Physical Activity', 'Other']
other = max(0, 24 - (sleep + screen + work + activity))
sizes = [sleep, screen, work, activity, other]

pie_colors = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#BDBDBD']

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        startangle=90, colors=pie_colors)
plt.title("Daily Time Distribution")
plt.show()

# ============================================
# 6. BAR CHART – LIFESTYLE COMPARISON
# ============================================

categories = ['Sleep', 'Screen', 'Work', 'Physical Activity']
values = [sleep, screen, work, activity]

bar_colors = ['#2E7D32', '#1565C0', '#EF6C00', '#6A1B9A']

plt.figure()
plt.bar(categories, values, color=bar_colors)
plt.ylabel("Hours per day")
plt.title("Lifestyle Factors Comparison")
plt.show()

# ============================================
# 7. LINE GRAPH – WEEKLY STRESS TREND
# ============================================

days = np.arange(1, 8)
stress_trend = stress_score + np.random.normal(0, 3, 7)

plt.figure()
plt.plot(days, stress_trend,
         color='#D32F2F', marker='o', linewidth=2)
plt.xlabel("Day")
plt.ylabel("Stress Score")
plt.title("Weekly Stress Trend")
plt.grid(True)
plt.show()

# ============================================
# 8. HISTOGRAM – GLOBAL STRESS DISTRIBUTION
# ============================================

population = np.random.normal(65, 10, 1000)

plt.figure()
plt.hist(population, bins=20,
         color='#03A9F4', edgecolor='black')
plt.axvline(stress_score, color='red', linewidth=2)
plt.xlabel("Stress Score")
plt.ylabel("Frequency")
plt.title("Global Stress Score Comparison")
plt.show()

# ============================================
# 9. SCATTER PLOT – SCREEN TIME vs STRESS
# ============================================

screen_vals = np.random.normal(6, 2, 50)
stress_vals = 70 + 4 * screen_vals + np.random.normal(0, 5, 50)

plt.figure()
plt.scatter(screen_vals, stress_vals,
            color='#8E24AA', alpha=0.7)
plt.xlabel("Screen Time (hrs/day)")
plt.ylabel("Stress Score")
plt.title("Screen Time vs Stress Relationship")
plt.show()

# ============================================
# 10. COLOR-CODED STRESS DASHBOARD
# ============================================

levels_range = list(range(1, 101))
colors = []

for i in levels_range:
    if i <= 30:
        colors.append('#4CAF50')   # green
    elif i <= 60:
        colors.append('#FFEB3B')   # yellow
    elif i <= 80:
        colors.append('#FF9800')   # orange
    else:
        colors.append('#F44336')   # red

plt.figure(figsize=(10,3))
plt.bar(levels_range, [1]*100, color=colors)
plt.axvline(stress_score, color='black', linewidth=3)
plt.yticks([])
plt.xlabel("Stress Score")
plt.title("Stress Severity Dashboard (Safe → Danger)")
plt.show()

# ============================================
# 11. PROBABILITY INTERPRETATION
# ============================================

prob_high = 1 - norm.cdf(stress_score, 65, 10)

print("\nPROBABILITY INSIGHT:")
print("Probability of stress being higher than global average:",
      round(prob_high, 2))

# ============================================
# 12. FINAL AI SUMMARY
# ============================================

print("\n----------- FINAL AI SUMMARY -----------")
print(f"Stress Score: {stress_score}/100")
print(f"Stress Level: {level_name}")

if stress_score <= 30:
    print("AI Insight: Excellent stress management. Keep it up.")
elif stress_score <= 60:
    print("AI Insight: Moderate stress. Small improvements needed.")
elif stress_score <= 80:
    print("AI Insight: High stress. Immediate correction advised.")
else:
    print("AI Insight: Critical stress. Professional help recommended.")
