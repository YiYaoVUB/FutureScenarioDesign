import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt

country_frac_ssp126_dict = scio.loadmat('C:\Research2\Output_data\\country_frac_ssp126.mat')
country_frac_ssp126 = country_frac_ssp126_dict['country_frac']

country_frac_ssp370_dict = scio.loadmat('C:\Research2\Output_data\\country_frac_ssp370.mat')
country_frac_ssp370 = country_frac_ssp370_dict['country_frac']

country_frac_ssp585_dict = scio.loadmat('C:\Research2\Output_data\\country_frac_ssp585.mat')
country_frac_ssp585 = country_frac_ssp585_dict['country_frac']

country_area_ssp126_dict = scio.loadmat('C:\Research2\Output_data\\country_area_ssp126.mat')
country_area_ssp126 = country_area_ssp126_dict['country_area']

country_area_ssp370_dict = scio.loadmat('C:\Research2\Output_data\\country_area_ssp370.mat')
country_area_ssp370 = country_area_ssp370_dict['country_area']

country_area_ssp585_dict = scio.loadmat('C:\Research2\Output_data\\country_area_ssp585.mat')
country_area_ssp585 = country_area_ssp585_dict['country_area']

x = range(2015, 2101, 5)

index = 240
fig = plt.figure(figsize=[18,22], dpi=100)

ax1 = fig.add_subplot(3,2,1)

# plt.plot(country_frac_ssp126[index,:,0], color='blue')
# plt.plot(country_frac_ssp370[index,:,0], color='red')
# plt.plot(country_frac_ssp585[index,:,0], color='green')

plt.fill_between(x, country_frac_ssp126[index,:,2] - country_frac_ssp126[index,:,2], country_frac_ssp126[index,:,2], alpha = 0.4, color = 'green', label = 'drip')
plt.fill_between(x, country_frac_ssp126[index,:,2], country_frac_ssp126[index,:,2] + country_frac_ssp126[index,:,1], alpha = 0.4, color = 'blue', label = 'sprinkler')
plt.fill_between(x, country_frac_ssp126[index,:,2] + country_frac_ssp126[index,:,1], country_frac_ssp126[index,:,2] + country_frac_ssp126[index,:,1] + country_frac_ssp126[index,:,0], alpha = 0.4, color = 'red', label = 'flood')

ax1 = fig.add_subplot(3,2,3)

plt.fill_between(x, country_frac_ssp370[index,:,2] - country_frac_ssp370[index,:,2], country_frac_ssp370[index,:,2], alpha = 0.4, color = 'green', label = 'drip')
plt.fill_between(x, country_frac_ssp370[index,:,2], country_frac_ssp370[index,:,2] + country_frac_ssp370[index,:,1], alpha = 0.4, color = 'blue', label = 'sprinkler')
plt.fill_between(x, country_frac_ssp370[index,:,2] + country_frac_ssp370[index,:,1], country_frac_ssp370[index,:,2] + country_frac_ssp370[index,:,1] + country_frac_ssp370[index,:,0], alpha = 0.4, color = 'red', label = 'flood')


ax1 = fig.add_subplot(3,2,5)

plt.fill_between(x, country_frac_ssp585[index,:,2] - country_frac_ssp585[index,:,2], country_frac_ssp585[index,:,2], alpha = 0.4, color = 'green', label = 'drip')
plt.fill_between(x, country_frac_ssp585[index,:,2], country_frac_ssp585[index,:,2] + country_frac_ssp585[index,:,1], alpha = 0.4, color = 'blue', label = 'sprinkler')
plt.fill_between(x, country_frac_ssp585[index,:,2] + country_frac_ssp585[index,:,1], country_frac_ssp585[index,:,2] + country_frac_ssp585[index,:,1] + country_frac_ssp585[index,:,0], alpha = 0.4, color = 'red', label = 'flood')


ax1 = fig.add_subplot(3,2,2)

plt.fill_between(x, country_area_ssp126[index,:,2] - country_area_ssp126[index,:,2], country_area_ssp126[index,:,2], alpha = 0.4, color = 'green', label = 'drip')
plt.fill_between(x, country_area_ssp126[index,:,2], country_area_ssp126[index,:,2] + country_area_ssp126[index,:,1], alpha = 0.4, color = 'blue', label = 'sprinkler')
plt.fill_between(x, country_area_ssp126[index,:,2] + country_area_ssp126[index,:,1], country_area_ssp126[index,:,2] + country_area_ssp126[index,:,1] + country_area_ssp126[index,:,0], alpha = 0.4, color = 'red', label = 'flood')

ax1 = fig.add_subplot(3,2,4)

plt.fill_between(x, country_area_ssp370[index,:,2] - country_area_ssp370[index,:,2], country_area_ssp370[index,:,2], alpha = 0.4, color = 'green', label = 'drip')
plt.fill_between(x, country_area_ssp370[index,:,2], country_area_ssp370[index,:,2] + country_area_ssp370[index,:,1], alpha = 0.4, color = 'blue', label = 'sprinkler')
plt.fill_between(x, country_area_ssp370[index,:,2] + country_area_ssp370[index,:,1], country_area_ssp370[index,:,2] + country_area_ssp370[index,:,1] + country_area_ssp370[index,:,0], alpha = 0.4, color = 'red', label = 'flood')


ax1 = fig.add_subplot(3,2,6)

plt.fill_between(x, country_area_ssp585[index,:,2] - country_area_ssp585[index,:,2], country_area_ssp585[index,:,2], alpha = 0.4, color = 'green', label = 'drip')
plt.fill_between(x, country_area_ssp585[index,:,2], country_area_ssp585[index,:,2] + country_area_ssp585[index,:,1], alpha = 0.4, color = 'blue', label = 'sprinkler')
plt.fill_between(x, country_area_ssp585[index,:,2] + country_area_ssp585[index,:,1], country_area_ssp585[index,:,2] + country_area_ssp585[index,:,1] + country_area_ssp585[index,:,0], alpha = 0.4, color = 'red', label = 'flood')

plt.show()