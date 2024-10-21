print("""Loan calculator
      
      1000$ over 10 years at 5% APR
      """)
principale = 1000
year = 10
rate = 0.05
total_interest = 0
new_principale= principale
for year in range(1, 11):
    interest = new_principale * rate
    principale+=interest
    total_interest+=interest
    print(year, principale, total_interest)
