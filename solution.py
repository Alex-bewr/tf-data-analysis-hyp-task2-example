import pandas as pd
import numpy as np
import scipy.stats as st


chat_id = 441809625 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.01
    a = st.anderson_ksamp([x, y]).pvalue
    
    return a < alpha
