A Bayesian network is a sirected acyclic graph. Each edge corresponds to some conditional depencancy. In addition, each node corresponds to some random variable.

Now that we know that a Bayesian network is a directed acyclic graph, there is one more important aspect to address. This is that the conditional probability distribution of a node is defined for every possible outcome of the preceding node(s). i.e. P(cause|evidence).

In this case we test several aspects of a persons cardiovascular health and address where certain aspects could indicate that there is a risk of heart disease.

Sample output: 
  age  sex  cp  trestbps  chol  ...  oldpeak  slope  ca  thal  heartdisease
0   63    1   1       145   233  ...      2.3      3   0     6             0
1   67    1   4       160   286  ...      1.5      2   3     3             2
2   67    1   4       120   229  ...      2.6      2   2     7             1
3   37    1   3       130   250  ...      3.5      3   0     3             0
4   41    0   2       130   204  ...      1.4      1   0     3             0

 
+-----------------+---------------------+
| heartdisease    |   phi(heartdisease) |
+=================+=====================+
| heartdisease(0) |              0.1012 |
+-----------------+---------------------+
| heartdisease(1) |              0.0000 |
+-----------------+---------------------+
| heartdisease(2) |              0.2392 |
+-----------------+---------------------+
| heartdisease(3) |              0.2015 |
+-----------------+---------------------+
| heartdisease(4) |              0.4581 |
+-----------------+---------------------+

 2. Probability of Heartdisease given evidence= cp 
+-----------------+---------------------+
| heartdisease    |   phi(heartdisease) |
+=================+=====================+
| heartdisease(0) |              0.3610 |
+-----------------+---------------------+
| heartdisease(1) |              0.2159 |
+-----------------+---------------------+
| heartdisease(2) |              0.1373 |
+-----------------+---------------------+
| heartdisease(3) |              0.1537 |
+-----------------+---------------------+
| heartdisease(4) |              0.1321 |
+-----------------+---------------------+
Finding Elimination Order: : 100%|██████████| 3/3 [00:00<00:00, 2998.07it/s]
Eliminating: sex: 100%|██████████| 3/3 [00:00<00:00, 750.59it/s]



Sources:
edureka.co
towardsdatascience.com
analyticsindiamag.com
vtpulse.com