import matplotlib.pyplot as plt

# Sample data
sizes = [30, 20, 15, 35]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0, wedgeprops=dict(width=0.3))
plt.title('Donut Chart')
plt.show()
