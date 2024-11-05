---
source: "blog"
title: "anitagraser.com: GeoAI: key developments & insights"
image: "geoai-key-developments-insights."
date: "2024-11-03"
link: "https://anitagraser.com/2024/11/04/geoai-key-developments-insights/"
draft: "true"
showcase: "planet"
---

<p>It&#8217;s been a while since my post on <a href="https://anitagraser.com/2019/05/01/movement-data-in-gis-and-the-ai-hype/">geo and the AI hype in 2019</a>. Back then, I didn&#8217;t use the term &#8220;GeoAI&#8221;, even though it has certainly been around for a while (including, e.g., with <a href="https://dl.acm.org/doi/10.1145/3377000.3377002">dedicated SIGSPATIAL workshops since 2017</a>).</p>



<p><em>GeoAI isn&#8217;t one single thing. It&#8217;s an umbrella term, including: &#8220;AI for Geo&#8221; (using AI methods in Geo, e.g. deep learning for object recognition in remote sensing images) and &#8220;Geo for AI&#8221; (integrating geographic concepts into AI models, e.g. by building spatially explicit models). </em><a href="https://mars.gmu.edu/items/2f2639c0-ef63-45cc-8d4e-86fcf8fb4475">[Zhang 2020]</a> <a href="https://doi.org/10.5311/JOSIS.2024.29.349">[Li et al. 2024]</a></p>



<p>Today&#8217;s post is a collection of key GeoAI developments I&#8217;m aware of. If I missed anything you are excited about, please let me know here in the comments or over on <a href="https://fosstodon.org/@underdarkGIS">Mastodon</a>. </p>



<h2 class="wp-block-heading">Background</h2>



<p>A week ago, I had the pleasure to attend a <a href="https://geographie.univie.ac.at/arbeitsgruppen/kartographie-und-geoinformation/events/sociotechnical-foundations-of-geoai-and-spatial-data-science/">&#8220;Specialist Meeting&#8221; on GeoAI</a> here in Vienna, meeting over 40 researchers from around the world, from Master students to professor emeritus. Huge props to Jano (Prof. Krzysztof Janowicz) and his team at Uni Wien for bringing this awesome group of people together. </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-9258" height="665" src="https://anitagraser.com/wp-content/uploads/2024/11/1730111597802-edited.jpeg?w=1024" width="1024" /></figure>



<h2 class="wp-block-heading">The elephant in the room: LLMs</h2>



<p>Unsurprisingly, LLMs and the claims they make about geography are a mayor issue due to the mistakes they make and the biases behind them. An infamous example is AI&#8217;s issue with understanding topology: </p>



<figure class="wp-block-image size-large"><a href="https://www.researchgate.net/figure/Distance-between-Ukraine-and-Russia-according-to-Google-Search-and-Chat-GPT-Note-that_fig1_370001256"><img alt="" class="wp-image-9261" height="221" src="https://anitagraser.com/wp-content/uploads/2024/11/image.png?w=850" width="850" /></a><figcaption class="wp-element-caption">Image source: Janowicz, K. (2023). Philosophical Foundations of GeoAI: Exploring Sustainability, Diversity, and Bias in GeoAI and Spatial Data Science. <em>arXiv e-prints</em>, arXiv-2304.</figcaption></figure>



<p>Even if recent versions of ChatGPT (such as GTP 4o) do a better job with this specific example, this doesn&#8217;t make their answers reliable. So between the trustworthiness, reproducibility, explainability, and sustainability issues &#8230; LLMs have a long way to go. And it&#8217;s not clear whether they are going in the right direction right now. </p>



<h2 class="wp-block-heading">Geospatial foundation models</h2>



<p>Prithvi, a model developed by <a href="https://arxiv.org/abs/2310.18660">NASA, IBM, et al.</a> in 2023, is one of the first geospatial foundation models. Like much of GeoAI, Prithvi deals with remote sensing data. Specifically, it is trained on Landsat and Sentinel-2 (HLS) imagery, with applications in flood mapping and wildfire prediction. And maybe best of all: the model is open-source and <a href="https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M">publicly available</a>.</p>



<h2 class="wp-block-heading">Spatiotemporal machine learning model specifications</h2>



<p>In the general AI community, <a href="https://modelcards.withgoogle.com/about">model cards</a> have become a common way to share information about models. However, identifying the right model for spatiotemporal tasks is hard since there are no standardized descriptions in existing model catalogs (e.g. Hugging Face, DLHub or MLFlow). To address this issue, <a href="https://dl.acm.org/doi/abs/10.1145/3681769.3698586">[Charette-Migneault et al. 2024]</a> have proposed the Machine Learning Model (MLM) extension for the SpatioTemporal Asset Catalogs (STAC). But, yet again, this development is targeting models trained with remote sensing imagery.</p>



<p>Similarly, the <a href="https://docs.ogc.org/is/23-008r3/23-008r3.html" rel="noreferrer noopener" target="_blank">OGC Training Data Markup Language for Artificial Intelligence (TrainingDML-AI)</a> and its ISO equivalent are limited to EO as well &#8230; </p>



<h2 class="wp-block-heading">Spatial knowledge graphs</h2>



<p>For those among us working mostly with vector data, the <a href="https://knowwheregraph.org/">KnowWhereGraph</a> is an interesting development. It&#8217;s the first geo-enriched knowledge graph <a href="https://onlinelibrary.wiley.com/doi/10.1002/aaai.12043">[Janowicz et al. 2022]</a> that helps answer geospatial questions by integrating a variety of spatial datasets through hierarchical grids, standard region boundaries and appropriate ontology and knowledge graph schema development. However, so far, the KnowWhereGraph is mostly limited to the United States. </p>



<h2 class="wp-block-heading">Explainable AI (XAI) and geo</h2>



<p>While answers from knowledge graphs are intrinsically explainable, many other (Geo)AI solutions are built on AI approaches that result in black box models.</p>



<p>Graph neural networks (GNNs) have become very popular in GeoAI (including in urban analytics and mobility <a href="https://arxiv.org/abs/2307.08461">[Jalali et al. 2023] </a><a href="https://journals.sagepub.com/doi/10.1177/23998083231204689">[Liu et al. 2024]</a>) but their black box nature limits their practical usefulness in domains where transparency and trustworthiness are crucial. To offer insights into how model predictions are made, <a href="https://journals.sagepub.com/doi/10.1177/23998083231204689">[Liu et al. 2024]</a> propose a spatially explicit GeoAI-based method that combines a graph convolutional network and a graph-based XAI method, called GNNExplainer to explore the correlation between urban objects.</p>



<h2 class="wp-block-heading">Reproducibility et al. </h2>



<p>The AI hype in geo is still going strong. Journals are being flooded with paper submissions and good reviewers are hard to come by. In many geo-related venues, it is still acceptable to present an AI paper without making code or model available. (We recently discussed this issue for mobility AI specifically <a href="https://doi.org/10.1007/s10707-024-00518-8">[Graser et al. 2024]</a>.)</p>



<p>I&#8217;m convinced we can and should do better: quality over quantity, moving steadily, building and fixing things. </p>



<h2 class="wp-block-heading">References</h2>



<ul class="wp-block-list">
<li><a href="https://dl.acm.org/doi/10.1145/3681769.3698586">Charette-Migneault, F., Avery, R., Pondi, B., Omojola, J., Vaccari, S., Membari, P., &#8230; &amp; Sundwall, J. (2024). Machine Learning Model Specification for Cataloging Spatio-Temporal Models. In <em>Proceedings of the 3rd ACM SIGSPATIAL International Workshop on Searching and Mining Large Collections of Geospatial Data</em> (pp. 36-39).</a></li>



<li><a href="https://link.springer.com/article/10.1007/s10707-024-00518-8?utm_source=rct_congratemailt&amp;utm_medium=email&amp;utm_campaign=oa_20240528&amp;utm_content=10.1007/s10707-024-00518-8">Graser, A., Jalali, A., Lampert, J., Weißenfeld, A., &amp; Janowicz, K. (2024). MobilityDL: a review of deep learning from trajectory data. GeoInformatica, 1-33.</a> </li>



<li><a href="https://arxiv.org/abs/2310.18660">Jakubik, J., Roy, S., Phillips, C., Fraccaro, P., Godwin, D., Zadrozny, B., &#8230; &amp; Edwards, B. (2023) Foundation models for generalist geospatial artificial intelligence. <em>arXiv preprint arXiv:2310.18660</em>.</a></li>



<li><a href="https://arxiv.org/abs/2307.08461">Jalali, A., Graser, A., &amp; Heistracher, C. (2023). Towards eXplainable AI for Mobility Data Science.&nbsp;<em>arXiv preprint arXiv:2307.08461</em>.</a></li>



<li><a href="https://onlinelibrary.wiley.com/doi/10.1002/aaai.12043">Janowicz, K., Hitzler, P., Li, W., Rehberger, D., Schildhauer, M., Zhu, R., &#8230; &amp; Currier, K. (2022). Know, Know Where, KnowWhereGraph: A densely connected, cross-domain knowledge graph and geo-enrichment service stack for applications in environmental intelligence. <em>AI Magazine</em>, <em>43</em>(1), 30-39.</a></li>



<li><a href="https://doi.org/10.5311/JOSIS.2024.29.349">Li, W., Arundel, S., Gao, S., Goodchild, M., Hu, Y., Wang, S., &amp; Zipf, A. (2024). GeoAI for Science and the Science of GeoAI. <em>Journal of Spatial Information Science</em>, (29), 1-17.</a></li>



<li><a href="https://journals.sagepub.com/doi/10.1177/23998083231204689">Liu, P., Zhang, Y., &amp; Biljecki, F. (2024). Explainable spatially explicit geospatial artificial intelligence in urban analytics. <em>Environment and Planning B: Urban Analytics and City Science</em>, <em>51</em>(5), 1104-1123.</a></li>



<li><a href="https://docs.ogc.org/is/23-008r3/23-008r3.html" rel="noreferrer noopener" target="_blank">OGC Training Data Markup Language for Artificial Intelligence (TrainingDML-AI) Part 1: Conceptual Model Standard (2023)</a> </li>



<li><a href="https://mars.gmu.edu/items/2f2639c0-ef63-45cc-8d4e-86fcf8fb4475">Zhang, L. (2020). <em>Explainable Machine Learning for Activity Modeling in GeoA</em>I. Doctoral dissertation, George Mason University.</a></li>
</ul>
