import argparse
from search import *
from util import *
from pyserini.search.lucene import LuceneSearcher
from pyserini.index.lucene import IndexReader
from pyserini.search import SimpleSearcher
from set_jm import CustomLuceneSearcher

# Initialize from a pre-built index:
#index_reader = IndexReader.from_prebuilt_index('collection')
# Initialize from an index path:
index_reader = IndexReader('indexes/collection')
stats = index_reader.stats()
print(stats)




if __name__ == '__main__':
    parser = argparse.ArgumentParser() #可以在運行腳本時設定參數
    parser.add_argument("--index", default="indexes/collection", type=str)
    parser.add_argument("--query", default="../data/topics.401_440.txt", type=str)
    parser.add_argument("--method", default="bm25", type=str)
    parser.add_argument("--k", default=1000, type=int)
    parser.add_argument("--output", default='runs/bm25_401_440.run', type=str)
    args = parser.parse_args()
    #print(args)

    #corpus = read_topic(args.query)

    #if args.method == "MLE":
    #    mle = MLE("indexes/collection", args.index)
    #    query = read_topic(args.query)
    #    mle.search_with_mle(query, k=args.k, output_file=args.output)

    #searcher = LuceneSearcher(args.index)
    if args.method == "bm25":
        searcher = LuceneSearcher(args.index)
        searcher.set_bm25(k1=2, b=0.75)
    if args.method == "mle":
        searcher = LuceneSearcher(args.index)        
        searcher.set_qld(mu=stats["total_terms"] / stats["unique_terms"])

    if args.method == "jm":
        searcher = CustomLuceneSearcher(args.index)
        searcher.set_jm(lambda_para=0.5)



    query = read_topic(args.query)
    #print(query)  # {'401': 'foreign minorities, Germany '}
    search(searcher, query, args) #eval

