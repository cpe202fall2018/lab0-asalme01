def weight_on_planets():
    weight_on_earth = input("What do you weigh on earth? ")
    weight = float(weight_on_earth)
    weight_on_mars = weight*0.38
    weight_on_jupiter = weight*2.34
    print("\nOn Mars you would weigh", "%.2f" % weight_on_mars, "pounds.\nOn Jupiter you would weigh", "%.2f" % weight_on_jupiter, "pounds.")
   
if __name__ == '__main__':
   weight_on_planets()