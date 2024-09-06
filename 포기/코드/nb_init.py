import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns
import sklearn as skl



if __name__ == "__main__":
    print(f"pandas: pd {pd.__version__}")
    print(f"numpy: np {np.__version__}")
    print(f"matplotlib: mpl {mpl.__version__}")
    print(f"seaborn: sns {sns.__version__}")
    print(f"sklearn: sns {skl.__version__}")
    
    font_path = "c:/Windows/Fonts/malgun.ttf"
    font_prop = mpl.font_manager.FontProperties(fname=font_path)
    mpl.rcParams['font.family'] = font_prop.get_name()
    mpl.rcParams['axes.unicode_minus'] = False
