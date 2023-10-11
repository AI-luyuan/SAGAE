# SAGAE

SAGAE is a graph autoencoder model based on self-attention feature fusion, designed for predicting the association between drugs and diseases. What sets SAGAE apart is its use of self-attention mechanisms, which enhance the mutual understanding between candidate drugs and disease features. This addresses a limitation in current graph neural network methods, which primarily focus on node information interactions within the graph, often neglecting the need for personalized and context-aware learning for candidate drugs and diseases.

## Environment Requirement
The code has been tested under Python 3.8.10. The required packages are:
- numpy == 1.21.1
- pandas == 1.4.3
- scipy == 1.10.1
- pytorch == 2.0.1
- pytorch-lightning==1.9.0
- scikit-learn == 0.23.2

We will actively maintain the code on Github. People with implementation problems can open an issue via Github online. 

## Example to Run the Code

```python demo.py```

## List of Folders
### data
We provide three processed datasets, Fdataset, Cdataset and LRSSL. 
The Fdataset dataset contains 593 drug and 313 diseases, with 1933 associations between them.
The Cdataset dataset contains 663 drug and 409 diseases, with 2532 associations between them.
The LRSSL dataset contains 763 drug and 681 diseases, with 3051 associations between them.


## List of Files
dataset.py: data preparation;\
bgnn.py: construct GNN layers;\
model.py: construct SAGAE model;\
main.py: main file;\
demo.py: train SAGAE model.

## License
MIT LICENSE

To use the code, please cite the paper entitled ***SAGAE: Drug-Disease Association Prediction Based on Self-Attention Feature Fusion and Graph Autoencoder***.

