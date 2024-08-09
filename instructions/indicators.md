# Technical Indicators

This file contains a total of 8 indicators used in Technical Analysis of Stocks. Each indicator's use, definition, formula, souce of the information etc. are mentioned. These are only some of the indicators, and there exists a lot more. The `pandas-ta` python library is popularly used to calculate the various indicators.  

1. Average Directional Index (ADX)

    * This technical indicator is used to determine the strength of a trend.

    * Formula for the indicator and calculation



        * $$ +DI = \left( \frac{\text{Smoothed } +DM}{\text{ATR}} \right) \times 100 $$

        * $$ -DI = \left( \frac{\text{Smoothed } -DM}{\text{ATR}} \right) \times 100 $$

        * $$DX = \left( \frac{|+DI - (-DI)|}{|+DI + (-DI)|} \right) \times 100$$

        * $$ADX = \frac{\text{(Prior ADX × 13) + Current ADX}}{14}$$

        Where:
        - **+DM (Directional Movement)** = Current High – PH
        - **PH** = Previous High
        - **-DM** = Previous Low – Current Low
        - **Smoothed +/-DM** = \(\sum_{t=1}^{14} DM - \left(\frac{\sum_{t=1}^{14} DM}{14}\right) + CDM\)
        - **CDM** = Current DM
        - **ATR** = Average True Range

    * The trend has "strength" when ADX > 25

    * The trend is "weak" when ADX < 20

    * Source: https://www.investopedia.com/terms/a/adx.asp

2. Aroon Indicator

    * This indicator is used to identify trend changes in the price of an asset and strength of that trend.

    * Aroon line up measures strength of the uptrend.

    * Aroon line down measures strength of downtrend 

    * When Aroon Up is above Aroon Down, it indicates bullish price behaviour.

    * When Aroon Down is above Aroon Up, it indicates bearish price behaviour

    * Crossover of two lines can indicate trend changes.

    * The range of the Aroon Indicator is [0,100]

    * Value close to 100 indicate strong trend.

    * Value close to 0 indicate weak trend. 

    * Formula (For a period of 25 over an asset):

        * $$ \text{Aroon Up} = \frac{25 - \text{Period since 25 period high}}{25} \times 100 $$

        * $$ \text{Aroon Down} = \frac{25 - \text{Period since 25 period low}}{25} \times 100 $$

        * Source: https://www.investopedia.com/terms/a/aroon.asp

3. Choppiness Index 

    * The Choppiness Index tells us whether there's a trend or the market is moving sideways. 

    * The range of Choppiness Index is [0,100]

    * A value closer to 100 indicate higher choppiness (sideways movement)

    * A value closer to 0 indicates a trend. 

    * Formula 

    $$ 100 \times \frac{\log_{10}\left( \sum \text{ATR}(1), n \right)}{\left( \text{MaxHi}(n) - \text{MinLo}(n) \right)} \div \log_{10}(n) $$

    Where

    - **n** = User defined period length.

    - **LOG10(n)** = base10 LOG of n
        
    - **ATR(1)** = Average True Range (Period of 1)

    - **SUM(ATR(1), n)** = Sum of the Average True Range over past n bars 
        
    - **MaxHi(n)** = The highest high over past n bars

    - **MinLo(n)** = The lowest low over past n bars

    * Source: https://in.tradingview.com/support/solutions/43000501980-choppiness-index-chop/


4. Chande Kroll Stop 

    * Chande Kroll Stop can identify stop loss for long or short position. 

    * It has two lines - one for stop level of short position and other for stop level of long position. 

    * Chande Kroll Stop is independent of volatility.

    * It's a sell signal when the price crosses below both lines.

    * It's a buy signal when the price crosses above both lines. 

    * Source: https://www.wallstreetmojo.com/chande-kroll-stop/

5. Detrended Price Oscillator

    * It strips out the price trends in an effort to estimate the length of price cycles from peak to peak or trough to trough

    * Formula: 

        * $$ DPO = \text{Price from} \left(\frac{X}{2} + 1 \text{ periods ago}\right) - X \text{ period SMA} $$

        Where

        - **X** = Number of periods used for the look-back period

        - **SMA** = Simple Moving Average

    * Source: https://www.investopedia.com/terms/d/detrended-price-oscillator-dpo.asp

6. Qstick indicator 

    * Qstick indicator was developed to numerically identify trends on price chart. 

    * Qstick indicator is calculated by taking an 'n' period moving average of difference between open and closing prices.
    
    * Qstick > 0 indicates that majority of last days have been up & buying pressure has been increasing. 

    * Qstick crossing above zero line indicates buy signal. 

    * Qstick crossing below zero line indicates sell signal. 

    * Source: https://www.investopedia.com/terms/q/qstick.asp

7. Balance of Power 

    * This is a momentum indicator. 

    * It measures a price trend by evaluating the strength of buy and sell signals.

    * The range of this indicator is [-1,+1]

    * Values greater than zero indicate stronger buying pressure.

    * Values lower than zero indicate strong selling pressure

    * A value of zero indicates that the strength of buyers and sellers is equalizing. 

    * Formula: 

        * $$ \text{Balance of Power (BOP)} = \text{Moving Average} \left(\frac{\text{Close Price - Open Price}}{\text{High Price - Low Price}}\right) $$ 

    * Source: https://in.tradingview.com/support/solutions/43000589100-balance-of-power-bop/

8. Fisher Transform Indicator 

    * This is a momentum indicator.

    * It converts prices into Gaussian Normal Distribution.

    * Formula:

        * $$ \text{Fisher Transform} = \frac{1}{2} \times ln \left(\frac{1 + X}{ 1 - X} \right) $$

        Where

        - ln = Natural logarithm

        - X = transformation of price between -1 and +1.

    * Source: https://www.investopedia.com/terms/f/fisher-transform.asp









