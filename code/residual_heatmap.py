import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm

# 설정: 점성 계수 ν와 초기 진폭 A₀의 격자 생성
viscosity = np.linspace(0.01, 0.2, 200)
amplitude = np.linspace(0, 2.0, 200)
V, A = np.meshgrid(viscosity, amplitude)

# 구조적 경계: A*(ν) = Cν^{-α}
C = 0.5
alpha = 0.8
critical_boundary = C * V**(-alpha)

# 잔차 함수: 경계 위에서 급격한 증가
residual = np.exp((A - critical_boundary) * 5)
residual[A < critical_boundary] *= 0.1  # 경계 아래는 안정

# 시각화를 위한 클리핑
residual = np.clip(residual, 0, 100)

# 히트맵 생성
fig, ax = plt.subplots(figsize=(10, 6))
cmap = cm.get_cmap('coolwarm')
norm = Normalize(vmin=0, vmax=100)
heatmap = ax.pcolormesh(V, A, residual, cmap=cmap, norm=norm, shading='auto')

# 컬러바 추가
cbar = plt.colorbar(heatmap, ax=ax)
cbar.set_label('Residual Magnitude', fontsize=12)

# 경계 곡선 표시
boundary_curve = C * viscosity**(-alpha)
ax.plot(viscosity, boundary_curve, 'k--', linewidth=2, label=r'$A^*(\nu) \sim C\nu^{-\alpha}$')

# 라벨 및 제목
ax.set_xlabel('Viscosity (ν)', fontsize=12)
ax.set_ylabel('Initial Amplitude (A₀)', fontsize=12)
ax.set_title('Residual Heatmap of Navier–Stokes Surrogate Instability', fontsize=14)
ax.legend()

# 저장
plt.tight_layout()
plt.savefig("residual_heatmap.png", dpi=300)
plt.show()
