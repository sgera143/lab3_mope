import numpy as np, random

x1_min = -30
x1_max = 20
x2_min = -25
x2_max = 10
x3_min = -30
x3_max = -15

x_midlle_max = (x1_max + x2_max + x3_max) / 3
x_midlle_min = (x1_min + x2_min + x3_min) / 3
y_max = 200 + x_midlle_max
y_min = 200 + x_midlle_min

m = 3
n = 4
q = 0.5

def matrix(mtrx):
    for i in range(len(mtrx)):
        print("{}.".format(i + 1), end = "")
        for j in range(len(mtrx[i])):
            print("{:7}".format(mtrx[i][j]), end = "")
        print()

def lab3(m, n, q):
    print("Матриця кодових значень")
    x_code = np.array([[+1, -1, -1, -1], [+1, -1, +1, +1], [+1, +1, -1, +1], [+1, +1, +1, -1]])
    matrix(x_code)

    print("Матриця іксів:")
    x = np.array([[x1_min, x2_min, x3_min], [x1_min, x2_max, x3_max], [x1_max, x2_min, x3_max], [x1_max, x2_max, x3_min]])
    matrix(x)

    print("Матриця ігриків:")
    y = np.random.randint(y_min, y_max, size = (n, m))
    matrix(y)

    print("Середні значення функцій відгуку:")
    y_midlle = np.sum(y, axis = 1) / len(y[0])
    y_1, y_2, y_3, y_4 = y_midlle
    print(f"y_1 = {y_1:.2f}\ny_2 = {y_2:.2f}\ny_3 = {y_3:.2f}\ny_4 = {y_4:.2f}")
    mx_1, mx_2, mx_3 = [i / len(x) for i in np.sum(x, axis = 0)]
    my = sum(y_midlle) / len(y_midlle)

    a_1 = sum([x[i][0] * y_midlle[i] for i in range(len(x))]) / len(x)
    a_2 = sum([x[i][1] * y_midlle[i] for i in range(len(x))]) / len(x)
    a_3 = sum([x[i][2] * y_midlle[i] for i in range(len(x))]) / len(x)

    a_11 = sum([x[i][0] ** 2 for i in range(len(x))]) / len(x)
    a_22 = sum([x[i][1] ** 2 for i in range(len(x))]) / len(x)
    a_33 = sum([x[i][2] ** 2 for i in range(len(x))]) / len(x)
    a_12 = sum([x[i][0] * x[i][1] for i in range(len(x))]) / len(x)
    a_13 = sum([x[i][0] * x[i][2] for i in range(len(x))]) / len(x)
    a_23 = a_32 = sum([x[i][1] * x[i][2] for i in range(len(x))]) / len(x)

    det = np.linalg.det([[1, mx_1, mx_2, mx_3], [mx_1, a_11, a_12, a_13], [mx_2, a_12, a_22, a_32], [mx_3, a_13, a_23, a_33]])
    det_0 = np.linalg.det([[my, mx_1, mx_2, mx_3], [a_1, a_11, a_12, a_13], [a_2, a_12, a_22, a_32], [a_3, a_13, a_23, a_33]])
    det_1 = np.linalg.det([[1, my, mx_2, mx_3], [mx_1, a_1, a_12, a_13], [mx_2, a_2, a_22, a_32], [mx_3, a_3, a_23, a_33]])
    det_2 = np.linalg.det([[1, mx_1, my, mx_3], [mx_1, a_11, a_1, a_13], [mx_2, a_12, a_2, a_32], [mx_3, a_13, a_3, a_33]])
    det_3 = np.linalg.det([[1, mx_1, mx_2, my], [mx_1, a_11, a_12, a_1], [mx_2, a_12, a_22, a_2], [mx_3, a_13, a_23, a_3]])

    b_0 = det_0 / det
    b_1 = det_1 / det
    b_2 = det_2 / det
    b_3 = det_3 / det
    b = [b_0, b_1, b_2, b_3]

    print("Нормоване рівняння регресії:: y = {0} + {1} * x1 + {2} * x2 + {3} * x3\n".format(round(b_0, 5), round(b_1, 5), round(b_2, 5), round(b_3, 5)))
    print("Перевірка:")
    y_1_exp = b_0 + b_1 * x[0][0] + b_2 * x[0][1] + b_3 * x[0][2]
    y_2_exp = b_0 + b_1 * x[1][0] + b_2 * x[1][1] + b_3 * x[1][2]
    y_3_exp = b_0 + b_1 * x[2][0] + b_2 * x[2][1] + b_3 * x[2][2]
    y_4_exp = b_0 + b_1 * x[3][0] + b_2 * x[3][1] + b_3 * x[3][2]
    print(f"y_1 = {b_0:.3f} + {b_1:.3f} * {x[0][0]} + {b_2:.3f} * {x[0][1]} + {b_3:.3f} * {x[0][2]} = {y_1_exp:.3f}"
          f"\ny_2 = {b_0:.3f} + {b_1:.3f} * {x[1][0]} + {b_2:.3f} * {x[1][1]} + {b_3:.3f} * {x[1][2]} = {y_2_exp:.3f}"
          f"\ny_3 = {b_0:.3f} + {b_1:.3f} * {x[2][0]} + {b_2:.3f} * {x[2][1]} + {b_3:.3f} * {x[2][2]} = {y_3_exp:.3f}"
          f"\ny_4 = {b_0:.3f} + {b_1:.3f} * {x[3][0]} + {b_2:.3f} * {x[3][1]} + {b_3:.3f} * {x[3][2]} = {y_4_exp:.3f}")

    print("\nКритерій Кохрена")
    f_1 = m - 1
    f_2 = n
    s_1 = sum([(i - y_1) ** 2 for i in y[0]]) / m
    s_2 = sum([(i - y_2) ** 2 for i in y[1]]) / m
    s_3 = sum([(i - y_3) ** 2 for i in y[2]]) / m
    s_4 = sum([(i - y_4) ** 2 for i in y[3]]) / m
    s_array = np.array([s_1, s_2, s_3, s_4])
    gP = max(s_array) / sum(s_array)

    table = {3: 0.6841, 4: 0.6287, 5: 0.5892, 6: 0.5598, 7: 0.5365, 8: 0.5175, 9: 0.5017, 10: 0.4884, range(11, 17): 0.4366, range(17, 37): 0.3720, range(37, 145): 0.3093}
    gT = table.get(m)

    if(gP < gT):
        print(f"Дисперсія однорідна: Gp = {gP:.5} < Gt = {gT}")
    else:
        print(f"Дисперсія не однорідна Gp = {gP:.5} < Gt = {gT}")
        m = m + 1
        lab3(m + 1, n, q)
        return

    print("\nКритерій Стьюдента")
    s2_B = s_array.sum() / n
    s2_beta_S = s2_B / (n * m)
    s_beta_S = pow(s2_beta_S, 1/2)

    beta_0 = sum([x_code[i][0] * y_midlle[i] for i in range(len(x_code))]) / n
    beta_1 = sum([x_code[i][1] * y_midlle[i] for i in range(len(x_code))]) / n
    beta_2 = sum([x_code[i][2] * y_midlle[i] for i in range(len(x_code))]) / n
    beta_3 = sum([x_code[i][3] * y_midlle[i] for i in range(len(x_code))]) / n

    t = [abs(beta_0) / s_beta_S, abs(beta_1) / s_beta_S, abs(beta_2) / s_beta_S, abs(beta_3) / s_beta_S ]

    f3 = f_1 * f_2
    t_table = {8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131, 16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 21: 2.08, 22: 2.074, 23: 2.069, 24: 2.064, 25: 2.06}
    d = 4

    for i in range(len(t)):
        if(t_table.get(f3) > t[i]):
            b[i] = 0
            d -= 1

    print(f"Рівняння регресії: y = {b[0]:.3f} + {b[1]:.3f} * x1 + {b[2]:.3f} * x2 + {b[3]:.3f} * x3")
    check_0 = b[0] + b[1] * x[0][0] + b[2] * x[0][1] + b[3] * x[0][2]
    check_1 = b[0] + b[1] * x[1][0] + b[2] * x[1][1] + b[3] * x[1][2]
    check_2 = b[0] + b[1] * x[2][0] + b[2] * x[2][1] + b[3] * x[2][2]
    check_3 = b[0] + b[1] * x[3][0] + b[2] * x[3][1] + b[3] * x[3][2]
    ckeck_list = [check_0, check_1, check_2, check_3]
    print("Значення у нормованих: ", ckeck_list)

    print("\nКритерій Фішера")
    f_4 = n - d
    s2_ad = m / f_4 * sum([(ckeck_list[i] - y_midlle[i]) ** 2 for i in range(len(y_midlle))])
    fP = s2_ad / s2_B
    fT = [[164.4, 199.5, 215.7, 224.6, 230.2, 234], [18.5, 19.2, 19.2, 19.3, 19.3, 19.3],
         [10.1, 9.6, 9.3, 9.1, 9, 8.9], [7.7, 6.9, 6.6, 6.4, 6.3, 6.2], [6.6, 5.8, 5.4, 5.2, 5.1, 5],
		 [6, 5.1, 4.8, 4.5, 4.4, 4.3], [5.5, 4.7, 4.4, 4.1, 4, 3.9], [5.3, 4.5, 4.1, 3.8, 3.7, 3.6],
		 [5.1, 4.3, 3.9, 3.6, 3.5, 3.4], [5, 4.1, 3.7, 3.5, 3.3, 3.2], [4.8, 4, 3.6, 3.4, 3.2, 3.1],
		 [4.8, 3.9, 3.5, 3.3, 3.1, 3], [4.7, 3.8, 3.4, 3.2, 3, 2.9], [4.6, 3.7, 3.3, 3.1, 3, 2.9],
		 [4.5, 3.7, 3.3, 3.1, 2.9, 2.8], [4.5, 3.6, 3.2, 3, 2.9, 2.7], [4.5, 3.6, 3.2, 3, 2.8, 2.7],
		 [4.4, 3.6, 3.2, 2.9, 2.8, 2.7], [4.4, 3.5, 3.1, 2.9, 2.7, 2.6], [4.4, 3.5, 3.1, 2.9, 2.7, 2.6]]
    if(fP > fT[f3][f_4]):
        print(f"fp = {fP} > ft = {fT[f3][f_4]}.\nМатематична модель не адекватна експериментальним даним")
    else:
    	print(f"fP = {fP} < fT = {fT}.\nМатематична модель адекватна експериментальним даним")

print("Рівняння регресії --- y = b_0 + b_1 * x1 + b_1 * x2 +b_3 * x3")
lab3(m, n, q)