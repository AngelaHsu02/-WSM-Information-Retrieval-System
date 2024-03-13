from io import StringIO
import pandas as pd
import xgboost as xgb

if __name__ == "__main__":
    #data = '''query_id doc_id score1 score2 score3 relevance
    #401 WT01-B01-1 2.8 4.6 7.1 1
    #401 WT01-B12-3 2.9 4.3 8.2 0
    #401 WT01-B12-34 1.8 4.2 8.4 0
    #...
    #440 WT01-B23-45 0.5 5.3 6.2 1'''

    #data_file = StringIO(../data/mle_401_440.run)
    #df = pd.read_table(data_file, delim_whitespace=True)










#/mnt/c/Python/WSM/proj2_sample_run/sparse_retrieval/codes
#/mnt/c/Python/WSM/proj2_sample_run/data

    df = pd.read_excel("../../data/training.xlsx")
    #print(df)
    
    x = df[['bm25score', 'mlescore', 'jmscore']]
    y = df['relevance']

    model = xgb.XGBRegressor()
    model.fit(x, y)

    testingdf = pd.read_excel("../../data/testing.xlsx")
    print(testingdf)

    testingx = testingdf[['bm25score', 'mlescore', 'jmscore']]
    print(testingx)

    pred = model.predict(testingx)
    print(len(pred), pred)

    # Add the predictions to the testing dataframe
    testingdf['prediction'] = pred

    # Print the testing dataframe with predictions
    print(testingdf)
    #testingdf.to_excel("output_predictions.xlsx", index=False)
    testingdf = testingdf.drop(columns=['key', 'bm25score', 'mlescore', 'jmscore'])
    # Sort the DataFrame by 'query_id' and 'prediction' in descending order
    testingdf_sorted = testingdf.sort_values(by=['query_id', 'prediction'], ascending=[True, False])
    # Add a new column 'ranking' representing the rank within each 'query_id'
    testingdf_sorted['ranking'] = testingdf_sorted.groupby('query_id').cumcount() + 1
    testingdf_sorted['constant'] = 'Q0'
    testingdf_sorted['method'] = 'learntorank'
    testingdf_sorted = testingdf_sorted[['query_id', 'constant', 'doc_id', 'ranking', 'prediction', 'method']]

    print(testingdf_sorted)
    testingdf_sorted.to_csv("../runs/learn_441_450.run", sep=' ', index=False)

    

