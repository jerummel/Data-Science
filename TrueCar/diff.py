'''This script reads in 2 data files and outputs the differences between the two files to a
CSV file.'''

import pandas as pd

def report_diff(x):
    return x[0] if x[0] == x[1] else '{} | {}'.format(*x)

def main():
    old_df = pd.read_csv('bike_data_20110921.csv')
    new_df = pd.read_csv('bike_data_20140821.csv')

    # find new IDs added between 09212011 and 08212014
    added_df = new_df[~new_df['@ID'].isin(old_df['@ID'])]
    added_df['Action'] = 'Added'

    # find IDs that were removed between 09212011 and 08212014
    deleted_df = old_df[~old_df['@ID'].isin(new_df['@ID'])]
    deleted_df['Action'] = 'Deleted'

    # create 2 data frames that have IDs that existed on 09212011 and 08212014
    # one data frame will contain data from 09212011, the other from 08212014
    inBoth2011_df = old_df[old_df['@ID'].isin(new_df['@ID'])]
    inBoth2014_df = new_df[new_df['@ID'].isin(old_df['@ID'])]

    #Make the indices equal on both data frames
    inBoth2011_df.index = range(len(inBoth2011_df))
    inBoth2014_df.index = range(len(inBoth2014_df))

    # Find the rows that have no changes and put them into a dataframe
    ne = (inBoth2011_df != inBoth2014_df).any(1)
    inBoth2011_df['hasChange'] = ne
    inBoth2014_df['hasChange'] = ne
    noChanges_df = inBoth2011_df[~inBoth2011_df['hasChange']]
    noChanges_df = noChanges_df.drop('hasChange', 1)
    noChanges_df['Action'] = 'Unchanged'

    # Find the rows that have changes and show the diffs in a dataframe
    data2011 = inBoth2011_df[inBoth2011_df['hasChange']]
    data2014 = inBoth2014_df[inBoth2014_df['hasChange']]
    my_panel = pd.Panel(dict(df1=data2011,df2=data2014))
    modify_df = my_panel.apply(report_diff, axis=0)
    modify_df = modify_df.drop('hasChange', 1)
    modify_df['Action'] = 'Modified'
    
    # Create the final data frame and export to .csv
    final_df = pd.concat([modify_df, noChanges_df, deleted_df, added_df])
    cols = final_df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    final_df = final_df[cols]
    final_df['@ID'] = final_df['@ID'].astype(int)
    final_df = final_df.sort(columns='@ID')
    final_df.to_csv('changes.csv', index=False)

if __name__ == "__main__": main()