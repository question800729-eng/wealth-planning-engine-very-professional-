import numpy as np
from simulator import financial_planning_simulation

if __name__ == "__main__":
    results, bankrupt_flags = financial_planning_simulation(
        initial_market_value=100000,
        initial_jewellery_value=50000,
        annual_expenses=10000,
        annual_contribution=5000,
        market_return_mean=0.07,
        market_return_std=0.15,
        jewellery_return_mean=0.05,
        jewellery_return_std=0.10,
        inflation_rate=0.03,
        income_growth_rate=0.05,
        tax_rate=0.20,
        liquidity_penalty=0.01,
        jewellery_liquidity_penalty=0.02
    )

    print("Mean:", np.mean(results))
    print("Median:", np.median(results))
    print("Survival rate:", (1 - np.mean(bankrupt_flags)) * 100)
