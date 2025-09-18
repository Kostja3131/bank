#MATRIX = []
#DEMAND =[]
PROPABILITY = (0.1,0.3,0.4,0.2)
ALPHA = 0.7
RES = [0,0,0,0]

MATRIX = [[0,-2.5,-5,-7.5],
          [-8,0,-2.5,-5],
          [-16,-8,0,-2.5],
          [-24,-16,-8,0]]

DEMAND = [11,12,13,14]

MATRIX = [[0,-16,-32,-78],
           [-8,0,-16,-32],
           [-16,-8,0,-16],
           [-24,-16,-8,0]]


DEMAND = [11+27,12+27,13+27,14+27]

def main():
    input_data()
    Wald()
    Bayes()
    Laplace()
    Hurwitz()
    Savage()

    print(f"\nЛУЧАШЯ СТРАТЕГИЯ A{RES.index(max(RES))+1}")


def input_data():
    print("Введите матрицу!")
    for i in range(4):
        print(f"Строка {i+1}: ", end="")
        MATRIX.append(list(map(float, input().split()))[:4])
    print("\nВведите спрос: ", end="")
    DEMAND.append(list(map(int, input().split()))[:4])

def show_result(criteria, row):
    RES[row] += 1
    print(f"По критерию {criteria} следует взять стратегию A{row+1} и заказывать/завозить {DEMAND[row]} единиц товара.")

def Wald():
    a = []
    for row in MATRIX:
        print(row)
        a.append(min(row))
    show_result("Вальда",a.index(max(a)))

def Bayes():
    a_ = []
    for row in MATRIX:
        a_.append(row[0]*PROPABILITY[0]+row[1]*PROPABILITY[1]+row[2]*PROPABILITY[2]+row[3]*PROPABILITY[3])
    show_result("Байеса",a_.index(max(a_)))

def Laplace():
    q = sum(PROPABILITY)/len(PROPABILITY)
    a = []
    for row in MATRIX:
        a.append(q*sum(row))
    show_result("Лапласа",a.index(max(a)))

def Hurwitz():
    a = []
    for row in MATRIX:
        a.append(min(row)*0.7)
    show_result("Гурвица",a.index(max(a)))

def Savage():
    r = []
    for row in MATRIX:
        r.append([max(row)-row[0],max(row)-row[1],max(row)-row[2],max(row)-row[3]])
    res = []
    for row in r:
        res.append(max(row))

    show_result("Сэвиджа",res.index(min(res)))

main()