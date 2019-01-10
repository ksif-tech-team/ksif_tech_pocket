# ksif_tech_pocket

### Transaction, Balance Record System for Quant

Pocket 은 Quant 투자 과정에서 거래기록, 잔액을 기록하는 시스템입니다

Pocket 은 다음과 같은 기능을 제공합니다.
* Ordering 
  * Ordering 은 주식을 주문하는 기능입니다. 개별 주식 단순 주문 뿐만 아니라 여러 주식을 동시에 주문하거나 주식 계정 리밸런싱 기능까지 제공합니다.
* Logging
  * Logging 은 주식을 샀던 기록들을 남기는 기능입니다. 주식 매매기록이 언제 이뤄졌는지를 볼 수 있게 해줍니다.
* Analyzing
  * Analyzing 은 주어진 기간동안 Order기록을 기반으로 자산의 기본 정보들을 트래킹할 수 있게 합니다.

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


