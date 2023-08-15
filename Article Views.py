""" Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.

 

Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+ """

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

  merged_df = views.merge(views, how='inner', left_on=['author_id', 'viewer_id'], right_on= ['viewer_id', 'author_id'])
    
    # Filter for rows where author_id equals viewer_id
  result_df = merged_df[merged_df['author_id_x'] == merged_df['viewer_id_x']]
    
    # Select the 'author_id_x' column and remove duplicates
  result_df = result_df[['author_id_x']].drop_duplicates()
    
    # Rename the column to 'id'
  result_df.columns = ['id']
    
    # Sort the result by 'id' in ascending order
  result_df = result_df.sort_values(by='id')
    
  return result_df