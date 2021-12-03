def break_to_phi(some_arr:list)->list:
    """
    Разбивает перестановку 0..n на циклы
    Возвращает массив длин циклов
    """
    repl={}
    for i in range(len(some_arr)):
        repl[i+1]=some_arr[i]
    first=1
    new=-1
    phi=[]
    computed=[]
    while len(computed)!=len(some_arr):
        new_phi=[]
        cur=first
        new=-1
        while first!=new:
            new=repl[cur]
            new_phi.append(new)
            cur=new
        new_phi=[new_phi[-1]]+new_phi[:len(new_phi)-1]
        phi.append(new_phi)
        computed+=new_phi
        while (first in computed):
            if (len(computed)==len(some_arr)):
                break
            first+=1
            if first>len(some_arr):
                first=1           
    return phi

def cycle_power(some_arr: list, power : int)->list:
    """
    Возводит цикл в степень
    Возвращает его измененным или e
    """
    if power==0:
        return ['e']
    if power==1:
        return some_arr
    the_very_first=some_arr[0]
    repl={}
    for x in some_arr:
        repl[x]=some_arr[(some_arr.index(x)+power)%len(some_arr)]
    first=some_arr[0]
    new=-1
    phi=[]
    computed=[]
    while len(computed)!=len(some_arr):
        new_phi=[]
        cur=first
        new=-1
        while first!=new:
            new=repl[cur]
            new_phi.append(new)
            cur=new
        new_phi=[new_phi[-1]]+new_phi[:len(new_phi)-1]
        phi+=new_phi
        computed+=new_phi
        while (first in computed):
            if (len(computed)==len(some_arr)):
                break
            first+=1
            if first>len(some_arr):
                first=some_arr[0]       
    phi=phi[phi.index(the_very_first):]+phi[:phi.index(the_very_first)]
    return phi



def find(cycles: list, index:int):
    res=[]
    for cycle in cycles:
        if index in cycle: 
            moved=cycle[(cycle.index(index)+1)%len(cycle)]
            return moved
    return index


def solve(arr_a: list, arr_b: list, power_a : int, power_b:int):
    phi_a=break_to_phi(arr_a)
    phi_b=break_to_phi(arr_b)
    print(f"Циклы перестановки а: {phi_a}", '\n')
    print(f"Циклы перестановки b: {phi_b}", '\n')
    phi_a_reformed=[]
    phi_b_reformed=[]
    print(f'Cтепень а равна {power_a}:', '\n')
    for phi in phi_a:
        print(f"Цикл {phi} длины {len(phi)} получит степень {power_a%len(phi)}", '\n')
        phi_a_reformed.append(cycle_power(phi, power_a%len(phi)))
    print(f'Cтепень b равна {power_b}:', '\n')
    for phi in phi_b:
        print(f"Цикл {phi} длины {len(phi)} получит степень {power_b%len(phi)}" '\n')
        phi_b_reformed.append(cycle_power(phi,power_b%len(phi)))
    print("После преобразований а имеет вид:")
    for i in range(len(phi_a_reformed)):
        print(phi_a_reformed[i], end='')
    print('\n')
    print("После преобразований b имеет вид:")
    for i in range(len(phi_b_reformed)):
        print(phi_b_reformed[i], end='')
    print('\n')
    natural=[x+1 for x in range(len(arr_b))]
    averted_a=[]
    for i in range(1, len(arr_a)+1):
        averted_a.append(find(phi_a_reformed,i))
    print("Результат перестановки a:")
    print(natural)
    print(averted_a, '\n')
    averted_b=[]
    for i in range(1, len(arr_b)+1):
        averted_b.append(find(phi_b_reformed,i))
    print("Результат перестановки b:")
    print(natural)
    print(averted_b, '\n')
    final=[]
    for i in range(len(averted_b)):
        final.append(averted_a[averted_b[i]-1])
    print("Финальный результат:")
    print(natural)
    print(final, '\n')
    return final





if __name__=='__main__':
    a=input("Перестановка а, числа второй строки через пробел: ").split()
    a=list(map(int, a))
    b=input("Перестановка а, числа второй строки через пробел: ").split()
    b=list(map(int, b))
    pow_a=int(input("Степень a: "))
    pow_b=int(input("Степень b: "))