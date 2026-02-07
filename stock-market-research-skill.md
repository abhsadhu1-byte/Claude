# Stock Market Research Skill

A comprehensive reference for stock market research, analysis, and investing decisions. Use this as a structured knowledge base to evaluate stocks, understand market dynamics, and make informed investment decisions.

---

## Table of Contents

1. [Reading Financial Statements](#1-reading-financial-statements)
2. [Fundamental Analysis & Valuation](#2-fundamental-analysis--valuation)
3. [Key Financial Ratios & Stock Screening](#3-key-financial-ratios--stock-screening)
4. [Technical Analysis — Indicators](#4-technical-analysis--indicators)
5. [Technical Analysis — Chart Patterns](#5-technical-analysis--chart-patterns)
6. [Market Sentiment Indicators](#6-market-sentiment-indicators)
7. [Sector Rotation & the Business Cycle](#7-sector-rotation--the-business-cycle)
8. [Risk Management & Position Sizing](#8-risk-management--position-sizing)
9. [Portfolio Diversification](#9-portfolio-diversification)
10. [Order Types & Trade Execution](#10-order-types--trade-execution)
11. [Stock Research Workflow (Step-by-Step)](#11-stock-research-workflow-step-by-step)
12. [Checklists & Quick References](#12-checklists--quick-references)
13. [Recommended Resources](#13-recommended-resources)

---

## 1. Reading Financial Statements

Every publicly traded company releases quarterly financial statements. Three core statements form the foundation of stock analysis.

### 1.1 Income Statement (Profit & Loss)

Shows revenue earned and expenses incurred over a period.

| Line Item | What It Tells You |
|---|---|
| **Revenue (Top Line)** | Total sales — is it growing year-over-year? |
| **Cost of Goods Sold (COGS)** | Direct costs to produce goods/services |
| **Gross Profit** | Revenue minus COGS — measures production efficiency |
| **Operating Expenses (SG&A, R&D)** | Overhead costs to run the business |
| **Operating Income (EBIT)** | Profit from core business operations |
| **Net Income (Bottom Line)** | Final profit after all expenses, taxes, interest |
| **Earnings Per Share (EPS)** | Net income / shares outstanding — the most watched metric |

**What to look for:**
- Consistent revenue growth over multiple quarters/years
- Expanding or stable gross margins (not shrinking)
- Operating income growing faster than revenue (operating leverage)
- EPS growth trend — the primary driver of stock price over time

### 1.2 Balance Sheet

A snapshot of what the company owns and owes at a specific point in time.

**The equation:** Assets = Liabilities + Shareholders' Equity

| Section | Key Items | What to Watch |
|---|---|---|
| **Current Assets** | Cash, receivables, inventory | Liquidity — can it pay short-term bills? |
| **Non-Current Assets** | Property, equipment, intangibles | Long-term productive capacity |
| **Current Liabilities** | Accounts payable, short-term debt | Near-term obligations |
| **Long-Term Liabilities** | Long-term debt, lease obligations | Financial leverage and risk |
| **Shareholders' Equity** | Retained earnings, share capital | Book value of the company |

**What to look for:**
- Current ratio (current assets / current liabilities) > 1.5
- Debt-to-equity ratio appropriate for the industry
- Growing retained earnings (company reinvesting profitably)
- Goodwill not excessively large relative to total assets

### 1.3 Cash Flow Statement

Shows actual cash moving in and out. Harder to manipulate than earnings.

| Section | Meaning |
|---|---|
| **Operating Cash Flow (OCF)** | Cash generated from the core business |
| **Investing Cash Flow** | Cash spent on assets, acquisitions, or received from divestitures |
| **Financing Cash Flow** | Cash from issuing debt/equity or paying dividends/buybacks |
| **Free Cash Flow (FCF)** | OCF minus capital expenditures — cash available for shareholders |

**What to look for:**
- Positive and growing operating cash flow
- Free Cash Flow positive and tracking with (or exceeding) net income
- Capital expenditures reasonable relative to revenue
- Not relying on debt/equity issuance to fund operations

### 1.4 How They Connect

- Net income from the income statement flows into retained earnings on the balance sheet
- Cash flow statement reconciles the difference between reported earnings and actual cash
- A company can report profits but have negative cash flow (watch for this)
- Combined analysis of all three prevents missing red flags

**Where to find them:** Company investor relations pages, SEC EDGAR (10-K annual, 10-Q quarterly), brokerage platforms.

---

## 2. Fundamental Analysis & Valuation

Fundamental analysis evaluates a stock's intrinsic value by examining the underlying business, its financials, and the broader economy.

### 2.1 Top-Down vs. Bottom-Up

| Approach | Method |
|---|---|
| **Top-Down** | Economy → Sector → Industry → Company |
| **Bottom-Up** | Start with the company, work outward |

Most thorough analysis combines both.

### 2.2 Valuation Methods

#### Discounted Cash Flow (DCF)

The theoretical gold standard — values a company based on the present value of its future cash flows.

```
Intrinsic Value = Sum of [ FCF_t / (1 + r)^t ] + Terminal Value / (1 + r)^n

Where:
  FCF_t  = Free cash flow in year t
  r      = Discount rate (weighted average cost of capital)
  n      = Projection period (typically 5-10 years)
```

**Strengths:** Theoretically sound, focuses on fundamentals
**Weaknesses:** Highly sensitive to assumptions — small changes in growth rate or discount rate produce large swings in valuation

**Reverse DCF trick:** Instead of estimating fair value, ask: "What growth rate does the current stock price imply?" If the implied growth seems unrealistic, the stock may be mispriced.

**Best for:** Companies with predictable cash flows (utilities, consumer staples, mature tech)
**Challenging for:** Cyclical businesses, early-stage companies with no earnings

#### Relative Valuation (Multiples)

Compare a stock's valuation ratios against peers, industry averages, or its own history.

| Multiple | Formula | When to Use |
|---|---|---|
| **P/E** | Price / Earnings per share | Most common; works for profitable companies |
| **Forward P/E** | Price / Expected next-year EPS | Better for growing companies |
| **PEG** | P/E / Earnings growth rate | Adjusts P/E for growth; PEG < 1 = potentially undervalued |
| **P/S** | Price / Revenue per share | Useful when earnings are negative |
| **P/B** | Price / Book value per share | Asset-heavy industries (banks, real estate) |
| **P/CF** | Price / Cash flow per share | Harder to manipulate than P/E |
| **EV/EBITDA** | Enterprise value / EBITDA | Capital-structure-neutral; preferred for telecom, energy, materials |

**Rules of thumb:**
- Always compare within the same industry — a 30 P/E is cheap for high-growth SaaS, expensive for a utility
- Use forward multiples rather than trailing when future expectations differ significantly from the past
- P/E is preferred in 20 of 25 GICS industry groups; EV/EBITDA favored in telecom, energy, and materials
- Multiple models work best in combination, not isolation

#### Dividend Discount Model (DDM)

For stable dividend-paying companies:

```
Intrinsic Value = D1 / (r - g)

Where:
  D1 = Expected dividend next year
  r  = Required rate of return
  g  = Dividend growth rate
```

Best for mature companies with long dividend track records (utilities, REITs, consumer staples).

### 2.3 Moat Analysis (Competitive Advantages)

Lasting competitive advantages protect earnings and justify premium valuations:

| Moat Type | Description | Examples |
|---|---|---|
| **Network Effects** | Product becomes more valuable as more people use it | Visa, Meta, Microsoft |
| **Switching Costs** | Expensive or painful for customers to switch | Enterprise software (SAP, Oracle) |
| **Cost Advantages** | Can produce at lower cost than competitors | Walmart, Costco |
| **Intangible Assets** | Brands, patents, regulatory licenses | Coca-Cola, pharma patents |
| **Efficient Scale** | Market is only big enough for a few profitable players | Railroads, utilities |

---

## 3. Key Financial Ratios & Stock Screening

### 3.1 Profitability Ratios

| Ratio | Formula | Good Benchmark | What It Shows |
|---|---|---|---|
| **ROE** | Net Income / Shareholders' Equity | > 15% | How well the company uses equity capital |
| **ROA** | Net Income / Total Assets | > 5% | Efficiency of asset utilization |
| **ROIC** | NOPAT / Invested Capital | > 10% (above WACC) | Best all-around capital efficiency metric |
| **Gross Margin** | Gross Profit / Revenue | Industry-dependent | Pricing power and cost control |
| **Operating Margin** | Operating Income / Revenue | > Industry median | Operational efficiency |
| **Net Margin** | Net Income / Revenue | > Industry median | Overall profitability |

**Key insight:** ROE can be inflated by high debt — always check ROA alongside it. Large gaps between ROE and ROA signal high leverage. ROIC is the best single metric because it reflects all investors, not just equity holders.

### 3.2 Financial Health Ratios

| Ratio | Formula | Warning Level | What It Shows |
|---|---|---|---|
| **Debt-to-Equity** | Total Debt / Shareholders' Equity | > 2.0 (varies by industry) | Leverage level |
| **Debt-to-Capital** | Total Debt / Total Capital | > 40% warrants closer look | Proportion of debt funding |
| **Current Ratio** | Current Assets / Current Liabilities | < 1.0 is risky | Short-term liquidity |
| **Quick Ratio** | (Current Assets - Inventory) / Current Liabilities | < 0.8 is risky | Liquidity excluding inventory |
| **Interest Coverage** | EBIT / Interest Expense | < 3.0 is risky | Ability to service debt |

### 3.3 Cash Flow Quality Ratios

| Ratio | Formula | Target | What It Shows |
|---|---|---|---|
| **Cash Conversion** | OCF / Net Income | Close to 1.0 (100%) | Quality of reported earnings |
| **FCF Yield** | FCF / Market Cap | > 5% | Cash return relative to price |
| **Capex-to-Revenue** | Capital Expenditures / Revenue | Industry-dependent | Reinvestment requirements |

### 3.4 Building a Quality Stock Screen

**Minimum quality filters (to avoid value traps):**

1. ROE > 15% consistently for 5 years
2. Debt-to-equity below industry median
3. Positive free cash flow for 3+ consecutive years
4. Revenue growth exceeding industry median
5. Cash conversion ratio close to 1.0
6. No major accounting red flags (growing receivables faster than revenue)

**Layering in valuation:**

7. Forward P/E below industry median, or PEG < 1.5
8. EV/EBITDA below sector average
9. FCF yield above 4%

**Screening tools:** Finviz (free, quick filtering), Stock Rover (premium, deep analysis), FAST Graphs (valuation visualization), GuruFocus (guru-style screens), Simply Wall St (visual reports).

---

## 4. Technical Analysis — Indicators

Technical analysis uses price, volume, and mathematical indicators to identify trends and timing.

### 4.1 Moving Averages (MA)

Smooth price data to reveal the underlying trend.

| Type | Calculation | Common Periods | Use |
|---|---|---|---|
| **SMA** | Simple average of closing prices | 20, 50, 100, 200 | Trend identification |
| **EMA** | Weighted toward recent prices | 9, 12, 26, 50 | Faster trend response |

**Key signals:**
- **Golden Cross:** 50-day MA crosses above 200-day MA → bullish
- **Death Cross:** 50-day MA crosses below 200-day MA → bearish
- Price above 200-day SMA → long-term uptrend; below → downtrend
- Moving averages act as dynamic support and resistance levels

### 4.2 RSI (Relative Strength Index)

Measures momentum on a 0-100 scale. Default period: 14.

| Reading | Interpretation |
|---|---|
| **> 70** | Overbought — potential pullback or consolidation |
| **30-70** | Neutral zone |
| **< 30** | Oversold — potential bounce or reversal |

**Advanced usage:**
- **Bullish divergence:** Price makes lower low, RSI makes higher low → potential reversal up
- **Bearish divergence:** Price makes higher high, RSI makes lower high → potential reversal down
- In strong trends, RSI can stay overbought/oversold for extended periods — don't use RSI alone

### 4.3 MACD (Moving Average Convergence Divergence)

Trend-following momentum indicator.

```
MACD Line    = 12-period EMA - 26-period EMA
Signal Line  = 9-period EMA of MACD Line
Histogram    = MACD Line - Signal Line
```

**Signals:**
- MACD crosses above signal line → bullish
- MACD crosses below signal line → bearish
- Histogram expanding → momentum strengthening
- Histogram contracting → momentum weakening
- Divergence between MACD and price → potential trend reversal

**Alternative settings:** Linda Raschke's 3-10-16 settings detect trend changes 5-10 candles earlier than standard 12-26-9.

### 4.4 Bollinger Bands

Three bands based on a 20-period SMA and 2 standard deviations.

```
Upper Band  = 20-SMA + (2 x Standard Deviation)
Middle Band = 20-SMA
Lower Band  = 20-SMA - (2 x Standard Deviation)
```

**Interpretation:**
- Price touching upper band → potentially overbought
- Price touching lower band → potentially oversold
- Bands narrowing (squeeze) → low volatility, breakout likely
- Bands widening → high volatility, trend in motion
- Price closing outside bands → continuation in that direction (not automatic reversal)

### 4.5 Volume

Volume confirms or denies price movements.

| Scenario | Interpretation |
|---|---|
| Price up + high volume | Strong buying — trend likely to continue |
| Price up + low volume | Weak rally — may not sustain |
| Price down + high volume | Strong selling — trend likely to continue |
| Price down + low volume | Weak decline — may reverse |
| High volume at support/resistance | Significance of the level confirmed |

**On Balance Volume (OBV):** Cumulative volume indicator — rising OBV with rising price confirms trend; divergence warns of reversal.

### 4.6 Combining Indicators for Confirmation

No single indicator is reliable alone. Use multiple confirmation:

| Signal | Strong Confirmation |
|---|---|
| Buy | Price above 200 SMA + RSI crossing above 30 + MACD bullish crossover + volume surge |
| Sell | Price below 200 SMA + RSI crossing below 70 + MACD bearish crossover + high volume breakdown |
| Overbought | Upper Bollinger Band touch + RSI > 70 + MACD bearish divergence |
| Oversold | Lower Bollinger Band touch + RSI < 30 + MACD bullish divergence |

**Rule:** Wait for simultaneous signals across 2-3 indicators before acting.

---

## 5. Technical Analysis — Chart Patterns

Chart patterns reflect market psychology and help predict future price direction.

### 5.1 Reversal Patterns

These signal that the current trend is likely to reverse.

#### Head and Shoulders (Bearish Reversal)

```
     Head
    /    \
   /      \
  / Left   \ Right
 / Shoulder \ Shoulder
/            \
------Neckline------
```

- Three peaks: left shoulder, head (highest), right shoulder
- Break below neckline with volume confirms the pattern
- Price target = distance from head to neckline, projected below neckline
- **Inverse Head and Shoulders** = bullish reversal (same pattern flipped)

#### Double Top (Bearish) / Double Bottom (Bullish)

- **Double Top (M-shape):** Two peaks at similar levels → break below support → bearish
- **Double Bottom (W-shape):** Two troughs at similar levels → break above resistance → bullish
- Second peak/trough typically has lower volume than the first
- Price target = height of the pattern projected from breakout point

#### Rounding Bottom (Saucer)

Gradual transition from downtrend to uptrend over weeks/months. Signals slow sentiment shift.

### 5.2 Continuation Patterns

These signal the trend will resume after a pause.

#### Flags and Pennants

- **Flag:** Small rectangular consolidation against the trend (parallel lines)
- **Pennant:** Small symmetrical triangle after a sharp move
- Both resolve in the direction of the prior trend
- Duration: typically 1-3 weeks

#### Triangle Patterns

| Type | Shape | Bias | Success Rate |
|---|---|---|---|
| **Ascending** | Flat top, rising bottom | Bullish | ~75% |
| **Descending** | Falling top, flat bottom | Bearish | ~75% |
| **Symmetrical** | Converging lines | Direction of prior trend | ~70% |

- Volume decreases as the triangle forms
- Breakout typically occurs between 50-75% of the distance from base to apex
- Volume should increase significantly on breakout

#### Wedge Patterns

| Type | Direction | Signal |
|---|---|---|
| **Rising Wedge** | Converging upward | Bearish reversal |
| **Falling Wedge** | Converging downward | Bullish reversal |

### 5.3 Cup and Handle (Bullish)

```
  Left        Right
  Rim  \_____/  Rim
         Cup       \__/ Handle
                   Breakout →
```

- Rounded bottom (cup) followed by small pullback (handle)
- Bullish breakout above the rim level
- Cup depth ideally 12-33% of prior advance
- Handle should retrace < 50% of cup depth

### 5.4 Candlestick Patterns

Single or multi-candle patterns that signal momentum shifts.

**Bullish Reversal Candles:**
- **Hammer:** Small body at top, long lower wick — buyers rejected lower prices
- **Bullish Engulfing:** Large green candle fully engulfs prior red candle
- **Morning Star:** Three-candle pattern — large red, small body, large green

**Bearish Reversal Candles:**
- **Shooting Star:** Small body at bottom, long upper wick — sellers rejected higher prices
- **Bearish Engulfing:** Large red candle fully engulfs prior green candle
- **Evening Star:** Three-candle pattern — large green, small body, large red

**Indecision:**
- **Doji:** Opening and closing price nearly equal — market indecision, potential reversal

### 5.5 Pattern Reliability

- Chart patterns work across all timeframes, but daily/weekly charts produce 15-20% higher accuracy than hourly charts
- Research shows 60-70% accuracy when combined with volume and indicator confirmation
- No pattern is infallible — always use stop losses
- Higher volume on breakout = higher probability of follow-through

---

## 6. Market Sentiment Indicators

Sentiment indicators measure the overall mood of market participants and help identify extremes.

### 6.1 VIX (CBOE Volatility Index)

The "fear gauge" — measures expected 30-day volatility derived from S&P 500 options.

| VIX Level | Interpretation |
|---|---|
| **< 15** | Low fear / complacency — markets calm (potential for complacency) |
| **15-20** | Normal range |
| **20-30** | Elevated fear — increased uncertainty |
| **> 30** | High fear / panic — historically marks bottoms (contrarian buy signal) |
| **> 40** | Extreme panic — rare events (2008, 2020) |

**Usage:** VIX spikes often mark market bottoms. However, context matters — pandemic volatility differs from financial crisis volatility.

### 6.2 CNN Fear & Greed Index

Composite of seven indicators scored 0-100:

1. Market momentum (S&P 500 vs. 125-day MA)
2. Stock price strength (52-week highs vs. lows)
3. Stock price breadth (advancing vs. declining volume)
4. Put/Call ratio
5. Junk bond demand (yield spread vs. investment grade)
6. Market volatility (VIX)
7. Safe haven demand (stocks vs. bonds performance)

| Score | Sentiment | Contrarian Signal |
|---|---|---|
| **0-25** | Extreme Fear | Potential buying opportunity |
| **25-45** | Fear | Market pessimistic |
| **45-55** | Neutral | No strong bias |
| **55-75** | Greed | Market optimistic |
| **75-100** | Extreme Greed | Potential selling/caution signal |

### 6.3 Put/Call Ratio

| Ratio | Meaning |
|---|---|
| **> 1.0** | More puts (bearish bets) than calls — bearish sentiment |
| **< 0.7** | More calls (bullish bets) than puts — bullish sentiment |
| **Extreme readings** | Contrarian signal — extreme fear often precedes rallies |

### 6.4 Market Breadth (Advance-Decline Line)

- Tracks cumulative difference between advancing and declining stocks
- Healthy rally: A/D line rises with the index
- **Bearish divergence:** Index makes new high but A/D line doesn't → rally driven by few stocks, potential weakness ahead
- **Bullish divergence:** Index makes new low but A/D line holds → broad market holding up, potential bottom

### 6.5 Other Sentiment Measures

- **AAII Sentiment Survey:** Weekly poll of individual investors (bullish/bearish/neutral)
- **Insider buying/selling:** Clustered insider buying is bullish; selling is ambiguous (insiders sell for many reasons)
- **Short interest:** High short interest can fuel short squeezes
- **Fund flows:** Money flowing into equity funds vs. bond funds

---

## 7. Sector Rotation & the Business Cycle

Different market sectors outperform at different phases of the economic cycle.

### 7.1 The Business Cycle Phases

```
                Peak
               /    \
              /      \
  Expansion  /        \  Contraction
            /          \
           /            \
  Trough ---              --- Trough
  (Recovery)              (Recession)
```

### 7.2 Sector Performance by Phase

| Phase | Economy | Leading Sectors | Lagging Sectors |
|---|---|---|---|
| **Early Cycle (Recovery)** | GDP accelerating, rates low, credit expanding | Technology, Consumer Discretionary, Financials, Industrials | Utilities, Consumer Staples, Healthcare |
| **Mid Cycle (Expansion)** | Steady growth, moderate inflation | Technology, Industrials, Materials | Utilities |
| **Late Cycle (Peak)** | Growth slowing, inflation rising, rates high | Energy, Materials, Healthcare | Technology, Consumer Discretionary |
| **Recession (Contraction)** | GDP declining, rates falling | Utilities, Consumer Staples, Healthcare | Technology, Financials, Consumer Discretionary |

### 7.3 The 11 GICS Sectors

1. **Information Technology** — software, hardware, semiconductors
2. **Healthcare** — pharma, biotech, medical devices, insurers
3. **Financials** — banks, insurance, asset management
4. **Consumer Discretionary** — retail, autos, housing, entertainment
5. **Consumer Staples** — food, beverages, household products
6. **Energy** — oil & gas, renewable energy
7. **Industrials** — aerospace, defense, machinery, transportation
8. **Materials** — chemicals, metals, mining, packaging
9. **Real Estate** — REITs, property development
10. **Communication Services** — telecom, media, interactive media
11. **Utilities** — electric, gas, water utilities

### 7.4 Sector Rotation Signals

- **Relative Strength Analysis:** Compare sector ETF performance vs. S&P 500 — outperformance signals rotation into that sector
- **Yield Curve:** Steepening favors financials; flattening/inverting favors defensives
- **Interest Rates:** Rising rates hurt utilities/REITs, help financials; falling rates do the opposite
- **Commodity Prices:** Rising commodities favor energy/materials; falling favors consumers

### 7.5 Key Sector ETFs for Tracking

| Sector | SPDR ETF | Vanguard ETF |
|---|---|---|
| Technology | XLK | VGT |
| Healthcare | XLV | VHT |
| Financials | XLF | VFH |
| Consumer Disc. | XLY | VCR |
| Consumer Staples | XLP | VDC |
| Energy | XLE | VDE |
| Industrials | XLI | VIS |
| Materials | XLB | VAW |
| Real Estate | XLRE | VNQ |
| Communication | XLC | VOX |
| Utilities | XLU | VPU |

---

## 8. Risk Management & Position Sizing

Capital preservation is the foundation of long-term investing success.

### 8.1 Core Risk Management Principles

1. **Never risk more than you can afford to lose** on any single position
2. **Diversify** across sectors, asset classes, and geographies
3. **Use stop losses** to limit downside on every trade
4. **Size positions** based on risk, not conviction alone
5. **Have an exit plan** before entering any trade

### 8.2 Position Sizing Methods

#### The 2% Rule

Never risk more than 2% of total portfolio on a single trade.

```
Position Size = (Portfolio Value x 0.02) / (Entry Price - Stop Loss Price)

Example:
  Portfolio: $100,000
  Max risk per trade: $2,000 (2%)
  Stock price: $50
  Stop loss: $45 (10% below entry)
  Risk per share: $5
  Position size: $2,000 / $5 = 400 shares ($20,000 position)
```

#### Fixed Fractional Method

Risk a fixed percentage of current portfolio value on each trade. Position size automatically scales down after losses and up after gains.

#### Volatility-Based Sizing

Use ATR (Average True Range) to adjust position size:

```
Position Size = (Risk Amount) / (N x ATR)

Where N = multiplier (e.g., 2x ATR for stop distance)
```

More volatile stocks get smaller positions; less volatile stocks get larger positions.

#### Kelly Criterion

Calculates the theoretically optimal bet size:

```
Kelly % = W - [(1 - W) / R]

Where:
  W = Win probability
  R = Win/loss ratio (average win / average loss)
```

Most practitioners use "half Kelly" to reduce volatility.

#### Risk Parity

Allocate capital so that each position contributes equally to total portfolio risk, rather than equal dollar amounts.

### 8.3 Stop Loss Strategies

| Type | Method | Best For |
|---|---|---|
| **Fixed percentage** | Stop at X% below entry (e.g., 7-10%) | Simple, consistent |
| **Support-based** | Stop just below key support level | Technically informed |
| **ATR-based** | Stop at 2x ATR below entry | Adjusts to volatility |
| **Trailing stop** | Moves up with price by fixed amount/% | Locking in profits |
| **Time-based** | Exit if trade hasn't worked in X days | Avoiding dead money |

### 8.4 Risk/Reward Ratio

Only take trades where potential reward significantly exceeds risk:

| Ratio | Meaning | Implication |
|---|---|---|
| **1:1** | Risk $1 to make $1 | Need > 50% win rate to profit |
| **1:2** | Risk $1 to make $2 | Need > 33% win rate to profit |
| **1:3** | Risk $1 to make $3 | Need > 25% win rate to profit |

**Target minimum:** 1:2 risk/reward on every trade.

---

## 9. Portfolio Diversification

### 9.1 Asset Allocation Models

| Model | Stocks | Bonds | Other | Risk Level |
|---|---|---|---|---|
| **Aggressive** | 80-100% | 0-20% | 0-10% | High |
| **Growth** | 70-80% | 15-25% | 5-10% | Medium-High |
| **Balanced** | 50-60% | 30-40% | 5-15% | Medium |
| **Conservative** | 30-40% | 50-60% | 5-15% | Low-Medium |
| **Income** | 20-30% | 60-70% | 5-15% | Low |

### 9.2 Diversification Dimensions

| Dimension | Method |
|---|---|
| **Asset class** | Stocks, bonds, commodities, real estate, cash |
| **Geography** | Domestic, international developed, emerging markets |
| **Sector** | Across all 11 GICS sectors |
| **Market cap** | Large-cap, mid-cap, small-cap |
| **Style** | Growth, value, blend |
| **Time** | Dollar-cost averaging over time |

### 9.3 Correlation Matters

- Assets that move independently reduce overall portfolio volatility
- Stocks and bonds are historically low-correlation (but not always)
- International stocks provide diversification but correlations increase in crises
- Commodities and real estate offer non-correlated return streams
- **Goal:** Own assets that don't all decline simultaneously

### 9.4 Rebalancing

- Review allocation quarterly or when any asset class drifts > 5% from target
- Rebalancing forces you to buy low (underperforming assets) and sell high (outperforming ones)
- Tax-loss harvesting during rebalancing can offset gains

---

## 10. Order Types & Trade Execution

### 10.1 Order Types

| Order | Execution | Price Control | Best For |
|---|---|---|---|
| **Market** | Immediate at best available price | None | Speed; highly liquid stocks |
| **Limit** | Only at specified price or better | Yes | Controlling entry/exit price |
| **Stop-Loss** | Becomes market order when trigger hit | None after trigger | Protecting against losses |
| **Stop-Limit** | Becomes limit order when trigger hit | Yes after trigger | Loss protection with price control |
| **Trailing Stop** | Follows price up by set amount/% | None after trigger | Locking in profits dynamically |
| **Bracket** | Entry + take-profit + stop-loss together | Varies | Complete trade management |

### 10.2 Time Conditions

| Condition | Duration |
|---|---|
| **Day** | Expires end of trading day |
| **GTC (Good 'Til Canceled)** | Active until executed or canceled |
| **MOO (Market on Open)** | Executes at market open |
| **MOC (Market on Close)** | Executes at market close |
| **IOC (Immediate or Cancel)** | Fill immediately or cancel unfilled portion |
| **FOK (Fill or Kill)** | Fill entirely immediately or cancel completely |

### 10.3 Execution Best Practices

- Use **limit orders** for less liquid stocks or volatile markets
- Place **stop losses** immediately after entering a position
- Avoid **market orders** during pre-market/after-hours when spreads are wide
- Use **trailing stops** for positions in strong trends
- Consider **bracket orders** for a complete trade plan at entry

---

## 11. Stock Research Workflow (Step-by-Step)

A systematic process for evaluating any stock from discovery to decision.

### Step 1: Idea Generation

- Stock screeners (Finviz, Stock Rover, Trading View)
- Sector rotation analysis (which sectors are in favor?)
- Earnings surprises and momentum scanners
- News catalysts, industry trends, thematic investing
- Insider buying clusters

### Step 2: Business Understanding (10 minutes)

- [ ] What does the company do? (read the 10-K business description)
- [ ] What is its competitive advantage / moat?
- [ ] What industry and sector? Growth or mature?
- [ ] Who are the main competitors?
- [ ] What are the major risks and catalysts?

### Step 3: Financial Analysis (20 minutes)

- [ ] Revenue trend (3-5 years): growing, stable, or declining?
- [ ] Earnings trend and EPS growth rate
- [ ] Margins: gross, operating, net — expanding or contracting?
- [ ] ROE, ROA, ROIC — above industry averages?
- [ ] Debt levels: debt-to-equity, interest coverage
- [ ] Cash flow: OCF positive? FCF positive? Cash conversion near 1.0?
- [ ] Balance sheet: current ratio > 1.5? Manageable long-term debt?

### Step 4: Valuation Assessment (10 minutes)

- [ ] Current P/E vs. industry average and own 5-year average
- [ ] Forward P/E and PEG ratio
- [ ] EV/EBITDA vs. peers
- [ ] FCF yield
- [ ] Is the stock trading below, at, or above fair value estimates?

### Step 5: Technical Analysis (5 minutes)

- [ ] What is the overall trend? (above/below 200-day MA)
- [ ] Key support and resistance levels
- [ ] RSI: overbought or oversold?
- [ ] MACD: bullish or bearish momentum?
- [ ] Volume: confirming price action?
- [ ] Any chart patterns forming?

### Step 6: Sentiment Check (5 minutes)

- [ ] VIX level and trend
- [ ] Fear & Greed Index reading
- [ ] Analyst consensus and price targets
- [ ] Short interest level
- [ ] Recent insider activity

### Step 7: Decision & Trade Plan

- [ ] **Buy / Hold / Sell / Pass** decision
- [ ] Entry price or zone
- [ ] Position size (using 2% rule or volatility method)
- [ ] Stop loss level
- [ ] Take-profit target(s)
- [ ] Risk/reward ratio (minimum 1:2)
- [ ] Time horizon
- [ ] Thesis invalidation — what would make you exit?

---

## 12. Checklists & Quick References

### 12.1 Red Flags Checklist

Watch out for these warning signs:

- [ ] Revenue declining for 2+ consecutive quarters
- [ ] Accounts receivable growing faster than revenue
- [ ] Cash flow from operations consistently below net income
- [ ] Rising debt with declining earnings
- [ ] Frequent management turnover or insider selling
- [ ] Goodwill larger than 50% of total assets
- [ ] Declining ROE/ROIC over multiple years
- [ ] Audit qualifications or restatements
- [ ] Related-party transactions
- [ ] Aggressive revenue recognition policies

### 12.2 Quality Company Checklist

Signs of a high-quality business:

- [ ] Consistent revenue growth (5+ years)
- [ ] ROE consistently above 15%
- [ ] Positive free cash flow every year
- [ ] Manageable debt levels
- [ ] Wide or expanding margins
- [ ] Strong competitive position / moat
- [ ] Aligned management incentives
- [ ] History of returning cash to shareholders (dividends + buybacks)
- [ ] Growing addressable market
- [ ] Transparent and conservative accounting

### 12.3 Key Formulas Quick Reference

```
P/E Ratio        = Stock Price / Earnings Per Share
PEG Ratio         = P/E / Annual EPS Growth Rate
EV/EBITDA         = (Market Cap + Debt - Cash) / EBITDA
ROE               = Net Income / Shareholders' Equity
ROA               = Net Income / Total Assets
ROIC              = NOPAT / Invested Capital
Current Ratio     = Current Assets / Current Liabilities
Debt-to-Equity    = Total Debt / Shareholders' Equity
Free Cash Flow    = Operating Cash Flow - Capital Expenditures
FCF Yield         = Free Cash Flow / Market Cap
Dividend Yield    = Annual Dividends / Stock Price
RSI               = 100 - [100 / (1 + (Avg Gain / Avg Loss))]
MACD              = 12-EMA - 26-EMA
Bollinger Upper   = 20-SMA + (2 x Std Dev)
Bollinger Lower   = 20-SMA - (2 x Std Dev)
Position Size     = (Portfolio x Risk%) / (Entry - Stop Loss)
Risk/Reward       = (Target - Entry) / (Entry - Stop Loss)
```

---

## 13. Recommended Resources

### Books
- *The Intelligent Investor* — Benjamin Graham (value investing bible)
- *Technical Analysis of the Financial Markets* — John J. Murphy (technical analysis standard)
- *One Up on Wall Street* — Peter Lynch (finding stocks in everyday life)
- *A Random Walk Down Wall Street* — Burton Malkiel (efficient markets perspective)
- *Common Stocks and Uncommon Profits* — Philip Fisher (growth investing)

### Free Tools & Platforms
- **Finviz** — stock screener, heat maps, charts
- **TradingView** — charting and technical analysis
- **Yahoo Finance** — financial statements, news, quotes
- **SEC EDGAR** — official company filings (10-K, 10-Q, 8-K)
- **Macrotrends** — long-term financial data and charts
- **FAST Graphs** — earnings and price visualization
- **StockCharts** — sector rotation, technical analysis

### Data Sources
- **Financial Statements:** SEC EDGAR, company IR pages
- **Economic Data:** FRED (Federal Reserve Economic Data)
- **Sentiment:** CNN Fear & Greed Index, AAII Sentiment Survey
- **Insider Activity:** SEC Form 4 filings, OpenInsider
- **Short Interest:** FINRA short interest data

### YouTube Tutorial Reference
- [Stock Market Research Playlist by abhsadhu1-byte](https://www.youtube.com/playlist?list=PLxNHpNhDaEFJsuzKNrMbr_SESDCCLmSu4) — foundational video course covering market analysis concepts

---

## Disclaimer

This skill document is for **educational purposes only**. It is not financial advice. Stock market investing involves risk, including the potential loss of principal. Always do your own research and consider consulting a qualified financial advisor before making investment decisions. Past performance does not guarantee future results.
