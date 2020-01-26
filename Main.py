# TODO ::  solving hanoi's tower problem using recursion

A = "A"
B = "B"
C = "C"


def move(initial, target):
    print(f"move {initial} to {target}")


def hanoi(NumberOfDisk, FromPosition=A, HelperPosition=B, TargetPosition=C):
    if NumberOfDisk == 0:
        pass
    else:
        hanoi(NumberOfDisk - 1, FromPosition, TargetPosition, HelperPosition)
        move(FromPosition, TargetPosition)
        hanoi(NumberOfDisk - 1, HelperPosition, FromPosition, TargetPosition)
