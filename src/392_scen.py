#set font `Arial` to display non-ascii characters in matplotlib
.

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

prop = fm.FontProperties(fname='arial.ttf')
plt.title('unicode test \(\phi\delta\theta\)', fontproperties=prop)