for i in range(2, 21):
    with open(f"Tables/Multiplication_Table{i}.txt",'w') as f:
        for j in range(1, 11):
            f.write(f" {i} * {j} = {i*j}")
            if j!=10:
                f.write('\n')

    