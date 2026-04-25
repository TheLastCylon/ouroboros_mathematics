import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ============================================================
# Angle Addition Diagram
#
# Shows the geometric construction for sin(A+B) and cos(A+B):
#
#   P_A  = point on unit circle at angle A
#   P_B  = point on unit circle at angle A+B
#   F    = foot of perpendicular from P_B onto ray OP_A
#
# The right triangle OFP_B has:
#   OF   = cos(B)  along ray OP_A
#   FP_B = sin(B)  perpendicular to ray OP_A
#
# The perpendicular direction is (-sin A, cos A) -- a 90 degree
# counterclockwise rotation of (cos A, sin A). This is where the
# minus sign in cos(A+B) lives: in the geometry, not the algebra.
#
# Run:
#   python3 angle_addition_diagram.py
# ============================================================

A_deg = 38.0
B_deg = 32.0

A = np.deg2rad(A_deg)
B = np.deg2rad(B_deg)
AB = A + B

# Key points
O  = np.array([0.0, 0.0])
PA = np.array([np.cos(A),  np.sin(A)])
PB = np.array([np.cos(AB), np.sin(AB)])

# F: foot of perpendicular from PB onto ray OP_A
# F = (PB . PA_unit) * PA_unit  (since |PA| = 1, PA_unit = PA)
OF_len = np.dot(PB, PA)          # = cos(B) on the unit circle
F  = OF_len * PA

# Perpendicular direction at F (90 deg CCW from PA direction)
perp = np.array([-PA[1], PA[0]])  # (-sin A, cos A)

# ============================================================
# Plot
# ============================================================

fig, ax = plt.subplots(figsize=(9, 9))
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-0.25, 1.35)
ax.set_ylim(-0.25, 1.25)

# -- Unit circle (light gray) --
theta_circle = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(theta_circle), np.sin(theta_circle),
        color='lightgray', linewidth=1.5, zorder=1)

# -- Axes --
ax.annotate('', xy=(1.25, 0), xytext=(-0.2, 0),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.2))
ax.annotate('', xy=(0, 1.20), xytext=(0, -0.2),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.2))

# -- Ray OP_A (extended slightly beyond P_A) --
PA_ext = 1.08 * PA
ax.plot([O[0], PA_ext[0]], [O[1], PA_ext[1]],
        'k-', linewidth=1.5, zorder=2)

# -- Ray OP_B --
PB_ext = 1.08 * PB
ax.plot([O[0], PB_ext[0]], [O[1], PB_ext[1]],
        'k-', linewidth=1.5, zorder=2)

# -- OF segment (highlighted) --
ax.plot([O[0], F[0]], [O[1], F[1]],
        color='steelblue', linewidth=2.5, zorder=3, solid_capstyle='round')

# -- FP_B segment (highlighted) --
ax.plot([F[0], PB[0]], [F[1], PB[1]],
        color='firebrick', linewidth=2.5, zorder=3, solid_capstyle='round')

# -- Dashed line from O to P_B (shows the full triangle) --
ax.plot([O[0], PB[0]], [O[1], PB[1]],
        'k--', linewidth=1.0, zorder=2, alpha=0.5)

# -- Right angle mark at F --
mark_size = 0.028
along = PA / np.linalg.norm(PA)        # unit along ray OP_A
perp_u = perp / np.linalg.norm(perp)  # unit perpendicular
corner1 = F + mark_size * along
corner2 = F + mark_size * along + mark_size * perp_u
corner3 = F + mark_size * perp_u
ax.plot([corner1[0], corner2[0], corner3[0]],
        [corner1[1], corner2[1], corner3[1]],
        'k-', linewidth=1.0, zorder=4)

# -- Angle arc for A (x-axis to ray OP_A) --
arc_r_A = 0.18
theta_arc_A = np.linspace(0, A, 60)
ax.plot(arc_r_A * np.cos(theta_arc_A), arc_r_A * np.sin(theta_arc_A),
        'k-', linewidth=1.2, zorder=3)
# Label A
A_label_pos = (arc_r_A + 0.06) * np.array([np.cos(A / 2), np.sin(A / 2)])
ax.text(A_label_pos[0], A_label_pos[1], r'$A$',
        fontsize=14, ha='center', va='center')

# -- Angle arc for B (ray OP_A to ray OP_B) --
arc_r_B = 0.26
theta_arc_B = np.linspace(A, AB, 60)
ax.plot(arc_r_B * np.cos(theta_arc_B), arc_r_B * np.sin(theta_arc_B),
        'k-', linewidth=1.2, zorder=3)
# Label B
B_mid = (A + AB) / 2
B_label_pos = (arc_r_B + 0.06) * np.array([np.cos(B_mid), np.sin(B_mid)])
ax.text(B_label_pos[0], B_label_pos[1], r'$B$',
        fontsize=14, ha='center', va='center')

# -- Points --
for point, label, offset in [
    (O,  r'$O$',   (-0.07, -0.06)),
    (PA, r'$P_A$', ( 0.05,  0.00)),
    (PB, r'$P_B$', ( 0.05,  0.02)),
    (F,  r'$F$',   (-0.09, -0.06)),
]:
    ax.plot(point[0], point[1], 'ko', markersize=5, zorder=5)
    ax.text(point[0] + offset[0], point[1] + offset[1], label,
            fontsize=13, ha='center', va='center', fontweight='bold')

# -- Label OF with cos B (steelblue, along the segment) --
OF_mid = (O + F) / 2
OF_perp = np.array([-PA[1], PA[0]])  # perpendicular to OF, for offset
cos_label = OF_mid - 0.07 * OF_perp
ax.text(cos_label[0], cos_label[1], r'$\cos B$',
        fontsize=12, ha='center', va='center', color='steelblue')

# -- Label FP_B with sin B (firebrick, along the segment) --
FPB_mid = (F + PB) / 2
sin_label = FPB_mid + 0.07 * PA   # offset away from segment
ax.text(sin_label[0], sin_label[1], r'$\sin B$',
        fontsize=12, ha='center', va='center', color='firebrick')

# -- Label the perpendicular direction --
perp_label_pos = F + 0.18 * perp_u
ax.annotate('', xy=perp_label_pos, xytext=F + 0.04 * perp_u,
            arrowprops=dict(arrowstyle='->', color='dimgray', lw=1.2))
ax.text(perp_label_pos[0] + 0.04, perp_label_pos[1],
        r'$(-\sin A,\ \cos A)$',
        fontsize=11, ha='left', va='center', color='dimgray')

# -- Coordinate projections of P_B (dashed, to axes) --
ax.plot([PB[0], PB[0]], [0, PB[1]],
        ':', color='gray', linewidth=1.0, alpha=0.7, zorder=1)
ax.plot([0, PB[0]], [PB[1], PB[1]],
        ':', color='gray', linewidth=1.0, alpha=0.7, zorder=1)

# -- Label the coordinates of P_B on the axes --
ax.text(PB[0], -0.07, r'$\cos(A{+}B)$',
        fontsize=11, ha='center', va='center', color='gray')
ax.text(-0.07, PB[1], r'$\sin(A{+}B)$',
        fontsize=11, ha='center', va='center', color='gray', rotation=90)

plt.tight_layout()
plt.savefig('../images/angle_addition_diagram.png', dpi=150, bbox_inches='tight')
plt.show()
