from main import parse, train
from src.model import WBNCF

if __name__=="__main__":
    args = parse(print_help=True)
    args.n_splits = 10
    args.split_mode = 'global'
    args.dataset_name = "Fdataset"
    args.lr = 5e-4
    args.dropout = 0.5
    args.disease_neighbor_num = 5
    args.drug_neighbor_num = 5
    args.disease_feature_topk = 20
    args.drug_feature_topk = 20
    args.embedding_dim = 64
    args.neighbor_embedding_dim = 64
    args.hidden_dims = (64, 32)
    args.epochs = 64
    args.seed = 72
    args.train_fill_unknown = False


    args.alpha = 0.5
    args.lamda = 0.8
    args.gamma = 1.2

    train(args, WBNCF)

