import re
import matplotlib.pyplot as plt

fname = "mbox.txt"
fhand = open(fname)
months = []
days = []
for line in fhand:
    line = line.strip()
    if line.startswith("From "):
        result = re.findall('(Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', line)
        for item in result:
            days.append(item[0])
            months.append(item[1])
    
print("total emails:", len(days))

plt.hist(months, bins='auto', histtype='bar')
plt.xlabel("Month")
plt.ylabel("Count")
plt.title("Emails by Month")
plt.show()

plt.hist(days, bins='auto', histtype='bar')
plt.xlabel("Day of Week")
plt.ylabel("Count")
plt.title("Emails by Day of Week")
plt.show()