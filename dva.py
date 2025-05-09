class Moon:
    r = 1737.10

    def __lt__(self, other):
        print('moon lt')
        return self.r < other.r


class Earth:
    r = 6371.0

    def __lt__(self, other):
        print('earth lt')
        return self.r < other.r


my_moon = Moon()
my_earth = Earth()

is_lt = (my_moon < my_earth)  # moon lt
print(is_lt)  # True
