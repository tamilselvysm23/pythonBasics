temperature=[10, 20, 50, 46, -35, -56, 232, 100, -45, 187]

def celsius_to_fahrenheit(temp):
    with open("temp.txt", "w") as myfile:
        for c in temperature:
            if c > 40:
                f = c*9/5+32
                myfile.write(str(f)+"\n")


celsius_to_fahrenheit(temperature)                