import sys

chords = list(map(int, sys.stdin.readline().rstrip().split()))

if chords == sorted(chords):
    print("ascending")
elif chords == sorted(chords, reverse=True):
    print("descending")
else:
    print("mixed")