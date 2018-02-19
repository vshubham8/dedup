DeDup - An analytics tool for deduplicating your records in a file
=====================================================
Functionalities provided by this tool:
-----------------------------------------------------
**Remove entries/records of the same person from a file, that appears many times !**
-----------------------------------------------------
**It will produce a new file having all the unique records !**
-----------------------------------------------------
**Technique Used: Cosine Similarity**
-----------------------------------------------------
- Cosine Similarity is a measure of the cohesiveness of items within a cluster, i.e. we can use it to check how close is a word to the other word !
----
- It is based on the orientation of the word rather than its magnitude, i.e. cos(theta) is calculated based on the vectors derived from the text itself. Ex:
----
- **text1** = "Vladimir Antonio Frometa Garo" and **text2** ="Vladimir Antonio F Garo"**
----
- Now the similarity between text1 and text2 = 0.75
----
- **cos(theta) = v1.v2/(||v1||.||v2||)**
----
- where, v1 and v2 are vectors derived from text1 and text2
----
- and ||x|| means norm of vector x.
----
- So, here **v1** = [1 1 1 1] and **v2** = [1 1 1 0]
----
- thus, **Similarity** = cos(theta) = 0.75
----
- and a **threshold** is set by analysing the facts to capture similar words.
-----------------------------------------------------
**Files to Run**
================
1)Open Terminal and run file with name 'deduplication.py'
------------
**Output:**
-----------
- On terminal deduplicated records will be showed !
- **'output.csv'** will be generated that will contain all the deduplicated records!
-----------
