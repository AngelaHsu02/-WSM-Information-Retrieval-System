#./clean.sh


#############################################################################
# We first convert WT2G files into the jsonl format required by pyserini.   #
# No need this step when Using TrecwebCollection instead of JsonCollection. #
#############################################################################
# python3 codes/convert_wt2g_to_jsonl.py


##################################################################
# Secondly, we can build index for our WT2G corpus(247491 docs). #
# Use TrecwebCollection to build WT2G corpus(246772).            #
##################################################################
# ./codes/build_index.sh
./codes/build_trecweb_index.sh

##########################################################
# Then, search and store result in the trec_eval format. #
##########################################################
#python3 ./codes/main.py --query ../data/topics.401_440.txt --method bm25 --output ./runs/bm25_401_440.run
#python3 ./codes/main.py --query ../data/topics.401_440.txt --method mle --output ./runs/mle_401_440.run
#python3 ./codes/main.py --query ../data/topics.401_440.txt --method jm --output ./runs/jm_401_440.run
#python3 ./codes/main.py --query ../data/topics.401_440.txt --method bm25 --output ./runs/bm25nostem_401_440.run
#python3 ./codes/main.py --query ../data/topics.401_440.txt --method mle --output ./runs/mlenostem_401_440.run
#python3 ./codes/main.py --query ../data/topics.401_440.txt --method jm --output ./runs/jmnostem_401_440.run

python3 ./codes/main.py --query ../data/topics.441_450.txt --method bm25 --output ./runs/bm25_441_450.run
#python3 ./codes/main.py --query ../data/topics.441_450.txt --method mle --output ./runs/mle_441_450.run
#python3 ./codes/main.py --query ../data/topics.441_450.txt --method jm --output ./runs/jm_441_450.run


##############################
# Lastly, do the evaluation. #
##############################
#echo "BM25 result on 40 queries" #perl trec_eval.pl [-q] ../data/qrels.401_440.txt runs/bm25_401_440.run
#perl trec_eval.pl ../data/qrels.401_440.txt runs/bm25_401_440.run
#perl trec_eval.pl ../data/qrels.401_440.txt runs/mle_401_440.run
#perl trec_eval.pl ../data/qrels.401_440.txt runs/jm_401_440.run
#perl trec_eval.pl ../data/qrels.401_440.txt runs/bm25nostem_401_440.run
#perl trec_eval.pl ../data/qrels.401_440.txt runs/mlenostem_401_440.run
#perl trec_eval.pl ../data/qrels.401_440.txt runs/jmnostem_401_440.run


perl trec_eval.pl ../data/qrels.441_450.txt runs/bm25_441_450.run
#perl trec_eval.pl ../data/qrels.441_450.txt runs/mle_441_450.run
#perl trec_eval.pl ../data/qrels.441_450.txt runs/jm_441_450.run


#perl trec_eval.pl ../data/qrels.441_450.txt runs/learn_441_450.run
