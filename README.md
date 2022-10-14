# Phylogenetictree
### Introduction
- Phylogenetic trees illustrate the evolutionary relationships among groups of organisms, or among a family of related nucleic acid or protein sequences.

### Building Methods
- The most popular methods are:

	1- Unweighted Pair Group Method with Arithmetic mean (UPGMA).
	
  2- Neighbor Joining method (NJ).

### Model
- Code is implemented by using UPGMA.

- UPGMA is originally developed for numerical taxonomy in 1958 by Sokal and Michener.

- UPGMA is a simplest algorithm for tree construction, so it's fast!

### How to construct a tree with UPGMA?
1- Prepare a distance matrix.

2- Cluster a pair of leaves (taxa) by shortest distance.

3- Recalculate a new average distance with the new cluster and other taxa, and make a new distance matrix.

4- Repeat step 2 and step 3 until there are only two clusters.
