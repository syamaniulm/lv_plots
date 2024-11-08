# Letter-value plots
Letter-value plots to eliminate anomalies or outlier pixel values ​​in digital remote sensing images. Outliers often appear in quite complex mathematical operations, such as exponentials, logarithms, square roots, and so on. Outlier values ​​have the potential to change the visual quality of the image, and of course will have a direct impact on the statistical analysis of the image.<br/>

### Instructions:

You can use the file ```Cleaning_pixel_outliers.ipynb``` as an example of the implementation. The file ```Cleaning_pixel_outliers.ipynb``` and ```LvPlots.py``` file must be located in the same directory.<br/>

The method for calling Letter-value plots:<br/>
```
LvPlots.lvplots(image,rule='trustworthy',left_fill=0,right_fill=0,ol_prop=0.007,z_value=1.96,zero=False)
```

```image``` is the image to be processed. ```image``` must be in NumPy array format. You can use Rasterio or GDAL to open your image file.<br/>

There are four rules that can be applied in ```rule```, namely ```'trustworthy'``` (default), ```'proportion'```, ```'tukey'```, and ```'full'```. For a more complete explanation, please read the literature listed below.<br/>

```left_fill``` and ```right_fill``` are values ​​that will replace outlier values. By default, outlier values ​​in digital images will be replaced with 0. You can use other values ​​if desired.<br/>

```ol_prop``` is the proportion of outliers. This parameter will only take effect if you set ```rule='proportion'```. This The default value is ```0.007```. You can change it to another value, and it must be less than 1.<br/>

```z_value``` will only have an effect if ```rule='trustworthy'```. ```z_value=1.96``` is the default value for a 95% confidence interval. If you want a 99% confidence interval, set ```z_value=2.58```, or set ```z_value=1.65``` for a 90% confidence interval.<br/>

```zero``` is the option whether the value 0 will be included in the outliers calculation or not. The default value is ```False```, meaning the value 0 is not included. If you want the value 0 to be part of the outliers calculation, set ```zero=True```.<br/>

### Python prerequisites:<br/>
Python 3.9 or higher<br/>

### Required packages:<br/>
Rasterio (https://anaconda.org/conda-forge/rasterio)<br/>
NumPy (https://anaconda.org/anaconda/numpy)<br/>
Seaborn ((https://anaconda.org/anaconda/seaborn))<br/>

### Other requirements:<br/>
The codes are intended to be run in the JupyterLab environment.<br />

### Letter-value plots citation::<br/>
Hofmann, H., Wickham, H., & Kafadar, K. (2017). Letter-Value Plots: Boxplots for Large Data. Journal of Computational and Graphical Statistics, 26(3), 469–477. https://doi.org/10.1080/10618600.2017.1305277.<br/>
