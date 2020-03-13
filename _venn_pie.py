from matplotlib_venn._venn2 import *
import matplotlib
import numpy as np

def pie2(subsets, ax, venn_area, venn_markers, scale_factor = 21, boundary = 0.01, alpha = 1.0):
    '''Plots markers in Venn Diagram proportional to their pie chart area 

    '''
    venn_shapes=[x for x in ax.get_children() if type(x) == matplotlib.patches.PathPatch]
    
    mapping = {
        0 : "01",
        1 : "10",
        2 : "11"
    }

    # venn_area should have binary keys 
    try: 
        if not any([True if x in venn_area else False for x in mapping.values()]):
            raise KeyError
    except KeyError:
        print("Key mismatch")

    # Calculate relative scale, so proportional number of markers can be placed in each area
    subsets = list(subsets)
    subsets[0] -= subsets[2]
    subsets[1] -= subsets[2]

    marker_scale=[]

    for idx, shape in enumerate(venn_shapes):
        pie_areas = list(venn_area[mapping[idx]].values())
        pie_labels = [x for x in venn_area[mapping[idx]]]
        pie_markers = [venn_markers[x] for x in pie_labels]
        a,b,c,d = shape.get_path().get_extents().corners()
        marker_scale += [d - a]

    marker_scale = np.floor(marker_scale / np.max(marker_scale, 0) * scale_factor).astype(int)

    for idx, shape in enumerate(venn_shapes):
        pie_areas = list(venn_area[mapping[idx]].values())
        pie_labels = [x for x in venn_area[mapping[idx]]]
        pie_markers = [venn_markers[x] for x in pie_labels]
        a,b,c,d = shape.get_path().get_extents().corners()

        # marker locations across shape
        marker_fill=[(x, y) for x in np.linspace(a[0], d[0], marker_scale[idx][0]) for y in np.linspace(a[1], d[1], marker_scale[idx][1])
            if shape.get_path().contains_point((x - boundary, y - boundary)) and shape.get_path().contains_point((x + boundary, y - boundary)) and
                shape.get_path().contains_point((x - boundary, y + boundary)) and shape.get_path().contains_point((x + boundary, y + boundary))]

        # rounding markers 
        area_markers = np.floor(len(marker_fill) * np.array(pie_areas)).astype(int)
        leftover_markers = len(marker_fill) - sum(area_markers)
        leftover_area = len(marker_fill) * np.array(pie_areas) - area_markers

        while leftover_markers > 0:
            max_idx = np.argmax(leftover_area)
            leftover_area[max_idx] = 0
            area_markers[max_idx] += 1
            leftover_markers -= 1

        # plot markers for some annotation
        last_idx = 0
        for idy, i in enumerate(venn_markers):
            if len(marker_fill[last_idx : (last_idx + area_markers[idy])]) > 0:
                ax.scatter(*zip(*marker_fill[last_idx : (last_idx + area_markers[idy])]), color='r', marker = venn_markers[i], 
                	label = i if idx == 0 else "", alpha = alpha)
            last_idx += area_markers[idy]