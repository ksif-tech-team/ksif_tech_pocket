# ksif_tech_pocket

### Transaction, Balance Record System for Quant

Pocket 은 Quant 투자 과정에서 거래기록, 잔액을 기록하는 시스템입니다

Pocket 은 다음과 같은 기능을 제공합니다.
* Organize_portfolio
  * 구성해야 할 포트폴리오 정보를 받아 Ordering, Logging을 수행합니다.
    * Organize new portfolio
        1. 백테스팅 시작시
        2. 예산이 추가되는 경우(?)
        3. 복수의 자산운용전략을 종합적으로 분석하는 경우 
    * Update previous portfolio
        1. 리밸런싱
        * get_update_list 
            1. From new_portfolio_list and (previous)portfolio_list get update_list
            ```
            # From
            new_portfolio_dict = {"Strategy" : 0001, "A000120" : 50, "A009340" : 100, "A349400" : 1000}
            (previous)portfolio_dict = {"A000120" : 10, "A009340" : 150}
            
            # Get
            update_stock_list = ["A000120", -10, 39000, -390000, 138, 'add'] 
                # [Stock_code, quantity, price, Transaction volume, Transaction cost, state]
                # the state is in ['add'(추가 매수), 'sell'(매도), 'enterance'(신규 진입), 'clear'정리(전량 매도)]
            update_portfolio_list = [Time, list1, list2, list3, ..., Transaction Volume, Transaction cost]
                # [Transaction time, update_stock_list1, update_stock_list2, ..., Total volume, Total transaction cost]
            ```
     
       
  
  setting 합니다. 운용 전략에 맞는 포트폴리오 구성 정보를 넘겨받아 필요에 따라 매수 및 매도 주문을 수행합니다.
  ```
  status = 'update' # 'new' - Organize new portfolio / 'update' - Rebalance portfolio
    # (previous) portfolio_dict = {"A000120" : 10, "A009340" : 150}
  portfolio_dict = {"A000120" : 50, "A009340" : 100, "A349400" : 1000}
  set_portfolio(portfolio_dict) # 변경된 포트폴리오를 구성하기 위한 주문을 분석하고 기록한다
    # Order_dict = {"A000120" : 40, "A009340" : -50, "A349400" : 1000}
    # Ordering(Orering_dict)
    # append(log) = (Time, ("stock_code", price(per), quantity, status(New, Quit, Add, Subtract)),...)
  ```
* Ordering 
  * Ordering 은 주식을 주문하는 기능입니다. 개별 주식 단순 주문 뿐만 아니라 여러 주식을 동시에 주문하거나 주식 계정 리밸런싱 기능까지 제공합니다.
  ```
   today = datetime.today()
   order_list = ["A000120", "A009340"]
   order_dict = {"A000120" : 30, "A009340" : 100, "A349400" : 4000}
   pocket.order(order_dict, today) # make given order at given date
  ```
* Logging
  * Logging 은 주식을 샀던 기록들을 남기는 기능입니다. 주식 매매기록이 언제 이뤄졌는지를 볼 수 있게 해줍니다.
  ```
   pocket.logs.activate = True
   # After Transactions ...
   print(pocket.logs)
  ```
  * Logging 은 Tracking 기능까지 제공합니다.
  ```
   tracker = pocket.logger()
   start = datetime(2018, 12, 31)
   end = datetime(2019, 1, 31)
   tracker.log(start, end) # Transactions Log from "start" to "end"
  ``` 
* Analyzing
  * Analyzing 은 주어진 기간동안 Order기록을 기반으로 자산의 기본 정보들을 트래킹할 수 있게 합니다.
  ```
   analyzer = pocket.Analyzer()
   start = datetime(2018, 12, 31)
   end = datetime(2019, 1, 31)
   analyzer.summarize(start, end) # Analyzing Basic Statistics from "start" to "end"
  ```


# Implementation Todos

1. Abstraction - Pocket
2. Data Fetching - Google Drive
3. API Implementation


# API Description

### Ordering

* order(asset, amount, time)
  * market_order
  * limit_order
  * stop_order
  * stop_limit_order
  
### Logging

* logging(filepath) - save logs at filepath

### Analyzing

* viewing 
  * View() - transaction, balance system for quant
  
  
## Practice
* Practice


