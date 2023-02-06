import numpy as np
 
def detect_outlier(data):
    outliers = np.array([])
    outliers_count = 0
    data_ordem_crescente = np.sort(data)
    print(data_ordem_crescente)

    q1 = np.percentile(data_ordem_crescente,25,interpolation='nearest')
    q3 = np.percentile(data_ordem_crescente,75,interpolation='nearest')
 
    # compute IRQ
    iqr = q3 - q1
    
    # find lower and upper bounds
    lower_bound = q1 - (1.5 * iqr)
    
    upper_bound = q3 + (1.5 * iqr)
    
    isoutlier = [[element>= upper_bound or element<=lower_bound for element in row] for row in data]
    for row in isoutlier:
      for element in row:
        if element == True:
          outliers_count  = outliers_count+1
    for row in data:
      for element in row:
        if element>= upper_bound or element<=lower_bound:
          outliers = np.append(outliers,element)

    return isoutlier, outliers_count,outliers


matrix =  np.random.randn(300,15)
isoutlier, outliers_count,outliers = detect_outlier(matrix)