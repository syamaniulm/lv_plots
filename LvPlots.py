# Letter-value plots or Boxplots for removing pixel value anomalies from digital images
# These codes are intended for processing a single band digital image
# Code provided by Syam'ani (https://github.com/syamaniulm)

"""
Letter-value plots citation:

Hofmann, H., Wickham, H., & Kafadar, K. (2017). Letter-Value Plots: Boxplots for Large Data. Journal of Computational and Graphical Statistics, 26(3), 469–477. https://doi.org/10.1080/10618600.2017.1305277.
"""

class LvPlots:
    
    @staticmethod
    def lvp(image,rule='trustworthy'):
    
        print('Starting Letter-value plots computation...')

        import numpy as np
        import seaborn as sns
        
        # Resolving NaN and Infinite data
        image[np.isnan(image)] = 0
        image[np.isinf(image)] = 0
        
        # Reshaping image array
        image_array = np.reshape(np.array(image[image != 0]), (-1,1))

        # Calculating the main median (the letter "M") of the data
        dm = np.median(image_array)

        # Finding the first left and right boxes
        Left_box = image_array[image_array <= dm]
        Right_box = image_array[image_array > dm]

        # Calculating the first left and right boxes median (the letter "F") of the data
        left_med = np.median(Left_box)
        right_med = np.median(Right_box)

        # Defining how deep to dive in Letter-value plots
        if rule == 'proportion':
            # Assuming outliers contamination proportion of the data is 0.7%
            ol_prop = 0.007
            n_samples = len(image_array)
            lv_stop = int(np.floor(np.log2(n_samples)) - np.floor(np.log2(n_samples*ol_prop)))
        elif rule == 'trustworthy':
            # Using a 95% confidence interval
            z_value = 1.96
            n_samples = len(image_array)
            lv_stop = int(np.floor(np.log2(n_samples)) - np.floor(np.log2(2*(z_value**2))))
        elif rule == 'tukey':
            n_samples = len(image_array)
            lv_stop = int(np.floor(np.log2(n_samples)) - 3)
        elif rule == 'full':
            n_samples = len(image_array)
            lv_stop = int(np.floor(np.log2(n_samples)) + 1)
        else:
            print("There was an argument error in the rule.")
            print("Select one argument: 'proportion', 'trustworthy', 'tukey', or 'full'.")

        # Constructing the next left and right boxes to the last boxes
        for lv in range(2,lv_stop):
            Left_box = Left_box[Left_box <= left_med]
            Right_box = Right_box[Right_box > right_med]
            left_med = np.median(Left_box)
            right_med = np.median(Right_box)

        left_outlier_fence = round(left_med, 3)
        right_outlier_fence = round(right_med, 3)
        
        print('Left outlier fence  : {}'.format(left_outlier_fence))
        print('Right outlier fence : {}'.format(right_outlier_fence))

        # Removing anomaly pixel values from original image
        image[np.where((image < left_outlier_fence) | (image > right_outlier_fence))] = 0

        print('Letter-value plots computation completed...')

        # Drawing the Letter-value plots
        if rule == 'proportion':
            ax_lvplots = sns.boxenplot(x=image_array[:,0], k_depth=rule, outlier_prop=ol_prop)
        elif rule == 'tukey':
            ax_lvplots = sns.boxenplot(x=image_array[:,0], k_depth='tukey')
        elif rule == 'full':
            ax_lvplots = sns.boxenplot(x=image_array[:,0], k_depth='full')
        else:
            ax_lvplots = sns.boxenplot(x=image_array[:,0], k_depth='trustworthy')

        ax_lvplots.set_title(f'Letter-value plots using {rule}', fontsize=16)

        return image