import numpy as np

def financial_planning_simulation(
    initial_market_value,
    initial_jewellery_value,
    annual_expenses,
    annual_contribution,
    market_return_mean,
    market_return_std,
    jewellery_return_mean,
    jewellery_return_std,
    inflation_rate,
    income_growth_rate,
    tax_rate,
    liquidity_penalty,
    jewellery_liquidity_penalty,
    liquidation_penalty=0.10,
    years=100,
    num_simulations=1000
):
    ending_values = []
    bankrupt_flags = []

    for _ in range(num_simulations):
        portfolio = initial_market_value
        jewellery = initial_jewellery_value
        expenses = annual_expenses
        contribution = annual_contribution
        bankrupt = False

        for year in range(1, years + 1):

            portfolio += contribution

            market_return = np.random.lognormal(
                np.log(1 + market_return_mean) - 0.5 * market_return_std**2,
                market_return_std
            ) - 1

            jewellery_return = np.random.lognormal(
                np.log(1 + jewellery_return_mean) - 0.5 * jewellery_return_std**2,
                jewellery_return_std
            ) - 1

            gain = portfolio * market_return
            tax = tax_rate * max(gain, 0)
            portfolio += gain - tax

            jewellery *= (1 + jewellery_return)

            portfolio *= (1 - liquidity_penalty)
            jewellery *= (1 - jewellery_liquidity_penalty)

            if portfolio >= expenses:
                portfolio -= expenses
            else:
                shortfall = expenses - portfolio
                if jewellery * (1 - liquidation_penalty) >= shortfall:
                    jewellery -= shortfall / (1 - liquidation_penalty)
                    portfolio = 0
                else:
                    portfolio = 0
                    jewellery = 0
                    bankrupt = True
                    break

            expenses *= (1 + inflation_rate)
            contribution *= (1 + income_growth_rate)

        real_ending = (portfolio + jewellery) / ((1 + inflation_rate) ** years)
        ending_values.append(real_ending)
        bankrupt_flags.append(bankrupt)

    return np.array(ending_values), bankrupt_flags
