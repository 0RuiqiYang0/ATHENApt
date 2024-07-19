# Code-Astro-Group
#### This is a Python package for ATHENA++ visualization inspred by <a href="https://github.com/PrincetonUniversity/athena/wiki/Plotting-Scripts#plot_slicepy">athena++ plotting scripts</a>
This package takes a 2D color plot of a single quantity from an Athena++ `.athdf` file. 3D data will be sliced, averaged, or summed as requested. A stream plot of a vector field from the same file can be overlayed. The script is best used in Cartesian coordinates. Plots are made in coordinate space like x-y or y-z plane. Averaging and summing are done in a naive way so that the package will not be able to handle AMR(Adaptive Mesh Refinement) output data. Stream plots are similarly done as simply as possible, without accounting for subtleties with vector bases. 

Usage (in terminal): `plot_lines.py <data_files> <x_names> <y_names> <output_file> [<options>]`

Arguments introduction can be found at <a href="https://github.com/PrincetonUniversity/athena/wiki/Plotting-Scripts#plot_slicepy">athena++ plotting scripts</a>

Additional arguments to the original scripts:

`-fig_width`: width of the figure in inches

`-fig_height`: height of teh figure in inches

`-dpi`: dots per inch(DPI) of the output plot

`-format`: output file format(e.g., png, jpg, tif)

## Installation
```

```

## Example
```
python -m ATHENApt.plot_slice disk.out2.00800.athdf vel1 test_plot_vel.png
--direction 3 --x_min 1.0 --x_max 10.0 --vmin 0 --vmax 0.8 -fig_width 12.0 -fig_height 12.0 -dpi 300
```
<div align="center">
  <img src="tst/test_out.png">
</div>


---------------------------------
## Collaborator
#### Ruiqi Yang
#### Xiaoyuan Yang
#### Ruining Zhao
---------------------------------
**Code/Astro 2024**
