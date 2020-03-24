# vennpi
## About
Vennpi is an add-on to [matplotlib-venn](https://pypi.org/project/matplotlib-venn/) that plots markers onto a Venn diagram to indicate how different slices of each Venn diagram chunk are organized like a connected series of non-circular pie plots. 

It was originally developed to compare [HOMER annotated peaks](http://homer.ucsd.edu/homer/ngs/annotation.html) where the Venn diagram would show the overlap between peaks and the pie charts would break down the annotations within some slice of a peak set. 

## Usage 

```python
from matplotlib_venn import venn2
from _venn_pie import pie2

markers=["*","+"]

venn2_dict = {}
# A
venn2_dict["01"]={"*":0.5,"+":0.5}
# B
venn2_dict["10"]={"*":0.75,"+":0.25}
# AB
venn2_dict["11"]={"*":0.33,"+":0.67}

venn2(subsets = (sumA, sumB, sumAB), ax = ax, set_labels = ("A", "B"))
pie2((sumA, sumB, sumAB), ax, venn2_dict, markers)

```

In the example, I used [pybedtools](https://daler.github.io/pybedtools/) to read in the peaks after reformating HOMER's output from annotatePeaks.pl with awk (commands shown below)
```
awk 'FNR > 1 {print $2"\t"$3"\t"$4"\t"$8"\t"$6"\t"$5}' peaksA.bed.anno > peaksA.bed

awk 'FNR > 1 {print $2"\t"$3"\t"$4"\t"$8"\t"$6"\t"$5}' peaksB.bed.anno > peaksB.bed
```
![sample](venn_pie_plot.png)
