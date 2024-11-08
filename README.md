# Letter-value plots
Letter-value plots to eliminate anomalies or outlier pixel values ​​in digital remote sensing images. Outliers often appear in quite complex mathematical operations, such as exponentials, logarithms, square roots, and so on. Outlier values ​​have the potential to change the visual quality of the image, and of course will have a direct impact on the statistical analysis of the image.<br/>

### Instructions:

You can use the file ```Cleaning_pixel_outliers.ipynb``` as an example of the implementation. The file ```Cleaning_pixel_outliers.ipynb``` and ```LvPlots.py``` file must be located in the same directory.<br/>

The method for calling Letter-value plots:<br/>
```
LvPlots.lvplots(image,rule='trustworthy',ci=95,ol_prop=0.007,left_fill=0,right_fill=0,zero=False)
```

```image``` is the image to be processed. The ```image``` must be a single band image and in NumPy array format. You can use Rasterio or GDAL to open your image file.<br/>

```rule``` is a parameter to stop the formation of the Letter-value plots. There are four rules that can be set for ```rule```, namely ```'trustworthy'```, ```'proportion'```, ```'tukey'```, and ```'full'```. For a more complete explanation, please read the literature listed below. If you do not set any value for ```rule``` then the default value of ```'trustworthy'``` will be used.<br/>

```ci``` is the confidence interval, the default value is 95%. ```ci``` will only have an effect if ```rule='trustworthy'```. You can set the value to ```ci=90``` or ```ci=99```, according to your needs.<br/>

```ol_prop``` is the proportion of outliers. This parameter will only take effect if you set ```rule='proportion'```. The default value is ```0.007```. You can change it to another value, and it must be less than 1.<br/>

```left_fill``` and ```right_fill``` are values ​​that will replace outlier values, respectively for the left side (outlier values ​​that are too low) and for the right side (outlier values ​​that are too high). By default, outlier values ​​in a digital image on both sides will be replaced with 0. You can use other values ​​if desired. If you want the minimum or the maximum values ​​of the cleaned data to be used as replacements for outliers, then ```left_fill``` or ```right_fill``` can be set to ```'fence'```, e.g. ```left_fill='fence'``` or ```right_fill='fence'```.<br/>

```zero``` is the option whether the value 0 will be included in the outliers calculation or not. The default value is ```False```, meaning the value 0 is not included. If you want the value 0 to be part of the outliers calculation, set ```zero=True```.<br/>

### Python prerequisites:<br/>
Python 3.9 or higher<br/>

### Required packages:<br/>
Rasterio (https://anaconda.org/conda-forge/rasterio)<br/>
NumPy (https://anaconda.org/anaconda/numpy)<br/>
SciPy (https://anaconda.org/anaconda/scipy)<br/>
Seaborn ((https://anaconda.org/anaconda/seaborn))<br/>

### Other requirements:<br/>
The codes are intended to be run in the JupyterLab environment.<br />

### Letter-value plots citation::<br/>
Hofmann, H., Wickham, H., & Kafadar, K. (2017). Letter-Value Plots: Boxplots for Large Data. Journal of Computational and Graphical Statistics, 26(3), 469–477. https://doi.org/10.1080/10618600.2017.1305277.<br/>
