import matplotlib.pyplot as plt

month = ['Jan', 'Fab', 'March', 'April', 'May' , 'june', 'julay', 'ogust', 'sept', 'octo', 'desc']
sale = [35000,27000,48000,43000,50000,95000,50000,75000,68000,48500,35200,78000]


plt.bar(x = month, y=sale)
plt.show()