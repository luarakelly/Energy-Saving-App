import numpy as np 
#    Liquidity Ratios:
#        Current Ratio: Current assets divided by current liabilities. It measures a company's ability to meet short-term obligations. A ratio above 1 indicates good short-term liquidity.
#        Quick Ratio (Acid-Test Ratio): (Current Assets - Inventory) divided by current liabilities. This ratio is more conservative because it excludes inventory, which may not be as liquid.

#    Profitability Ratios:
#        Gross Profit Margin: (Gross Profit / Revenue) * 100. It measures the percentage of revenue that exceeds the cost of goods sold.
#        Net Profit Margin: (Net Income / Revenue) * 100. It measures the percentage of revenue that remains as profit after all expenses.

#    Efficiency Ratios:
#        Inventory Turnover: (Cost of Goods Sold / Average Inventory). It measures how many times a company sells and replaces its inventory in a given period.
#        Accounts Receivable Turnover: (Net Sales / Average Accounts Receivable). It indicates how quickly a company collects payments from customers.

#    Debt and Solvency Ratios:
#        Debt to Equity Ratio: Total Debt divided by Shareholder's Equity. It measures the proportion of a company's financing that comes from debt.
#        Interest Coverage Ratio: Earnings Before Interest and Taxes (EBIT) divided by Interest Expense. It assesses a company's ability to cover its interest payments.

#    Market Ratios:
#        Price-to-Earnings (P/E) Ratio: Market price per share divided by Earnings Per Share (EPS). It shows how much investors are willing to pay for each dollar of earnings.
#        Price-to-Sales (P/S) Ratio: Market price per share divided by Revenue per Share. It measures a company's valuation based on its sales.

#    Return on Investment (ROI) Ratios:
#        Return on Assets (ROA): Net Income divided by Total Assets. It indicates a company's ability to generate profit from its assets.
#        Return on Equity (ROE): Net Income divided by Shareholder's Equity. It measures the return to shareholders for their investments.

#    Dividend Ratios:
#        Dividend Yield: Dividend per Share divided by Market Price per Share. It shows the return on investment from dividends.
#        Dividend Payout Ratio: Dividends per Share divided by Earnings Per Share. It indicates the proportion of earnings paid out as dividends.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# general analises that i want to do:
#    Trend Analysis:
#        Numpy can help you create time series arrays and calculate trends, but you may find pandas more suitable for time series analysis.

#    Financial Ratios:
#        You can use numpy to calculate and manipulate arrays of financial data. For example, you can calculate ratios like gross margin or leverage ratios using numpy functions.

#    DuPont Analysis:
#        Numpy can be used in conjunction with pandas to break down ROE into its components by performing element-wise calculations.

#    Valuation Analysis:
#        Numpy can help with calculations for a DCF analysis, but you'll likely use other libraries like scipy for more advanced numerical analysis.

#    Earnings Per Share (EPS) Analysis:
#        Numpy can be used to calculate and manipulate EPS data over time.

#    Risk Metrics:
        You can use numpy to calculate standard deviations or to perform basic statistical calculations. More advanced risk analysis may require other libraries.

    Working Capital Analysis:
        Numpy can help with calculating changes in working capital components, but pandas is often more convenient for working with financial data.

    Market Metrics:
        Numpy can assist with calculations related to market metrics, but you might also use pandas and other libraries for comprehensive market analysis.

    Dividend Growth Analysis:
        You can use numpy for basic dividend growth rate calculations, but pandas is more suitable for time series analysis.

    Segment Performance Analysis:
        You can use numpy for array calculations on segment data, but pandas may be more effective for data manipulation and aggregation.

    Geographic Analysis:
        Numpy can assist in calculations related to geographic analysis, but data manipulation and visualization are often better handled by pandas and other libraries.

    Correlation Analysis:
        Numpy can calculate correlations between variables, but pandas or other statistical libraries can provide more detailed analysis.

    Time Series Analysis:
        Numpy can help with basic time series operations, but more advanced time series analysis is typically done with libraries like pandas and statsmodels.

    Regression Analysis:
        Numpy can be used for matrix operations in linear regression, but libraries like statsmodels or scikit-learn are often better suited for regression analysis.

    Monte Carlo Simulation:
        Numpy can generate random numbers for Monte Carlo simulations, but you'd typically use other libraries to perform the simulations and analyze the results.