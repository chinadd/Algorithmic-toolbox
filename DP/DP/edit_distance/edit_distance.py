# Uses python3
def edit_distance(s1, s2):
    #write your code here
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        print (distances_)
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1]) #match
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))#mismatch,insertion,deletion
        print (distances_)
        distances = distances_
    return distances[-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
