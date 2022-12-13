# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 19:20:08 2021
@author: DELL PC
"""

update_x = [0]
update_y1 = [0]
update_y2 = [0]


def Step_size():
    step = [0, 1, 2, 3, 4]
    h = (step[len(step) - 1] - step[0])/(len(step) - 1)
    return h

def function_1(x, y1, y2):
    f1 = 2 - x*y1 - pow(y2, 2)
    return f1

def function_2(x, y1, y2):
    f2 = 1 - pow(x, 2) - y1*y2
    return f2

count = 0
i = 1
for x,y1,y2 in zip(update_x, update_y1, update_y2):
    print(" ______________ \n")
    print(f"-> ITERATION {i}:\n ______________ \n")
    
    k11 = Step_size()*function_1(x, y1, y2)
    print("k11 = hf1(x, y1, y2)")
    print(f"k11 = {Step_size()}*f1({x}, {y1}, {y2})")
    print(f"k11 = {k11}\n")
    k12 = Step_size()*function_2(x, y1, y2)
    print("k12 = hf2(x, y1, y2)")
    print(f"k12 = {Step_size()}*f2({x}, {y1}, {y2})")
    print(f"k12 = {k12}")
    print("\n\n")
    
    
    k21 = Step_size()*function_1(x + 0.5*Step_size(), y1 + 0.5*k11, y2 + 0.5*k12)
    print("k21 = hf1(x + 1/2h, y1 + k11, y2 + k12)")
    print(f"k21 = {Step_size()}*f1({x} + {0.5*Step_size()}, {y1} + {0.5*k11}, {y2} + {0.5*k12})")
    print(f"k21 = {k21}\n")
    k22 = Step_size()*function_2(x + 0.5*Step_size(), y1 + 0.5*k11, y2 + 0.5*k12)
    print("k22 = hf2(x + 1/2h, y1 + k11, y2 + k12)")
    print(f"k22 = {Step_size()}*f1({x} + {0.5*Step_size()}, {y1} + {0.5*k11}, {y2} + {0.5*k12})")
    print(f"k22 = {k22}")
    print("\n\n")

    k31 = Step_size()*function_1(x + 0.5*Step_size(), y1 + 0.5*k21, y2 + 0.5*k22)
    print("k31 = hf1(x + 1/2h, y1 + k21, y2 + k22)")
    print(f"k31 = {Step_size()}*f1({x} + {0.5*Step_size()}, {y1} + {0.5*k21}, {y2} + {0.5*k22})")
    print(f"k31 = {k31}\n")
    k32 = Step_size()*function_2(x + 0.5*Step_size(), y1 + 0.5*k21, y2 + 0.5*k22)
    print("k32 = hf1(x + 1/2h, y1 + k21, y2 + k22)")
    print(f"k32 = {Step_size()}*f1({x} + {0.5*Step_size()}, {y1} + {0.5*k21}, {y2} + {0.5*k22})")
    print(f"k32 = {k32}")
    print("\n\n")
    
    k41 = Step_size()*function_1(x + 0.5*Step_size(), y1 + 0.5*k31, y2 + 0.5*k32)
    print("k41 = hf1(x + 1/2h, y1 + k31, y2 + k32)")
    print(f"k41 = {Step_size()}*f1({x} + {0.5*Step_size()}, {y1} + {0.5*k31}, {y2} + {0.5*k32})")
    print(f"k41 = {k41}\n")
    k42 = Step_size()*function_2(x + 0.5*Step_size(), y1 + 0.5*k31, y2 + 0.5*k32)
    print("k42 = hf1(x + 1/2h, y1 + k31, y2 + k32)")
    print(f"k42 = {Step_size()}*f1({x} + {0.5*Step_size()}, {y1} + {0.5*k31}, {y2} + {0.5*k32})")
    print(f"k42 = {k42}")
    print("\n\n")
    
    det_y1 = 1/6*(k11 + 2*k21 + 2*k31 + k41)
    print("Dy[1n] = 1/6*(k11 + 2*k21 + 2*k31 + k41)")
    print(f"Dy[1n] = {det_y1}\n")
    det_y2 = 1/6*(k12 + 2*k22 + 2*k32 + k42)
    print("Dy[2n] = 1/6*(k12 + 2*k22 + 2*k32 + k42)")
    print(f"Dy[2n] = {det_y2}")
    print("\n\n")
    
    new_x = x + 1
    update_x.append(new_x)
    print("x[n+1] = xn + h")
    print(f"X[n+1] = {new_x}\n")
    
    new_y1 = y1 + det_y1
    update_y1.append(new_y1)
    print("Y[1, n+1] = y1 + Dy[1n]")
    print(f"Y[1, n+1] = {new_y1}\n")
    
    new_y2 = y2 + det_y2
    update_y2.append(new_y2)
    print("Y[2, n+1] = y2 + Dy[2n]")
    print(f"Y[2, n+1] = {new_y2}")
    
    print("\n\n\n\n")
    
    count += 1
    i += 1
    
    if count == 5:
        break