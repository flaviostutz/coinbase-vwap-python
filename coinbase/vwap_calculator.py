
from mathutils import weighted_avg
from decimal import *

weighted_avgs = {}

def CalculateVWAP(matchInfo, averagerMaxSize, onVMAPInfo):
    pid = matchInfo['product_id']
    sa = weighted_avgs.get(pid)
    if sa == None:
        sa = weighted_avg.WeightedAvg(averagerMaxSize)
        weighted_avgs[pid] = sa

    sa.add(Decimal(matchInfo['price']), Decimal(matchInfo['size']))

    onVMAPInfo(sa.avg(), pid)

