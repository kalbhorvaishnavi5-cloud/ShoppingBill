def calculateElectronicsGST(a, b):
    subtotal = a + b
    gst = subtotal * 18 / 100
    total = subtotal + gst

    return total



def calculateFashionGST(c, d):
    subtotal = c + d
    gst = subtotal * 13 / 100
    total = subtotal + gst

    return total



def calculateFoodGST(e):
    gst = e * 7 / 100
    total = e + gst

    return total



def totalBill(a, b, c, d, e):
    electronics_total = calculateElectronicsGST(a, b)
    fashion_total = calculateFashionGST(c, d)
    food_total = calculateFoodGST(e)

    total = electronics_total + fashion_total + food_total

    return total



def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)

    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount



a = 100
b = 100
c = 100
d = 100
e = 100



electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)



print("......... SHOPPING BILL .........")

print(f"Electronics + 18% GST : Rs. {electronics:.2f}")
print(f"Fashion + 13% GST     : Rs. {fashion:.2f}")
print(f"Food + 7% GST         : Rs. {food:.2f}")

print("-----------------------------------")

print(f"Total After GST       : Rs. {total:.2f}")
print(f"20% Discount          : Rs. {discount:.2f}")

print("-----------------------------------")

print(f"Final Payable Amount  : Rs. {final_amount:.2f}")

print("===================================")