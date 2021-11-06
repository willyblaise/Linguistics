

temps = [("LA", 20), ("Chicago", 15), ("Dallas", 25), ("New York", 12)]

c_to_f = lambda data : ( data[0], 9/5 * data[1] + 32)


converted_temps = list(map(c_to_f, temps))

print(converted_temps)
