Like many before me, I\'ll endeavor to gain some intuitive 
understanding of the Black-Scholes valuation formula. I'll be using the formulation from the original ['73 paper](https://www.jstor.org/stable/1831029?origin=JSTOR-pdf).

### $$ d_1 = {\ln{(\frac{x}{c})} + (r + \frac{1}{2}v^2)(t^* - t) \over v \sqrt{t^* - t}} $$

### $$ d_2 = {\ln{(\frac{x}{c})} + (r - \frac{1}{2}v^2)(t^* - t) \over v \sqrt{t^* - t}} $$

### $$ w(x,t) = xN(d_1) - ce^{r(t-t^*)}N(d_2) $$

### $$ u(x,t) = -xN(-d_1) + ce^{-rt^*}N(-d_2) $$

Where:
- x = spot price
- c = strike price
- r = risk free interest rate
- v = volatility (the standard deviation of the distribution of annualized stock returns)
- $$ t^* $$ = maturity time of the option
- t = time
- N(d) = the cumulative normal density function

As with all models, it's important to remind myself of the basic assumptions and limitations of the formula:
- :green[***Short-term interest rates are known and constant through time.***]
  - Ironically, as I write the yield-curve is inverted, so I believe this one might not always play out.
- :green[***The stock price follows a random walk in continuous time with a variance rate proportional to the square of the stock price.***]
  - Seems as though this may be truer the shorter term you're looking at. BRK certainly hasn't been on a random walk, but maybe in the short term it trades in this manner. 
  - Additionally, it seems like the "continuous" assumption breaks down when thinking about daily trading periods. Maybe some overnight news gaps the underlying. I think its worth looking into the implications of these types of moves in future research.
- :green[***Thus, the distribution of possible stock prices at the end of any finite interval is log-normal.***]
  - This feels intuitive. The payoff structure of the shares inherently is infinite on the upside, but limited to one's cost basis on the downside.
- :green[***The variance of the return on the stock is constant.***]
  - This strikes me as a potential trap. In calm markets it seems like this would play out, but I believe the volatility will increase in times of panic.
- :green[***The stock pays no dividends or other distribution.***]
  - This could be viable depending on the underlying. I'm sure more recent models can account for other cashflows.
- :green[***The option is European.***]
  - One could restrict themselves to European options. However, Americans are more typical and I know that the increased optionality in exercise date makes modeling price more complex. I'd like to research more recent models that account for American options.  
- :green[***There are no transaction costs in buying or selling the stock or the option.***]
  - This is clearly not applicable in real markets.
- :green[***It is possible to borrow any fraction of the price of a security to buy or hold it at the short-term interest rate.***]
  - It seems to me that this is a reasonable approximation for short periods and smaller quantities.
- :green[***There are no penalties to short selling and shorts may be settled in cash.***]
  - This is clearly not always applicable, but seems a reasonable approximation unless Porsche or Reddit starts buying up your underlying. 

All in all, while the assumptions of the formulation might not hold up in every market, it seems to remain a very insightful model for the behavior and sensitivities of options.

Next I'll implement the formula in a simple class, and build a basic fair-price calculator.
