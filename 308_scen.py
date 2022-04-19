#add color bar with image `mappable` to plot `plt`


```
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fig, ax = plt.subplots()
im = ax.imshow(mappable, cmap=cm.jet)

# Add colorbar, make sure to specify tick locations to match desired ticklabels
fig.colorbar(im, ax=ax, ticks=[.75, .8, .85, .9, .95, 1])
```