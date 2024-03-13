from pyserini.search.lucene import LuceneSearcher

class CustomLuceneSearcher(LuceneSearcher):  # 繼承 LuceneSearcher

    def set_jm(self, lambda_para):
        from jnius import autoclass

        similarity = autoclass("org.apache.lucene.search.similarities.LMJelinekMercerSimilarity")(lambda_para)
        self.object.similarity = similarity

        IndexSearcher = autoclass("org.apache.lucene.search.IndexSearcher")
        self.object.searcher = IndexSearcher(self.object.reader)
        self.object.searcher.setSimilarity(self.object.similarity)
