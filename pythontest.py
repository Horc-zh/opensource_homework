class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)

print()
colours = ["红", "绿", "黄", "蓝"]
things = ["房子", "车", "树"]
combined = [(x, y) for x in colours for y in things]

print(combined)
