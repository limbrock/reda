import matplotlib as mpl
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
cb_pos = mpl_get_cb_bound_next_to_plot(ax)
ax1 = fig.add_axes(cb_pos, frame_on=True)
cmap = mpl.cm.jet_r
norm = mpl.colors.Normalize(vmin=float(23), vmax=float(33))
# cmap = pm.cmap
# norm = pm.norm
cb1 = mpl.colorbar.ColorbarBase(
    ax1,
    cmap=cmap,
    norm=norm,
    orientation='vertical'
)
cb1.locator = mpl.ticker.FixedLocator([23, 28, 33])
cb1.update_ticks()
cb1.ax.artists.remove(cb1.outline)    # remove framei
