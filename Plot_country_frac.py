import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt
import matplotlib as mpl

def set_plot_param():
    """Set my own customized plotting parameters"""

    #mpl.rc('axes', edgecolor='dimgrey')
    #mpl.rc('axes', labelcolor='dimgrey')
    #mpl.rc('xtick', color='dimgrey')
    #mpl.rc('ytick', color='dimgrey')
    mpl.rc('legend', fontsize='large')
    mpl.rc('text', color='dimgrey')

def get_data_from_mat(file, variable):
    var_dict = scio.loadmat(file)
    var = var_dict[variable]
    return var

country_frac_ssp126 = get_data_from_mat('C:\Research2\Output_data\\country_frac_ssp126.mat', 'country_frac')
country_frac_ssp370 = get_data_from_mat('C:\Research2\Output_data\\country_frac_ssp370.mat', 'country_frac')
country_frac_ssp585 = get_data_from_mat('C:\Research2\Output_data\\country_frac_ssp585.mat', 'country_frac')

country_area_ssp126 = get_data_from_mat('C:\Research2\Output_data\\country_area_ssp126.mat', 'country_area')
country_area_ssp370 = get_data_from_mat('C:\Research2\Output_data\\country_area_ssp370.mat', 'country_area')
country_area_ssp585 = get_data_from_mat('C:\Research2\Output_data\\country_area_ssp585.mat', 'country_area')


x = range(2010, 2101, 5)
index = 190 # country index 190 = USA; 240 = China; 36 = India; 38 = Pakistan

fig = plt.figure(figsize=[12,8], dpi=100)
fig.subplots_adjust(hspace=0.2, wspace=0.2, left = 0.07, right = 0.95, top = 0.95, bottom = 0.05)
set_plot_param()

color1 = (0.2, 0.73, 0.3)   # grass
color2 = (0.75, 0.75, 1)    # light blue
color3 = (0.6, 0.24, 0.24)  # nice red

def plot_irrigation_fraction(x, y0, y1, y2, y3, y_label, y_lim = (0, 1)):
    plt.fill_between(x, y0, y1, alpha=0.4, color='limegreen', label='drip')
    plt.fill_between(x, y1, y2, alpha=0.4, color='dodgerblue', label='sprinkler')
    plt.fill_between(x, y2, y3, alpha=0.4, color='darkred', label='flood')

    plt.ylabel(y_label, fontsize=14)
    plt.ylim(y_lim)
    plt.xlim(2010, 2100)

    plt.xticks([2020, 2040, 2060, 2080, 2100], ['2020', '2040', '2060', '2080', '2100'], fontsize=12)
    plt.yticks(fontsize=12)


ax1 = fig.add_subplot(3,2,1)
plot_irrigation_fraction(x, country_frac_ssp126[index,:,2] - country_frac_ssp126[index,:,2],
                         country_frac_ssp126[index,:,2],
                         country_frac_ssp126[index,:,2] + country_frac_ssp126[index,:,1],
                         country_frac_ssp126[index,:,2] + country_frac_ssp126[index,:,1] + country_frac_ssp126[index,:,0],
                         'fraction')
plt.legend(loc = 'upper left')


ax1 = fig.add_subplot(3,2,3)
plot_irrigation_fraction(x, country_frac_ssp370[index,:,2] - country_frac_ssp370[index,:,2],
                         country_frac_ssp370[index,:,2],
                         country_frac_ssp370[index,:,2] + country_frac_ssp370[index,:,1],
                         country_frac_ssp370[index,:,2] + country_frac_ssp370[index,:,1] + country_frac_ssp370[index,:,0],
                         'fraction')


ax1 = fig.add_subplot(3,2,5)
plot_irrigation_fraction(x, country_frac_ssp585[index,:,2] - country_frac_ssp585[index,:,2],
                         country_frac_ssp585[index,:,2],
                         country_frac_ssp585[index,:,2] + country_frac_ssp585[index,:,1],
                         country_frac_ssp585[index,:,2] + country_frac_ssp585[index,:,1] + country_frac_ssp585[index,:,0],
                         'fraction')


ax1 = fig.add_subplot(3,2,2)
plot_irrigation_fraction(x, (country_area_ssp126[index,:,2] - country_area_ssp126[index,:,2])/1000,
                         (country_area_ssp126[index,:,2])/1000,
                         (country_area_ssp126[index,:,2] + country_area_ssp126[index,:,1])/1000,
                         (country_area_ssp126[index,:,2] + country_area_ssp126[index,:,1] + country_area_ssp126[index,:,0])/1000,
                         'area ($\mathregular{10^3}$ $\mathregular{km^2}$)', (0, 230))


ax1 = fig.add_subplot(3,2,4)
plot_irrigation_fraction(x, (country_area_ssp370[index,:,2] - country_area_ssp370[index,:,2])/1000,
                         (country_area_ssp370[index,:,2])/1000,
                         (country_area_ssp370[index,:,2] + country_area_ssp370[index,:,1])/1000,
                         (country_area_ssp370[index,:,2] + country_area_ssp370[index,:,1] + country_area_ssp370[index,:,0])/1000,
                         'area ($\mathregular{10^3}$ $\mathregular{km^2}$)', (0, 230))


ax1 = fig.add_subplot(3,2,6)
plot_irrigation_fraction(x, (country_area_ssp585[index,:,2] - country_area_ssp585[index,:,2])/1000,
                         (country_area_ssp585[index,:,2])/1000,
                         (country_area_ssp585[index,:,2] + country_area_ssp585[index,:,1])/1000,
                         (country_area_ssp585[index,:,2] + country_area_ssp585[index,:,1] + country_area_ssp585[index,:,0])/1000,
                         'area ($\mathregular{10^3}$ $\mathregular{km^2}$)', (0, 230))


plt.show()