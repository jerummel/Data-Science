'''This module contains the function that is used to create charts for the blog.'''

import matplotlib.pyplot as plt

def plotFigure(data, chartKind, chartTitle, xLabel, yLabel, colors, chartSize, rotation, fileName, needsYLim, YLim):
	fig = plt.figure()
	subplot = fig.add_subplot(111)
	data.plot(kind = chartKind, ax=subplot, title=chartTitle, color=colors, figsize = chartSize, rot=rotation)
	subplot.set_xlabel(xLabel)
	subplot.set_ylabel(yLabel)
	#subplot.autoscale(enable=False)
	if(needsYLim):
		subplot.set_ylim(YLim)
	fig.savefig(fileName)