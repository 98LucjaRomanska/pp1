def min_pts(limit):
    def check(pts):
        if pts >= limit:
            return True
        return False
    return check

print(min_pts(50))
#przeanalizować zad 12 i zrobić 13
