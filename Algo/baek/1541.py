formula = input()

formula_list = formula.split('-')
answer = 0

for i in range(len(formula_list)):
    if i == 0:
        p_temp = list(map(int, formula_list[i].split('+')))
        answer += sum(p_temp)
    else:
        m_temp = list(map(int, formula_list[i].split('+')))
        answer += -sum(m_temp)

print(answer)