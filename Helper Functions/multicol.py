def find_multicol(corr_matrix, threshold):
    correlated_cols = []
    
    # Loop through all columns
    for i in range(len(corr_matrix.columns)):
        #print(i)
        # Loop through all columns before ith column
        for j in range(i):
            #print(i, j)
            # Check if the variables before ith variable are highly correlated with ith variable
            if abs(corr_matrix.iloc[i,j]) > threshold:
                print(corr_matrix.columns[i], corr_matrix.columns[j])
                # Add to list of multicollinear columns
                correlated_cols.append(tuple(corr_matrix.columns[i], corr_matrix.columns[j]))