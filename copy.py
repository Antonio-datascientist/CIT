def collect_personal_information():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    id_number = input("Enter your ID number: ")
    date_of_birth = input("Enter your date of birth: ")
    profession = input("Enter your profession/career: ")
    marital_status = input("Enter your marital status: ")
    email_address = input("Enter your email address: ")

    print("\nClient Information")
    print("Full Name:", full_name)
    print("Phone Number:", phone_number)
    print("ID Number:", id_number)
    print("Date of Birth:", date_of_birth)
    print("Profession:", profession)
    print("Marital Status:", marital_status)
    print("Email Address:", email_address)

    return {
        "full_name": full_name,
        "phone_number": phone_number,
        "id_number": id_number,
        "date_of_birth": date_of_birth,
        "profession": profession,
        "marital_status": marital_status,
        "email_address": email_address,
    }

def assess_loan():
    employment_status = input("What is your employment status? ").strip().lower()

    if employment_status != "employed":
        print("rejected")
        return

    print("accepted")

    monthly_income = float(input("What's your monthly income? "))
    existing_loan = float(input("What is your current existing loan amount? "))

    if monthly_income <= 0:
        print("Invalid monthly income")
        return

    debt_income_ratio = existing_loan / monthly_income
    print(f"Debt-to-income ratio: {debt_income_ratio:.2f}")

    if debt_income_ratio < 0.30:
        print("approve")
        
    elif debt_income_ratio <= 0.50:
        print("Request more information")
        has_other_income = input("Do you have any other source of income? ").strip().lower()

        if has_other_income == "yes":
            total_income = float(input("Total amount you receive from it? "))

            if total_income < existing_loan:
                print("rejected")
            elif total_income >= existing_loan:
                print("accepted")
            else:
                print("rejected")
        else:
            print("rejected")
    else:
        print("rejected")

assess_loan()