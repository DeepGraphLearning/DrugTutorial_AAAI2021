---
layout: default
permalink: wikidata5m
title: Wikidata5m
image: /assets/images/wikidata5m.jpg
papers:
  - title: "KEPLER: A Unified Model for Knowledge Embedding and Pre-trained Language Representation"
    authors: [Xiaozhi Wang, Tianyu Gao, Zhaocheng Zhu, Zhiyuan Liu, Juanzi Li, Jian Tang]
    conference: TACL 2020
    links:
      arXiv: https://arxiv.org/pdf/1911.06136.pdf
      BibTeX: /bibtex/kepler.txt
---

Info
----
Wikidata5m is a million-scale knowledge graph dataset with aligned corpus. This dataset integrates the [Wikidata] knowledge graph and [Wikipedia] pages. Each entity in Wikidata5m is described by a corresponding Wikipedia page, which enables the evaluation of link prediction over unseen entities.

The dataset is distributed as a knowledge graph, a corpus, and aliases. We provide both transductive and inductive data splits used in the [original paper].

| Setting      |       | #Entity    | #Relation | #Triplet   |
|--------------|-------|------------|-----------|------------|
| Transductive | Train | 4,594,485  | 822       | 20,614,279 |
|              | Valid | 4,594,485  | 822       | 5,163      |
|              | Test  | 4,594,485  | 822       | 5,133      |
|--------------|-------|------------|-----------|------------|
| Inductive    | Train | 4,579,609  | 822       | 20,496,514 |
|              | Valid | 7,374      | 199       | 6,699      |
|              | Test  | 7,475      | 201       | 6,894      |

[Wikidata]: https://www.wikidata.org
[Wikipedia]: https://www.wikipedia.org/
[original paper]: https://arxiv.org/pdf/1911.06136.pdf

Data
----
- Knowledge graph: [Transductive split], 160 MB. [Inductive split], 160 MB. [Raw], 168 MB.
- [Corpus], 991 MB.
- [Entity & relation aliases], 188 MB.

For raw knowledge graph, it may also contain entities that do not have corresponding Wikipedia pages.

[Transductive split]: https://www.dropbox.com/s/6sbhm0rwo4l73jq/wikidata5m_transductive.tar.gz?dl=1
[Inductive split]: https://www.dropbox.com/s/csed3cgal3m7rzo/wikidata5m_inductive.tar.gz?dl=1
[Raw]: https://www.dropbox.com/s/563omb11cxaqr83/wikidata5m_all_triplet.txt.gz?dl=1
[Corpus]: https://www.dropbox.com/s/7jp4ib8zo3i6m10/wikidata5m_text.txt.gz?dl=1
[Entity & relation aliases]: https://www.dropbox.com/s/lnbhc8yuhit4wm5/wikidata5m_alias.tar.gz?dl=1

Format
------
Wikidata5m follows the identifier system used in Wikidata. Each entity and relation is identified by a unique ID. Entities are prefixed by `Q`, while relations are prefixed by `P`.

### Knowledge Graph
The knowledge graph is stored in the triplet list format. For example, the following line corresponds to *<Donald Trump, position held, President of the United States>*.
```
Q22686	P39	Q11696
```

### Corpus
Each line in the corpus is a document, indexed by entity ID. The following line shows the description for *Donald Trump*.
```
Q22686	Donald John Trump (born June 14, 1946) is the 45th and current president of the United States ...
```

### Alias
Each line lists the alias for an entity or relation. The following line shows the aliases of *Donald Trump*.
```
Q22686  donnie trump	45th president of the united states     Donald John Trump ...
```

Publications
------------
{% include publication papers=page.papers %}