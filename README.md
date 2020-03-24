# vennpi
Vennpi is an add-on to [matplotlib-venn](https://pypi.org/project/matplotlib-venn/) that plots markers onto a Venn diagram to indicate how different slices of each Venn diagram chunk are organized like a connected series of non-circular pie plots. 

It was originally developed to compare [HOMER annotated peaks](http://homer.ucsd.edu/homer/ngs/annotation.html) where the Venn diagram would show the overlap between peaks and the pie charts would break down the annotations within some slice of a peak set. 

In the example, I used [pybedtools](https://daler.github.io/pybedtools/) to read in the peaks after reformating HOMER's output from annotatePeaks.pl with awk (commands shown below)
```
awk 'FNR > 1 {print $2"\t"$3"\t"$4"\t"$8"\t"$6"\t"$5}' peaksA.bed.anno > peaksA.bed

awk 'FNR > 1 {print $2"\t"$3"\t"$4"\t"$8"\t"$6"\t"$5}' peaksB.bed.anno > peaksB.bed
```
![sample](venn_pie_plot.png)
