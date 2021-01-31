
def sales_tax():
    x = int(input("Please give me the subtotal: "))
    tax = x * .0825
    total = tax + x
    return print("The total after tax is {}".format(total))

if __name__ == "__main__":
    sales_tax()
