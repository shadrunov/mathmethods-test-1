import task2

def test_201():
    list_a=[4,1,5,8,3,6,2,7,10,9]
    list_b=[7,5,4,8,3,10,1,2,6,9]
    result=task2.solve(list_a, list_b,1751,1996) 
    assert result == [4, 3, 8, 7, 5, 9, 2, 1, 6, 10] 
def test_sem():
    list_a=[5,9,3,6,1,7,4,8,10,2]
    list_b=[5,9,1,2,3,7,4,10,6,8]
    result=task2.solve(list_a, list_b,1,114)
    assert result == [5, 6, 3, 4, 1 ,10, 7, 8, 9, 2]
test_201()
test_sem()