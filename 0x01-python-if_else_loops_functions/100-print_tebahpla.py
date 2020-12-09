#!/usr/bin/python3
for aux in range(-122, -96):
    aux = abs(aux)
    if aux % 2 == 0:
        print("{:c}".format(aux), end="")
    else:
        print("{:c}".format(aux - 32), end="")
