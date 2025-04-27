import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("Results_21MAR2022_nokcaladjust.csv")

# 筛选 vegan 和 vegetarian
veg_df = df[df['diet_group'].isin(['vegan', 'vegetarian'])]

# 提取需要的列并重命名
veg_df_selected = veg_df[['age_group', 'mean_ghgs', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'diet_group']]
veg_df_selected.columns = ['Age', 'Total_GHG', 'CH4', 'N2O', 'Diet']

# 数据清洗
cols = ['Total_GHG', 'CH4', 'N2O']
veg_df_selected[cols] = veg_df_selected[cols].apply(pd.to_numeric, errors='coerce')
veg_df_selected.dropna(subset=cols, inplace=True)

# 保持原点样式，只调整图例
sns.set(style="whitegrid")
plot = sns.pairplot(
    veg_df_selected,
    hue='Age',
    palette='Set2',
    diag_kind='hist'
)

# 添加标题
plot.fig.suptitle("GHG Emissions among Vegans and Vegetarians by Age", y=1.02)

# 调整图例位置和字体
plot._legend.set_bbox_to_anchor((1.05, 0.5))
plot._legend.set_title('Age')
for text in plot._legend.texts:
    text.set_fontsize(12)

# 保存改良版图像
plt.tight_layout()
plot.savefig("ghg_scatterplot_matrix_veg_age_improved.png", dpi=300)
plt.show()
