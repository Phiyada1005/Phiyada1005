print('KPH\tMPH')
print('________')

for kph in range(60,140,10):
    mp = kph*0.6241
    print(kph, '\t', format(mph,".1f"))