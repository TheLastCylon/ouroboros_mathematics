import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc, FancyArrowPatch
from matplotlib.path import Path

THETA_DEG = 55
THETA = np.radians(THETA_DEG)

# Key points
O = np.array([0.0, 0.0])
B = np.array([1.0, 0.0])
A = np.array([np.cos(THETA), np.sin(THETA)])
D = np.array([np.cos(THETA), 0.0])

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_aspect("equal")
ax.axis("off")

# -- Unit circle
circle = plt.Circle(O, 1.0, fill=False, color="#444444", linewidth=1.5, zorder=2)
ax.add_patch(circle)

# -- Triangle OAD (blue)
tri_OAD = plt.Polygon([O, A, D], closed=True,
                      facecolor="#cce5ff", edgecolor="#2255aa",
                      linewidth=1.5, zorder=3, alpha=0.8)
ax.add_patch(tri_OAD)

# -- Triangle ADB (orange)
tri_ADB = plt.Polygon([A, D, B], closed=True,
                      facecolor="#ffe5cc", edgecolor="#cc6600",
                      linewidth=1.5, zorder=3, alpha=0.8)
ax.add_patch(tri_ADB)

# -- Right-angle marker at D
sq = 0.035
ax.plot([D[0] - sq, D[0] - sq, D[0]], [D[1], D[1] + sq, D[1] + sq],
        color="#444444", linewidth=1.2, zorder=5)

# -- Angle arc at O
angle_arc = Arc(O, 0.30, 0.30, angle=0,
                theta1=0, theta2=THETA_DEG,
                color="#2255aa", linewidth=1.5, zorder=5)
ax.add_patch(angle_arc)

# -- x-axis (light, dashed)
ax.plot([-0.15, 1.15], [0, 0], color="#aaaaaa", linewidth=1.0,
        linestyle="--", zorder=1)

# -- Points
for point, label, ha, va in [
    (O, "$O$",  "right",  "top"),
    (B, "$B$",  "left",   "center"),
    (A, "$A$",  "left",   "bottom"),
    (D, "$D$",  "right",  "top"),
]:
    ax.plot(*point, "o", color="#333333", markersize=5, zorder=6)
    offset = {"right": (-0.045, 0), "left": (0.045, 0),
              "center": (0.045, 0)}
    voffset = {"top": (0, -0.045), "bottom": (0, 0.045), "center": (0, 0)}
    dx = offset[ha][0] + voffset[va][0]
    dy = offset[ha][1] + voffset[va][1]
    ax.text(point[0] + dx, point[1] + dy, label,
            ha=ha, va=va, fontsize=14, zorder=7)

# -- Segment labels
def midpoint(P, Q):
    return 0.5 * (P + Q)

def label_segment(P, Q, text, offset, color="#333333", fontsize=12):
    m = midpoint(P, Q)
    ax.text(m[0] + offset[0], m[1] + offset[1], text,
            ha="center", va="center", fontsize=fontsize,
            color=color, zorder=7)

# OD  (along x-axis, below)
label_segment(O, D, r"$OD = \cos\theta$", (0.0, -0.07), color="#2255aa")

# AD  (vertical, to the right)
label_segment(A, D, r"$AD = \sin\theta$", (0.13, 0.0), color="#2255aa")

# DB  (along x-axis, above -- versin)
label_segment(D, B, r"$DB = \mathrm{versin}(\theta)$", (0.0, 0.07), color="#cc6600")

# AB  (chord, to the left of the chord)
chord_mid = midpoint(A, B)
perp = np.array([-(B - A)[1], (B - A)[0]])
perp = perp / np.linalg.norm(perp) * 0.09
label_segment(A, B, r"$AB = \mathrm{chord}$",
              (perp[0] - 0.04, perp[1] + 0.04), color="#333333")

# -- Angle label
angle_label_r = 0.22
ax.text(angle_label_r * np.cos(THETA / 2),
        angle_label_r * np.sin(THETA / 2),
        r"$\theta$", ha="center", va="center",
        fontsize=13, color="#2255aa", zorder=7)

ax.set_xlim(-0.25, 1.35)
ax.set_ylim(-0.25, 1.15)

plt.tight_layout()
plt.savefig("papers/images/construction_diagram.png", dpi=150, bbox_inches="tight")
print("Saved: papers/images/construction_diagram.png")
