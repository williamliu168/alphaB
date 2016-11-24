#ifndef FUNDAMENTALDATAPOINT_H
#define FUNDAMENTALDATAPOINT_H

class FundamentalDataPoint
{
public:
    FundamentalDataPoint();
    ~FundamentalDataPoint();

    void Initialize();


public:
    std::string m_symbol;   // my container should know this, should I know this?
    std::string m_date;     // should be in date format, boost?

    // income statement - primary data
    long int m_revenue;
    long int m_revenueUsd;
    long int m_costOfRevenue;   // like cost of goods sold
    long int m_rnd;             // research and development
    long int m_ebit;            // earning before interest tax
    long int m_ebitUsd;
    long int m_intExp;          // interest expense
    long int m_ebt;
    long int m_taxExp;          // income tax expense
    long int m_netIncome;
    long int m_prefDivis;       // preferred dividends income statement impact
    long int m_netIncomeCs;     // net income common stock
    long int m_netIncomeCsUsd;
    long int m_netIncDiscontinuedOp;    // net income from discontinued operations
    long int m_sharesWa;        // weighted average shares
    long int m_sharesWaDil;     // diluted weighted average shares

    // secondary data   (like margins, basic ratios)
    long int m_grossProfit;
    long int m_eps;             // earning per share
    long int m_epsUsd;
    long int m_epsDil;          // earnings per diluted share
    long int m_dps;             // dividends per basic common share

    // cash flow statement
    long int m_ncfo;
    long int m_depAmort;        // depreciation, amortization & accretion(what is accretion?)
    long int m_ncfi;            // net cash flow from investing
    long int m_capex;           // capital expenditure





}


#endif // FUNDAMENTALDATAPOINT_H
