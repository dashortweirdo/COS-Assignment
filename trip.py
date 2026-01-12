# Name - Osimen Ivie Favour
# Matric No - BU24SEN1039
# Course - COS 201
# Assignment - U.S Federal Personal Income Tax Calculator
# Filing Status:



class IncomeTaxCalculator:
    def __init__(self, income: float, filing_status: int) -> None:
        self.income = float(income)
        self.filing_status = filing_status
        self.brackets = self.get_tax_brackets()

    def get_tax_brackets(self):
        # Define tax brackets based on filing status
        if self.filing_status == 0:  # Single
            return [
                (0, 8350, 0.10),
                (8351, 33950, 0.15),
                (33951, 82250, 0.25),
                (82251, 171550, 0.28),
                (171551, 372950, 0.33),
                (float('inf'), 0.35)
            ]
        elif self.filing_status == 1:  # Married Filing Jointly or Qualified Widower
            return [
                (0, 16700, 0.10),
                (16701, 67900, 0.15),
                (67901, 137050, 0.25),
                (137051, 208850, 0.28),
                (208851, 372950, 0.33),
                (float('inf'), 0.35)
            ]
        elif self.filing_status == 2:  # Married Filing Separately
            return [
                (0, 8350, 0.10),
                (8351, 33950, 0.15),
                (33950, 68525, 0.25),
                (68525, 104425, 0.28),
                (104425, 186475, 0.33),
                (float('inf'), 0.35)
            ]
        elif self.filing_status == 3:  # Head of Household
            return [
                (0, 11950, 0.10),
                (11951, 45500, 0.15),
                (45501, 117450, 0.25),
                (117451, 190200, 0.28),
                (190200, 372950, 0.33),
                (float('inf'), 0.35)
            ]
        else:
            raise ValueError("Unsupported filing status")
        
    def compute_tax(self) -> float:
        tax = 0.0
        prev_limit = 0.0
        for upper, rate in self.brackets:
            if self.income <= prev_limit:
                break
            taxable = min(self.income, upper) - prev_limit
            if taxable > 0:
                tax += taxable * rate
            prev_limit = upper
        return tax
    
if __name__ == "__main__":
    try:
        income = float(input("Enter your gross income: "))
        filing_status = int(input("Enter your filing status (0-3): "))
        calculator = IncomeTaxCalculator(income, filing_status) # type: ignore
        tax = calculator.compute_tax()
        net_income = income - tax
        print(f"Total Tax: {tax:.2f}")
        print(f"Net Income: {net_income:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


        
