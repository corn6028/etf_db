import db

## Part of ETF
## Period: 2011/7/4 Mon. ~ 2016/9/5 Mon. [3000~4350]
## ETF: 434 (in valid_etf.txt)
## numpy array shape: (6,434,1351)
etf_ndarr = db.get_etf_ndarr()

## All the ETF
## Period: 2000/1/3 Mon. ~ 2020/12/31 Thu. [0~5478]
## ETF: 846
## numpy array shape: (6,846,5479)
etf_all_ndarr = db.get_all_etf_ndarr()
