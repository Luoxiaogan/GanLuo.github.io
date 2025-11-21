import matplotlib.pyplot as plt
import numpy as np

# Define score range
x = np.linspace(70, 100, 1000)

# Calculate GPA
GPA = 4 - 3 * (100 - x)**2 / 1600

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, GPA, linewidth=2, color='blue')
plt.xlabel('Score', fontsize=12)
plt.ylabel('GPA', fontsize=12)
plt.title('Relationship between GPA and Score', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xlim(70, 100)
plt.ylim(2.0, 4.2)

# Add reference lines
plt.axhline(y=4.0, color='r', linestyle='--', alpha=0.5, label='GPA=4.0')
plt.axvline(x=100, color='g', linestyle='--', alpha=0.5, label='Perfect Score')

plt.legend()
plt.tight_layout()
plt.savefig('./Transcript_and_Enrollment/gpa_score_relationship.png', dpi=300)
plt.show()