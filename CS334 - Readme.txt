This project is focused on Bayesian Networks that use weather data in order to determine relationships between weather and the probability of a weather event occuring.


First we create nodes with probabilities.
the Normalized frequencies would be common practice, but this can also be done using actual frequencies. That is why the 
BbnNode(Var, 0, 'dataPoint',['<= n', '>n']}) was used in this case. (This data will be discretied for submission.)

For Child nodes that are for instance "Hum3pmCat" with some parent node let's say "Hum9amCat", we need to be able to input probabilities for each combination of child and parent nodes. The DefProbs function is created so we don't have to calculate each frequency one-by-one.

Def probs function largely helps with the calculation of the probability distribution which is used to go in to the Bayesian network Node. This handles up to two parent nodes (Hum9am, Wind).

Following that, each probability is calculated:

The defPrintProbs is the function designed to print any and all marginal probabilities. Basically, we want to plot probabilities for each node without passing any additional information to the graph. The function here is used to avoid having to retype any future code. This way we can also allow for multiple prints of information.

Code successfully runs and prints out a tree. 
Successfully calculates probability of BBN.


Sources used:
https://www.kaggle.com/jsphyg/weather-dataset-rattle-package //Excel Dataset to use for evidence in bayesian network.
https://towarddatascience.com/bbn-bayesian-belief-networks-how-to-build-them-effectively-in-python-6b793435bba// Portions of Source code
https://www.geeksforgeeks.org/basic-understanding-of-bayesian-belief-networks/// Explanation of data to understand concepts and implementation
https://www.tutorialspoint.com/data_mining/dm_bayesian_classification.htm // Explanation of data to further understand how bayesian networks work and how to implement.
Informational-Statistical Data Mining - Warehouse Integration with examples of Oracle basics (Bon K. Sy)// Knowledge and explanation of Bayesian Networks
Bayesian Networks (Michal Horný) // Some background information of bayesian networks
https://py-bbn.readthedocs.io/index.html // Python packages
https://pandas.pydata.org/docs/ // Python packages
Networkx import - Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, “Exploring network structure, dynamics, and function using NetworkX”, in Proceedings of the 7th Python in Science Conference (SciPy2008), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008
Matlib plot - https://matplotlib.org/stable/users/index.html
https://gist.github.com/SolClover/4dc6be814663bbcd6274069727754b29 - Source code
https://gist.github.com/SolClover/183b3bc2d51881138177a2ed80c00fdc - Source code
https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html - For visual pd
https://gist.github.com/SolClover/52a69b8ceeb77240ea51d6a61a1fffed - Source code for defPrintProbs
