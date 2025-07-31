import matplotlib.pyplot as plt

# Sample data from the image
age_groups = ['0 to 20 Years', '21 to 64 Years', '65+ Years']
population_mn = [512, 807, 98]
percentage = [36.1, 57.0, 6.9]

# Bar chart
plt.bar(age_groups, population_mn, color=['yellow', 'blue', 'magenta'])

# Titles and labels
plt.title("India's Population Distribution by Age (2022)")
plt.xlabel("Age Groups")
plt.ylabel("Population (in Millions)")

# Show population percentage on top of each bar
for i in range(len(age_groups)):
    plt.text(i, population_mn[i] + 10, f"{percentage[i]}%", ha='center')

# Show the chart
plt.show()
