import os

users = ["kasun", "duleetha", "sachintha"]

print("1.login\n2.create a new account\n\n")

login = input("Enter the number of your choice:")
if login == "2":
    name = input("enter a username: ")
    users.append(name)
    print("Your password is 12345")
    print("1.login\n2.create a new account\n\n")
    login = input("Enter the number of your choice:")

if login == "1":
    # login.......
    username = input("enter the username: ")
    for i in users:
        if i == username:
            password = input("enter the password: ")
            break
    else:
        print("username not found.")

    if password == "12345":
        print("correct password")
        # revenue..............................
        revenue = []
        cost_of_sell = []
        Distribution_cost = []
        Admin_cost = []

        x = int(input("how many Revenues do you have?"))

        # Append revenues into the file........
        f = open("p&l.txt", "a")
        f.write("Revenues\n\n")

        # print(f"Enter your {x} Revenue one by one")
        for i in range(1, x + 1):
            rev_nm = input(f'{i} Revenues item name :')
            rev_vl = float(input(f'{i} Revenue item value: '))
            revenue.append(rev_vl)
            f.write(f'{rev_nm}\t- {rev_vl}\n')
        tot_revenue = sum(revenue)
        f.write(f'\nTotal Revenue is {tot_revenue}\n\n')
        # print(f"Your total Revenue is {tot_revenue}")

        # print("____________________________________________")

        print("Now calculate Cost of sales")

        starting_stock = float(input("Enter your Starting Stock: "))
        purchase = float(input("Enter your purchase cost: "))
        end_stock = float(input("Enter your End stock: "))

        cos = (starting_stock + purchase) - end_stock
        # print(f"your total cost of  sell is {cos}.")
        f.write(f'Cost of sales {cos}\n\n')

        gross_profit = (tot_revenue - cos)
        print(f"Your Gross Profit is {gross_profit}")
        f.write(f'Gross profit is {gross_profit}\n\n')

        # expenses list........................
        dist_exp_list = []
        admin_exp_list = []
        other_exp_list = []
        fin_exp_list = []
        # total expenses variables.............
        total_dist_exp = 0
        total_admin_exp = 0
        total_other_exp = 0
        total_fin_exp = 0

        f.write("\nDistribution Expenses\n\n")
        c = int(input("How many distribution Expenses do you have:"))
        for i in range(c):
            dis_nm = input(f'Enter {i + 1} distribution expense name:')
            dis_vl = float(input(f'Enter {i + 1} distribution expense value:'))
            dist_exp_list.append(dis_vl)
            total_dist_exp = total_dist_exp + dis_vl
            f.write(f'{dis_nm}\t-{dis_vl}\n ')

        f.write("\nAdministrative Expenses\n\n")
        c = int(input("How many Administrative Expenses do you have:"))
        for i in range(c):
            adm_nm = input(f'Enter {i + 1} Administation expense name:')
            adm_vl = float(input(f'Enter {i + 1} Administration expense:'))
            admin_exp_list.append(adm_vl)
            total_admin_exp = total_admin_exp + adm_vl
            f.write(f'{adm_nm}\t-{adm_vl}\n ')

        f.write("\nOther Expenses\n\n")
        c = int(input("How many Other expenses do you have:"))
        for i in range(c):
            oth_nm = input(f'Enter {i + 1} other expense name:')
            oth_vl = float(input(f'Enter {i + 1} other expense:'))
            other_exp_list.append(oth_vl)
            total_other_exp = total_other_exp + oth_vl
            f.write(f'{oth_nm}\t-{oth_vl}\n ')

        f.write("\nFinance Expenses\n\n")
        c = int(input("How many Finance Expenses do you have:"))
        for i in range(c):
            fin_nm = input(f'Enter {i + 1} Finance expense name:')
            fin_vl = float(input(f'Enter {i + 1} Finance expense:'))
            fin_exp_list.append(fin_vl)
            total_fin_exp = total_fin_exp + fin_vl
            f.write(f'{fin_nm}\t-{fin_vl}\n ')

        total_cost = total_dist_exp + total_admin_exp + total_other_exp + total_fin_exp
        print(f'Total of expenses for this year is {total_cost}')
        f.write(f'Total of expenses for this year is {total_cost}')
        net_profit = gross_profit-total_cost
        print("Net profit for the year : ",net_profit)
        f.write(f'\nNet profit for the year : {net_profit}\n')


#calculating the profit percentage for the year

        profit_percentage = (net_profit / tot_revenue) * 100
        print(f'Your profit percentage for this year is {profit_percentage}% ')
        f.write(f'\nYour profit percentage for this year is {profit_percentage}% \n')


#advicing
        def ratio(x):
            calculation = (x / total_cost) * 100
            return calculation

        def advice(y):
            if y > 25 :
                print(f'your expenses are {y}% .It takes more portion of the total cost. Reduce it!!!!')
            else:
                print("expenses are normal")


        if profit_percentage >= 50 :
            print("your revenue is good. try to enhance your business operations.")
        else:
            distribution_ratio = ratio(total_dist_exp)
            administration_ratio = ratio(total_admin_exp)
            finance_ratio = ratio(total_fin_exp)
            other_ratio = ratio(total_other_exp)

            print("1.distribution expenses\n2.administration expenses\n3.finance expenses\n4.other expenses")
            user_choice = "yes"
            while user_choice == "yes":
                u_input = input("name an expense you want to check: ")
                if u_input == "1":
                    advice(distribution_ratio)
                elif u_input == "2":
                    advice(administration_ratio)
                elif u_input == "3":
                    advice(finance_ratio)
                else:
                    advice(other_ratio)
                user_choice = input("do you need any other advices? ")


        f.close()


    else:
        print("incorrect password.")
        exit()
