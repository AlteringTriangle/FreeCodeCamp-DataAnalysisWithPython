import numpy as np


def calculate(l):
    if len(l) < 9:
        raise ValueError('List must contain nine numbers.')

    nl = np.array([l[:3], l[3:6], l[6:9]])

    """  
      m_ax1 = nl.mean(axis=0)
      m_ax2 = nl.mean(axis=1)
      m_fla = nl.mean()
  
      v_ax1 = nl.variance(axis=0)
      v_ax2 = nl.variance(axis=1)
      v_fla = nl.variance()
  
      s_ax1 = nl.std(axis=0)
      s_ax2 = nl.std(axis=1)
      s_fla = nl.std()
  
      max_ax1 = nl.max(axis=0)
      max_ax2 = nl.max(axis=1)
      max_fla = nl.max()
  
      min_ax1 = nl.min(axis=0)
      min_ax2 = nl.min(axis=1)
      min_fla = nl.min()
  
      sum_ax1 = nl.sum(axis=0)
      sum_ax2 = nl.sum(axis=1)
      sum_fla = nl.sum()
    """
    calculations = {'mean': [nl.mean(axis=0).tolist(), nl.mean(axis=1).tolist(), nl.mean()],
                    'variance': [nl.var(axis=0).tolist(), nl.var(axis=1).tolist(), nl.var()],
                    'standard deviation': [nl.std(axis=0).tolist(), nl.std(axis=1).tolist(), nl.std()],
                    'max': [nl.max(axis=0).tolist(), nl.max(axis=1).tolist(), nl.max()],
                    'min': [nl.min(axis=0).tolist(), nl.min(axis=1).tolist(), nl.min()],
                    'sum': [nl.sum(axis=0).tolist(), nl.sum(axis=1).tolist(), nl.sum()]}

    return calculations
