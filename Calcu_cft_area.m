LONGXY=ncread('C:\Research2\cft_calcu\surfdata_0.5x0.5_for_calcu.nc','LONGXY');
LON=LONGXY(:,1);
LATIXY=ncread('C:\Research2\cft_calcu\surfdata_0.5x0.5_for_calcu.nc','LATIXY');
LAT=LATIXY(1,:)
AREA=ncread('C:\Research2\cft_calcu\surfdata_0.5x0.5_for_calcu.nc','AREA');

save('C:\Research2\cft_calcu\area_all.mat', 'AREA')

PCT_CROP=ncread('C:\Research2\cft_calcu\surfdata_0.5x0.5_for_calcu.nc','PCT_CROP');
PCT_CFT=ncread('C:\Research2\cft_calcu\surfdata_0.5x0.5_for_calcu.nc','PCT_CFT');
CFT_AREA = AREA.*PCT_CROP.*PCT_CFT;


cft_spr = [2, 4, 6, 8, 12, 14, 16, 18, 20, 32, 36, 38, 46, 50, 52, 54, 58, 60, 62]
size_spr = size(cft_spr)
size_spr = size_spr(2)
cft_dri = [10, 22, 24, 26, 28, 30, 34, 40, 42, 44, 56, 64]
size_dri = size(cft_dri)
size_dri = size_dri(2)

area_all_irr = zeros(720, 360);
for cft = 2 : 2 : 64
    area_all_irr = area_all_irr + CFT_AREA(:,:,cft);
end

area_sur_irr = zeros(720, 360);
area_sur_irr = area_sur_irr + CFT_AREA(:,:,48);

area_spr_irr = zeros(720, 360);
for i = 1 : size_spr
    cft = cft_spr(i)
    area_spr_irr = area_spr_irr + CFT_AREA(:,:,cft);
end


area_dri_irr = zeros(720, 360);
for i = 1 : size_dri
    cft = cft_dri(i)
    area_dri_irr = area_dri_irr + CFT_AREA(:,:,cft);
end

save('C:\Research2\cft_calcu\area_all_irr', 'area_all_irr')
save('C:\Research2\cft_calcu\area_sur_irr', 'area_sur_irr')
save('C:\Research2\cft_calcu\area_spr_irr', 'area_spr_irr')
save('C:\Research2\cft_calcu\area_dri_irr', 'area_dri_irr')

save('C:\Research2\cft_calcu\lon', 'lon')
save('C:\Research2\cft_calcu\lat', 'lat')