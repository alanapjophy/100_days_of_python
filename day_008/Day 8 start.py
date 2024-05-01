def paint_calc(height, width, cover):
    number_of_cans = (height * width)/ cover
    print(f"You'll need {number_of_cans} cans paint")


test_h = int(input("Enter the height of the wall:"))
test_w = int(input("Enter the width of the wall:"))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)