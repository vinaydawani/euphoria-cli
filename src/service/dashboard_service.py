try:
    from store import euphoriaData
except ImportError:
    from ..store import euphoriaData


def getData():
    data = {}

    data["WAGMI Price"] = euphoriaData.wagmi_price
    data["Market Cap"] = euphoriaData.market_cap
    data["TVL"] = euphoriaData.staking_TVL
    data["APY"] = euphoriaData.staking_APY
    data["Current Index"] = euphoriaData.currentIndex
    data["Treasury balance"] = 0  # to be calculated
    data["Backing per $WAGMI"] = 0  # to be calculated
    data["Runway"] = 0  # to be calculated

    return data
