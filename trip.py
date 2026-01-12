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
                (8350, 0.10),
                (33950, 0.15),
                (82250, 0.25),
                (171550, 0.28),
                (372950, 0.33),
                (float('inf'), 0.35)
            ]
        elif self.filing_status == 1:  # Married Filing Jointly
            return [
                (16700, 0.10),
                (67900, 0.15),
                (137050, 0.25),
                (208850, 0.28),
                (372950, 0.33),
                (float('inf'), 0.35)
            ]
        elif self.filing_status == 2:  # Married Filing Separately
            return [
                (8350, 0.10),
                (33950, 0.15),
                (68525, 0.25),
                (104425, 0.28),
                (186475, 0.33),
                (float('inf'), 0.35)
            ]
        elif self.filing_status == 3:  # Head of Household
            return [
                (11950, 0.10),
                (45500, 0.15),
                (117450, 0.25),
                (190200, 0.28),
                (372950, 0.33),
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

        