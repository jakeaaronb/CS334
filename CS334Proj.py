#these imports are used for tabulation
# and ploting/graphing data

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#This portion here are the installed packages for BBN
from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController

#This sets display
pd.options.display.max_columns = 50
#reads in the weatherData file
df = pd.read_csv('weatherData.csv', encoding='utf-8')

#If we know it will not rain, then we just have
#it set to '==false' so we can remove it
df = df[pd.isnull(df['RainTomorrow']) == False]
#If for some reason data is missing, this fills in N/A values
df = df.fillna(df.mean())
#Variable for the model
df['WindGustSpeedCat'] = df['WindGustSpeed'].apply(lambda x: '0.<=40' if x <= 40 else
'1.40-50' if 40 < x <= 50 else '2.>50')
df['Humidity9amCat'] = df['Humidity9am'].apply(lambda x: '1.>60' if x > 60 else '0.<=60')
df['Humidity3pmCat'] = df['Humidity3pm'].apply(lambda x: '1.>60' if x > 60 else '0.<=60')
#present the data
df

#Nodes created here with input values set on variables
Humid9am = BbnNode(Variable(0, 'Humid9am', ['<=60', '>60']), [0.30658, 0.69342])
Humid3pm = BbnNode(Variable(1, 'Humid3pm', ['<=60', '>60']), [0.92827, 0.07173,
                                                            0.55760, 0.44240])
Wind = BbnNode(Variable(2, 'Wind', ['<=40', '40-50', '>50']), [0.58660, 0.24040, 0.17300])
RainTomorrow = BbnNode(Variable(3, 'RainTomorrow', ['No', 'Yes']), [0.92314, 0.07686,
                                                                    0.89072, 0.10928,
                                                                    0.76008, 0.23992,
                                                                    0.64250, 0.35750,
                                                                    0.49168, 0.50832,
                                                                    0.32182, 0.67818])

#)First we create nodes with probabilities.
#the Normalized frequencies would be common practice, but this can also be done using actual frequencies. That is why the
#BbnNode(Var, 0, 'dataPoint',['<= n', '>n']}) was used in this case. (This data will be discretied for submission.)


#Def probs function largely helps with the calculation of the probability distribution which is used to go in to the Bayesian network Node. This handles up to two parent nodes (Hum9am, Wind).
def probs(data, child, parent1=None, parent2=None):
    if parent1 == None:

        prob = pd.crosstab(data[child], 'Empty', margins=False, normalize='columns').sort_index().to_numpy().reshape(
            -1).tolist()
    elif parent1 != None:

        if parent2 == None:

            prob = pd.crosstab(data[parent1], data[child], margins=False,
                               normalize='index').sort_index().to_numpy().reshape(-1).tolist()
        else:

            prob = pd.crosstab([data[parent1], data[parent2]], data[child], margins=False,
                               normalize='index').sort_index().to_numpy().reshape(-1).tolist()
    else:
        print("Error in Probability Frequency Calculations")
    return prob

#Following this, each probability is calculated:

#For Child nodes that are for instance "Hum3pmCat" with some parent node let's say "Hum9amCat", we need to be able to input probabilities for each combination of child and parent nodes. The DefProbs function is created so we don't have to calculate each frequency one-by-one.
Humid9am = BbnNode(Variable(0, 'Humid9am', ['<=60', '>60']), probs(df, child='Humidity9amCat'))
Humid3pm = BbnNode(Variable(1, 'Humid3pm', ['<=60', '>60']), probs(df, child='Humidity3pmCat', parent1='Humidity9amCat'))
Wind = BbnNode(Variable(2, 'Wind', ['<=40', '40-50', '>50']), probs(df, child='WindGustSpeedCat'))
RainTomorrow = BbnNode(Variable(3, 'RainTomorrow', ['No', 'Yes']),
                       probs(df, child='RainTomorrow', parent1='Humidity3pmCat', parent2='WindGustSpeedCat'))

#adding in each node to they bayesian network
bbn = Bbn() \
    .add_node(Humid9am) \
    .add_node(Humid3pm) \
    .add_node(Wind) \
    .add_node(RainTomorrow) \
    .add_edge(Edge(Humid9am, Humid3pm, EdgeType.DIRECTED)) \
    .add_edge(Edge(Humid3pm, RainTomorrow, EdgeType.DIRECTED)) \
    .add_edge(Edge(Wind, RainTomorrow, EdgeType.DIRECTED))

#Bayesian Network -> Tree
join_tree = InferenceController.apply(bbn)

# Position of the Nodes
pos = {0: (-1, 2), 1: (-1, 0.5), 2: (1, 0.5), 3: (0, -1)}

#This is where all the details of node/edge design are created
options = {
    "font_size": 12,
    "node_size": 9000,
    "node_color": "white",
    "edgecolors": "black",
    "edge_color": "black",
    "linewidths": 5,
    "width": 5, }

n, d = bbn.to_nx_graph()
nx.draw(n, with_labels=True, labels=d, pos=pos, **options)

ax = plt.gca()
ax.margins(0.10)
plt.axis("off")
plt.show()


# The defPrintProbs is the function designed to print any and all marginal probabilities. Basically, we want to plot probabilities for each node without passing any additional information to the graph.
# The function here is used to avoid having to retype any future code.
# This way we can also allow for multiple prints of information.

def print_probs():
    for node in join_tree.get_bbn_nodes():
        potential = join_tree.get_bbn_potential(node)
        print("Node:", node)
        print("Values:")
        print(potential)
        print('----------------')


print_probs()

#evidence is added in order to calculate prob distribution
def evidence(ev, nod, cat, val):
    ev = EvidenceBuilder() \
        .with_node(join_tree.get_bbn_node_by_name(nod)) \
        .with_evidence(cat, val) \
        .build()
    join_tree.set_observation(ev)


evidence('ev1', 'Humid9am', '>60', 1.0)

print_probs()

evidence('ev1', 'Humid3pm', '>60', 1.0)
evidence('ev2', 'Wind', '>50', 1.0)
print_probs()

