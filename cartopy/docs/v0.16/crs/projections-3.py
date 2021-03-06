import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(5.1299, 3))
ax = plt.axes(projection=ccrs.AlbersEqualArea())
ax.coastlines(resolution='110m')
ax.gridlines()