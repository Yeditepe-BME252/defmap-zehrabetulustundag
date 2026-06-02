import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8), dpi=150)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# Arkaplan
ax.set_facecolor("#f2f2f2")

# --------------------
# Gri yardımcı ızgara
# --------------------
minor = np.arange(-3, 3.001, 0.3)

for x in minor:
    ax.axvline(x, color="#c0c0c0", lw=0.8, zorder=0)

for y in minor:
    ax.axhline(y, color="#c0c0c0", lw=0.8, zorder=0)

# --------------------
# Mavi ızgara
# --------------------
blue = np.arange(-3, 3.001, 0.35)

# Dikey çizgiler: tüm yükseklik boyunca
for x in blue:
    ax.plot([x, x], [-2.5, 2.5],
            color="#0066cc", lw=0.8)

# Yatay çizgiler: tüm genişlik boyunca
for y in np.arange(-2.5, 2.501, 0.25):
    ax.plot([-3, 3], [y, y],
            color="#0066cc", lw=0.8)

# Ana eksenler
ax.axhline(0, color="black", lw=1.3)
ax.axvline(0, color="black", lw=1.3)

# Tikler
ax.set_xticks(np.arange(-3, 4, 1))
ax.set_yticks(np.arange(-3, 4, 1))

# Etiketler
ax.set_xlabel(r"$a_1$", fontsize=15)
ax.set_ylabel(r"$a_2$", fontsize=15, rotation=0, labelpad=12)

# Çerçeveleri kaldır
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_aspect('equal')
plt.tight_layout()
plt.show()