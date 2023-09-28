# estimativa da demanda mínima

from minPackage import firstOrderDiff, secondOrderDiff, thirdOrderDiff, plotMinGraphics, createMinFunction
fod = firstOrderDiff()
sod = secondOrderDiff(fod)
tod = thirdOrderDiff(sod)
minTime, minDemand = createMinFunction(fod, sod, tod)
plotMinGraphics(minTime, minDemand, fod, sod, tod)