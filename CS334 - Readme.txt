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
Kaggle.com //Excel Data
towardsscience.co // Portions of Source code
geeksforgeeks.com // Explanation of data
tutorialspoint.com // Explanation of data
Sciencedirect.com // explanation of dat and source code
Informational-Statistical Data Mining - Warehouse Integration with examples of Oracle basics (Bon K. Sy)// Knowledge and explanation of Bayesian Networks
Bayesian Networks (Michal Horný) // Some background information of bayesian networks
