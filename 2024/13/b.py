import re
import numpy as np
from sympy import symbols, Eq, solve
from sympy.solvers.diophantine import diophantine

def cheapestPath(ax, ay, bx, by, px, py):
    # A, B = symbols('A B', integer=True)
    # eq1 = Eq(A*ax + B*bx, px)
    # eq2 = Eq(A*ay + B*by, py)
    # A_solve = solve(eq1, A)
    # if not len(A_solve):
    #     return 0
    # A_solve = A_solve[0]
    # sub_eq2 = eq2.subs(A, A_solve)
    # if sub_eq2 == False:
    #     return 0
    # b_val = diophantine(sub_eq2)
    
    # if not len(b_val):
    #     return 0
    
    # max_b = 0
    # for b in b_val:
    #     max_b = max(max_b, b[0])

    # print(A_solve.subs(B, max_b), max_b)
    # return 3*A_solve.subs(B, max_b) + max_b

    # print(sols)
    coeff_mat = np.array([[ax, bx], [ay, by]])
    result_mat = np.array([px, py])
    try:
        solution = np.linalg.solve(coeff_mat, result_mat)
        press_a, press_b = solution
        if ax*round(press_a) + bx*round(press_b) == px and ay*round(press_a) + by*round(press_b) == py:
            return 3*round(press_a) + round(press_b)
        
        # if abs(round(press_a) - press_a < 1e-20) and abs(round(press_b) - press_b < 1e-20):
        #     print("ROUND", round(press_a), round(press_b))
        #     print("close", press_a, press_b)
        #     return 3*round(press_a) + round(press_b)
        else:
            # print("TOO BAD", press_a, press_b)
            return 0

    except np.linalg.LinAlgError:
        return 0

def generateSolution(filename):
    with open(filename) as f:
        f_input = f.read().strip()

    all_A = re.findall(r"A:.*", f_input)
    all_B = re.findall(r"B:.*", f_input)
    all_prize = re.findall(r"Prize:.*", f_input)

    total_cost = 0
    for i in range(len(all_A)):
        ax, ay = map(int, re.findall(r"\d+", all_A[i]))
        bx, by = map(int, re.findall(r"\d+", all_B[i]))
        px, py = map(int, re.findall(r"\d+", all_prize[i]))

        print(f"{i} of {len(all_A)}")
        if (ax/bx == ay/by):
            print("VERY SCARY")
        # total_cost += cheapestPath(ax, ay, bx, by, px, py)
        total_cost += cheapestPath(ax, ay, bx, by, px+10000000000000, py+10000000000000)

    return total_cost


if __name__ == "__main__":
    print(generateSolution("ab.dat"))