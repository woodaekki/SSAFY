arr = [2, 3, 7]
for i1 in range(3):
    for i2 in range(3): #[1[123]
        if i1 != i2: # [1[23]]
            for i3 in range(3): # [1[23][123]]
                if i1 != i3 and i2 != i3: # [1[2][3]]
                    print(arr[i1], arr[i2], arr[i3])