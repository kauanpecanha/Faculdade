# estimativa da demanda máxima

from maxPackage import firstOrderDiff, secondOrderDiff, thirdOrderDiff, plotMaxGraphics, createMaxFunction
fod = firstOrderDiff()
sod = secondOrderDiff(fod)
tod = thirdOrderDiff(sod)
maxTime, maxDemand = createMaxFunction(fod, sod, tod)
plotMaxGraphics(maxTime, maxDemand, fod, sod, tod)