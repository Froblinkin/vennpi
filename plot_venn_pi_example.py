from pybedtools import BedTool
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from _venn_pie import pie2

font = {'family' : 'sans',
        'weight' : 'bold',
        'size'   : 16}
matplotlib.rc('font', **font)

peaksA=BedTool("data/peaksA.bed")
peaksB=BedTool("data/peaksB.bed")

# marker symbols
markers = {
	"3'" : "P",
	"5'" : "X",
	'Intergenic' : "^",
	'TTS' : "1",
	'exon' : "D",
	'intron' : "s",
	'non-coding' : "*",
	'promoter-TSS' : "o"
}

# dict counting annotations in each section of Venn diagram 
venn2_dict = {}
[venn_dict[x]={} for x in ["01","10","11"]]

for f in markers:
	sub_peaksA = BedTool([x for x in peaksA if x.fields[3] == f])
	sub_peaksB = BedTool([x for x in peaksB if x.fields[3] == f])
	venn2_dict["01"][f] = len(sub_peaksA) / len(peaksA)
	venn2_dict["10"][f] = len(sub_peaksB) / len(peaksB)
	venn2_dict["11"][f] = len(sub_peaksA.intersect(sub_peaksB)) / len(peaksA.intersect(peaksB))

sumA = len(peaksA)
sumB = len(peaksB)
sumAB = len(peaksA.intersect(peaksB))

fig, ax = plt.subplots()

venn2(subsets = (sumA, sumB, sumAB), ax = ax, set_labels = ("H3K27ac", "Pol II"))
pie2((sumA, sumB, sumAB), ax, venn2_dict, markers)

plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.show()