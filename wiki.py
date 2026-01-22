import re
import urllib.request
import matplotlib.pyplot as plt
#visit the webpage:
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0')]
infile = opener.open('https://en.wikipedia.org/wiki/Charles_Darwin')
hand = infile.read().splitlines()
years = []
for line in hand:
    line = line.decode('utf-8').strip()
    years_result = re.findall(r'\b(18\d{2})\b' , line)
    for i in years_result:
        years.append(int(i))
print("total years found", len(years))
print("min:", min(years), "max:", max(years))

plt.hist(years,bins='auto', histtype= 'bar')
plt.xlabel("Years")
plt.ylabel("Count")
plt.title('Charles Darwin years')
plt.show()