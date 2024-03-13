#with stemming
python3 -m pyserini.index.lucene \
  --collection TrecwebCollection \
  --input ../data/WT2G \
  --index indexes/collection \
  --generator DefaultLuceneDocumentGenerator \
  --threads 16 \
  --storePositions --storeDocvectors --storeRaw \
  --optimize

#without stemming
#python3 -m pyserini.index.lucene \
#  --collection TrecwebCollection \
#  --input ../data/WT2G \
#  --index indexes/collection \
#  --generator DefaultLuceneDocumentGenerator \
#  --threads 16 \
#  --storePositions --storeDocvectors --storeRaw \
#  --optimize \
#  --stemmer none


