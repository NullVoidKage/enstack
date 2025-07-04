Given a list of tuples A = (x, y), where x is an integer from 0 to 13 and y is an integer from 0 to 3, with all possible values of A without repetition and sorted by y then x in ascending order, write a pseudocode to shuffle A.

Answer:

shuffle(list A):
    for i = last index down to 1:
        pick random j between 0 and i
        swap A[i] and A[j]
