---
permalink: /
title: "Wei-Yao Wang's Homepage"
author_profile: true
hide_title: true
redirect_from: 
  - /about/
  - /about.html
---

<span class="anchor" id="about-me"></span>

My name is Wei-Yao Wang. I am a research scientist in the **[Creative AI Lab](https://sony.github.io/creativeai/)** at Sony, working on **interactive multimodal models for content creation, spanning omni‑modal LLMs/embedders, video generation/editing, and agentic understanding**. I received my Ph.D. and BS degrees from National Yang Ming Chiao Tung University and National Chiao Tung University in Taiwan respectively, advised by [Prof. Wen-Chih Peng](https://sites.google.com/site/wcpeng/wcpeng). During my academic journey, I served as a visiting researcher at the ScAi lab advised by [Prof. Wei Wang](https://web.cs.ucla.edu/~weiwang/) at the University of California, Los Angeles. I was a research intern at [Document AI](https://www.microsoft.com/en-us/research/project/document-ai/overview/) in Microsoft in Seattle and Microsoft AI R&D Center in Taipei advised by [Paul Hsu](https://www.microsoft.com/en-us/research/people/paulhsu/), working on **low-resource field extractions from multi-modal documents with LLMs**.

My research intersts include Interactive Omnimodal Models; LLM Agents; LLM Alignment; Foundation Models; Natural Language Processing; Sport Science; and Representation Learning; which has been published more than 40+ papers in international journals and major peer-reviewed conference proceedings (e.g., ICLR, NeurPS, ICML, CVPR, KDD, AAAI, ACL, EMNLP), including multiple best paper awards. I serve on the program committees of international conferences including ICLR, ICCV, AAAI, ACL ARR, KDD, IJCAI, CIKM, and PAKDD and workshop organizers ([GenProCC@NeurIPS-25](https://genprocc.github.io/), [IT4PSS@IJCAI23-24](https://wasn.csie.ncu.edu.tw/workshop/IT4PSS2024.html), [SocialNLP@NAACL-22&TheWebConf-22](https://sites.google.com/view/socialnlp2022/)).

I am also open to research collaboration. Please drop me an email if you are interested in.

# Research Experience

- [Sep. 2024 - Present] Research Scientist, [Creative AI Lab](https://sony.github.io/creativeai/), Sony Group Corporation
- [Jul. 2020 - Mar. 2024] Ph.D. Researcher, [Advanced Database System Laboratory](https://lab-adsl-website.vercel.app/), NYCU
- [Mar. 2023 - Mar. 2024] Visiting Researcher, [Scalable Analytics Institute](https://scai.cs.ucla.edu/), UCLA
- [Sep. 2023 - Dec. 2023] Research Intern, Microsoft ([Document AI](https://www.microsoft.com/en-us/research/project/document-ai/overview/))
- [May 2022 - Nov. 2022] Research Intern, Microsoft AI R&D Center ([Document AI](https://www.microsoft.com/en-us/research/project/document-ai/overview/))
- [Jun. 2018 - Jun. 2022] Project Lead & Research Scientist, Precision Sport Science - Coach AI in Badminton ([project link](https://github.com/wywyWang/CoachAI-Projects))
- [Jul. 2018 - Jun. 2020] Database Administrator, NCTU CS Curriculum Assistant

# Education

- [Sep. 2020 - Mar. 2024] Ph.D. at Institute of Computer Science and Engineering, National Yang Ming Chiao Tung University (advisor: [Prof. Wen-Chih Peng](https://sites.google.com/site/wcpeng/wcpeng))
- [Mar. 2023 - Mar. 2024] Visiting Researcher in Scalable Analytics Institute, University of California, Los Angeles (advisor: [Prof. Wei Wang](https://web.cs.ucla.edu/~weiwang/))
- [Sep. 2016 - Jun. 2020] B.S. in Department of Computer Science, National Chiao Tung University

# Publications

<!-- Pass selected="false" to keep a paper out of Selected. Pass kind="workshop" for workshop papers (default is conference). Add fig="images/papers/name.png" to show a figure on expand. -->

<p class="paper-hint"><i>Click a paper to expand details. <sup>♠</sup> denotes papers I mentored.</i></p>

<p class="paper-tabs">
  <button type="button" class="paper-tab is-active" data-filter="selected">Selected</button>
  <button type="button" class="paper-tab" data-filter="conference">Journals and Conferences</button>
  <button type="button" class="paper-tab" data-filter="workshop">Workshops</button>
  <button type="button" class="paper-tab" data-filter="mentor">Mentor</button>
</p>

<div id="paper-list">

{% include paper.html selected="false" badge="Preprint" title="Neural Audio-Visual Chords: A Multimodal Framework for Temporally and Spatially Aligned Sound Generation from Visual Cues" authors="Christian Simon, Wei-Yao Wang, Dongseok Shim, Kazuki Shimada, Masato Ishii, Takashi Shibuya, Shusuke Takahashi, Yuki Mitsufuji" %}

{% include paper.html badge="Preprint" title="Omni-Interactive Universal Embedder" authors="Wei-Yao Wang, Kazuya Tateishi, Shuyang Cui, Christian Simon, Takashi Shibuya, Shusuke Takahashi, Yuki Mitsufuji" %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2510.15543">preprint</a>{% endcapture %}
{% include paper.html badge="EMNLP 2026" title="MCA: Modality Composition Awareness for Robust Composed Multimodal Retrieval" url="https://arxiv.org/abs/2510.15543" authors="Qiyu Wu, Shuyang Cui, Satoshi Hayakawa, Wei-Yao Wang, Hiromi Wakaki, Yuki Mitsufuji" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2510.15306v1">preprint</a>{% endcapture %}
{% include paper.html badge="KDD 2026" title="WebGen-V Bench: Structured Representation for Enhancing Visual Design in LLM-based Web Generation and Evaluation" url="https://arxiv.org/abs/2510.15306v1" authors="Kuang-Da Wang, Zhao Wang, Wei-Yao Wang♠, Yotaro Shimose, Shingo Takamatsu" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://icml.cc/virtual/2026/poster/62292">paper</a>{% endcapture %}
{% include paper.html badge="ICML 2026" title="Agentic Model Predictive Questioning Control in Visual Design" url="https://icml.cc/virtual/2026/poster/62292" authors="Kuang-Da Wang, Zhao Wang, Wei-Yao Wang♠, Yotaro Shimose, Jaechang Kim, Shingo Takamatsu" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2603.16423">paper</a>{% endcapture %}
{% include paper.html badge="ICML 2026" title="SF-Mamba: Rethinking State Space Model for Vision" url="https://arxiv.org/abs/2603.16423" authors="Masakazu Yoshimura, Teruaki Hayashi, Yuki Hoshino, Wei-Yao Wang, Takeshi Ohashi" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2503.02597">paper</a>{% endcapture %}
{% include paper.html badge="ICML 2026" title="Seeing is Understanding: Unlocking Causal Attention into Modality-Mutual Attention for Multimodal LLMs" url="https://arxiv.org/abs/2503.02597" authors="Wei-Yao Wang, Zhao Wang, Helen Suzuki, Yoshiyuki Kobayashi" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2509.00446">paper</a>{% endcapture %}
{% include paper.html badge="ACL 2026 Findings" title="NEWSAGENT: Benchmarking Multimodal Agents as Journalists with Real-World Newswriting Tasks" url="https://arxiv.org/abs/2509.00446" authors="Yen-Che Chien, Kuang-Da Wang, Wei-Yao Wang♠, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2502.11098">preprint</a>{% endcapture %}
{% include paper.html badge="IEEE TAI 2026" title="Talk Structurally, Act Hierarchically: A Collaborative Framework for LLM Multi-Agent Systems" url="https://arxiv.org/abs/2502.11098" authors="Zhao Wang, Sota Moriyama, Wei-Yao Wang, Briti Gangopadhyay, Shingo Takamatsu" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2602.20981">paper</a>{% endcapture %}
{% include paper.html badge="CVPR 2026" title="Echoes Over Time: Unlocking Length Generalization in Video-to-Audio Generation Models" url="https://arxiv.org/abs/2602.20981" authors="Christian Simon, Masato Ishii, Wei-Yao Wang, Koichi Saito, Akio Hayakawa, Dongseok Shim, Zhi Zhong, Shuyang Cui, Takashi Shibuya, Shusuke Takahashi, Yuki Mitsufuji" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2510.00523">preprint</a> <a class="paper-link-btn" href="https://sony.github.io/virtue/">website</a>{% endcapture %}
{% include paper.html badge="ICLR 2026" title="VIRTUE: Visual-Interactive Text-Image Universal Embedder" url="https://arxiv.org/abs/2510.00523" authors="Wei-Yao Wang, Kazuya Tateishi, Qiyu Wu, Shusuke Takahashi, Yuki Mitsufuji" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2506.07033">preprint</a>{% endcapture %}
{% include paper.html badge="WSDM 2026" title="Adapting to Evolving Data: Test-Time Expert Aggregation for Imbalanced Tabular Regression" url="https://arxiv.org/abs/2506.07033" authors="Yung-Chien Wang, Kuang-Da Wang, Wei-Yao Wang, Wen-Chih Peng" links=links %}

{% include paper.html selected="false" badge="ACL SRW 2025" award="Oral" title="Tree-of-Report: Table-to-Text Generation for Sports Game Reports with Tree-Structured Prompting" authors="Shang-Hsuan Chiang, Tsan-Tsung Yang, Kuang-Da Wang, Wei-Yao Wang, An-Zi Yen, Wen-Chih Peng" %}

{% capture links %}<a class="paper-link-btn" href="https://dl.acm.org/doi/10.1145/3719207">paper</a>{% endcapture %}
{% include paper.html badge="ACM TIST 2025" title="LLM4TS: Aligning Pre-Trained LLMs as Data-Efficient Time-Series Forecasters" url="https://dl.acm.org/doi/10.1145/3719207" authors="Ching Chang, Wei-Yao Wang, Wen-Chih Peng, Tien-Fu Chen" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2312.10942">preprint</a>{% endcapture %}
{% include paper.html selected="false" badge="PAKDD 2025" title="ShuttleSHAP: A Turn-Based Feature Attribution Approach for Analyzing Forecasting Models in Badminton" url="https://arxiv.org/abs/2312.10942" authors="Wei-Yao Wang, Wen-Chih Peng, Wei Wang, Philip Yu" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2412.10941v1">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="AAAI 2025" title="APAR: Modeling Irregular Target Functions in Tabular Regression via Arithmetic-Aware Pre-Training and Adaptive-Regularized Fine-Tuning" url="https://arxiv.org/abs/2412.10941v1" authors="Hong-Wei Wu, Wei-Yao Wang♠, Kuang-Da Wang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2402.01204">paper</a>{% endcapture %}
{% include paper.html badge="ACML 2024" title="A Survey on Self-Supervised Learning for Non-Sequential Tabular Data" url="https://arxiv.org/abs/2402.01204" authors="Wei-Yao Wang, Wei-Wei Du, Derek Xu, Wei Wang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2306.04090">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="CIKM 2024" title="Professional Basketball Player Behavior Synthesis via Planning with Diffusion" url="https://arxiv.org/abs/2306.04090" authors="Wei-Yao Wang*, Xiusi Chen*, Ziniu Hu, David Reynoso, Kun Jin, Mingyan Liu, P. Jeffrey Brantingham, Wei Wang" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2403.12406">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="ECML-PKDD 2024" title="Offline Imitation of Badminton Player Behavior via Experiential Contexts and Brownian Motion" url="https://arxiv.org/abs/2403.12406" authors="Kuang-Da Wang, Wei-Yao Wang♠, Ping-Chun Hsieh, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2306.15664">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="IJCAI Demo 2024" title="Benchmarking Stroke Forecasting with Stroke-Level Badminton Dataset" url="https://arxiv.org/abs/2306.15664" authors="Wei-Yao Wang, Wei-Wei Du, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2312.04142">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="ICDE 2024" title="TimeDRL: Disentangled Representation Learning for Multivariate Time-Series" url="https://arxiv.org/abs/2312.04142" authors="Ching Chang, Chiao-Tung Chan, Wei-Yao Wang, Wen-Chih Peng, Tien-Fu Chen" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2212.12190">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="PAKDD 2024" title="Look Around! A Neighbor Relation Graph Learning Framework for Real Estate Appraisal" url="https://arxiv.org/abs/2212.12190" authors="Chih-Chia Li, Wei-Yao Wang, Wei-Wei Du, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://aclanthology.org/2024.eacl-long.92/">paper</a>{% endcapture %}
{% include paper.html badge="EACL 2024" title="Style-News: Incorporating Stylized News Generation and Adversarial Verification for Neural Fake News Detection" url="https://aclanthology.org/2024.eacl-long.92/" authors="Wei-Yao Wang, Yu-Chieh Chang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://ojs.aaai.org/index.php/AAAI/article/view/27772">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="AAAI 2024" title="Root Cause Analysis In Microservice Using Neural Granger Causal Discovery" url="https://ojs.aaai.org/index.php/AAAI/article/view/27772" authors="Zheng-Ming Lin, Ching Chang, Wei-Yao Wang, Kuang-Da Wang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://ojs.aaai.org/index.php/AAAI/article/view/27752">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="AAAI 2024" title="SeGA: Preference-Aware Self-Contrastive Learning with Prompts for Anomalous User Detection on Twitter" url="https://ojs.aaai.org/index.php/AAAI/article/view/27752" authors="Ying-Ying Chang, Wei-Yao Wang♠, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://ojs.aaai.org/index.php/AAAI/article/view/30584">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="AAAI Demo 2024" title="The CoachAI Badminton Environment: Bridging the Gap Between a Reinforcement Learning Environment and Real-World Badminton Games" url="https://ojs.aaai.org/index.php/AAAI/article/view/30584" authors="Kuang-Da Wang, Yu-Tse Chen, Yu-Heng Lin, Wei-Yao Wang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://ojs.aaai.org/index.php/AAAI/article/view/30523">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="AAAI 2024" title="The CoachAI Badminton Environment: A Novel Reinforcement Learning Environment with Realistic Opponents (Student Abstract)" url="https://ojs.aaai.org/index.php/AAAI/article/view/30523" authors="Kuang-Da Wang, Wei-Yao Wang, Yu-Tse Chen, Yu-Heng Lin, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2310.09773">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="EMNLP Findings 2023" title="RSVP: Customer Intent Detection via Agent Response Contrastive and Generative Pre-Training" url="https://arxiv.org/abs/2310.09773" authors="Yu-Chien Tang, Wei-Yao Wang♠, An-Zi Yen, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://dl.acm.org/doi/10.1145/3583780.3615470">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="CIKM 2023" title="DoRA: Domain-Based Self-Supervised Learning Framework for Low-Resource Real Estate Appraisal" url="https://dl.acm.org/doi/10.1145/3583780.3615470" authors="Wei-Wei Du, Wei-Yao Wang♠, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://dl.acm.org/doi/10.1145/3580305.3599906">paper</a>{% endcapture %}
{% include paper.html badge="KDD 2023" title="ShuttleSet: A Human-Annotated Stroke-Level Singles Dataset for Badminton Tactical Analysis" url="https://dl.acm.org/doi/10.1145/3580305.3599906" authors="Wei-Yao Wang, Yung Chang Huang, Tsi-Ui Ik, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://ojs.aaai.org/index.php/AAAI/article/view/25855">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="AAAI 2023" title="Where Will Players Move Next? Dynamic Graphs and Hierarchical Fusion for Movement Forecasting in Badminton" url="https://ojs.aaai.org/index.php/AAAI/article/view/25855" authors="Kai-Shiang Chang, Wei-Yao Wang♠, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://ojs.aaai.org/index.php/AAAI/article/view/26976">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="AAAI 2023" title="A Reinforcement Learning Badminton Environment for Simulating Player Tactics (Student Abstract)" url="https://ojs.aaai.org/index.php/AAAI/article/view/26976" authors="Li-Chun Huang, Nai-Zen Hseuh, Yen-Che Chien, Wei-Yao Wang, Kuang-Da Wang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://dl.acm.org/doi/abs/10.1145/3511808.3557820">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="CIKM 2022" title="Modeling Turn-Based Sequences for Player Tactic Applications in Badminton Matches" url="https://dl.acm.org/doi/abs/10.1145/3511808.3557820" authors="Wei-Yao Wang" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://dl.acm.org/doi/full/10.1145/3551391">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="ACM TIST 2022" title="How Is the Stroke? Inferring Shot Influence in Badminton Matches via Long Short-Term Dependencies" url="https://dl.acm.org/doi/full/10.1145/3551391" authors="Wei-Yao Wang, Teng-Fong Chan, Wen-Chih Peng, Hui-Kuo Yang, Chih-Chuan Wang, Yao-Chung Fan" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2112.01044">paper</a>{% endcapture %}
{% include paper.html badge="AAAI 2022" title="ShuttleNet: Position-Aware Fusion of Rally Progress and Player Styles for Stroke Forecasting in Badminton" url="https://arxiv.org/abs/2112.01044" authors="Wei-Yao Wang, Hong-Han Shuai, Kai-Shiang Chang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2109.06431">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="ICDM 2021" title="Exploring the Long Short-Term Dependencies to Infer Shot Influence in Badminton Matches" url="https://arxiv.org/abs/2109.06431" authors="Wei-Yao Wang, Teng-Fong Chan, Hui-Kuo Yang, Chih-Chuan Wang, Yao-Chung Fan, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://www.airitilibrary.com/Publication/alDetailedMesh?docid=10247297-202006-202007060015-202007060015-201-213">paper</a>{% endcapture %}
{% include paper.html selected="false" badge="PE Journal 2020" title="Badminton Coach AI: A badminton match data analysis platform based on deep learning" url="https://www.airitilibrary.com/Publication/alDetailedMesh?docid=10247297-202006-202007060015-202007060015-201-213" authors="Wei-Yao Wang, Kai-Shiang Chang, Teng-Fong Chen, Chih-Chuan Wang, Wen-Chih Peng, Chih-Wei Yi" links=links %}

{% include paper.html selected="false" kind="workshop" badge="NeurIPS Workshop 2024" title="Align and Fine-Tune: Enhancing LLMs for Time-Series Forecasting" authors="Ching Chang, Wei-Yao Wang, Wen-Chih Peng, Tien-Fu Chen, Sagar Samtani" %}

{% include paper.html selected="false" kind="workshop" badge="NeurIPS Workshop 2024" title="Self-Supervised Learning of Disentangled Representations for Multivariate Time-Series" authors="Ching Chang, Chan Chiao-Tung, Wei-Yao Wang, Wen-Chih Peng, Tien-Fu Chen" %}

{% include paper.html selected="false" kind="workshop" badge="KDD Workshop 2023" title="The CoachAI Badminton Environment: Improving Badminton Player Tactics with A Novel Reinforcement Learning Environment" authors="Kuang-Da Wang, Yu-Tse Chen, Yu-Heng Lin, Wei-Yao Wang, Wen-Chih Peng" %}

{% capture links %}<a class="paper-link-btn" href="https://openreview.net/forum?id=9cuULoi7Ex">paper</a>{% endcapture %}
{% include paper.html selected="false" kind="workshop" badge="ICML Workshop 2023" title="Generating Turn-Based Player Behavior via Experience from Demonstrations" url="https://openreview.net/forum?id=9cuULoi7Ex" authors="Kuang-Da Wang, Wei-Yao Wang, Ping-Chun Hsieh, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2212.12190">paper</a>{% endcapture %}
{% include paper.html kind="workshop" badge="AAAI Workshop 2023" award="Best Paper" title="Look Around! A Neighbor Relation Graph Learning Framework for Real Estate Appraisal" url="https://arxiv.org/abs/2212.12190" authors="Chih-Chia Li, Wei-Yao Wang, Wei-Wei Du, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2302.07740">paper</a>{% endcapture %}
{% include paper.html selected="false" kind="workshop" badge="AAAI Workshop 2023" title="Team Triple-Check at Factify 2: Parameter-Efficient Large Foundation Models with Feature Representations for Multi-Modal Fact Verification" url="https://arxiv.org/abs/2302.07740" authors="Wei-Wei Du, Hong-Wei Wu, Wei-Yao Wang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://ceur-ws.org/Vol-3318/short10.pdf">paper</a>{% endcapture %}
{% include paper.html selected="false" kind="workshop" badge="CIKM Workshop 2022" title="Track2Vec: Fairness Music Recommendation with a GPU-Free Customizable-Driven Framework" url="https://ceur-ws.org/Vol-3318/short10.pdf" authors="Wei-Wei Du, Wei-Yao Wang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://ceur-ws.org/Vol-3318/short9.pdf">paper</a>{% endcapture %}
{% include paper.html selected="false" kind="workshop" badge="CIKM Workshop 2022" title="RecFormer: Personalized Temporal-Aware Transformer for Fair Music Recommendation" url="https://ceur-ws.org/Vol-3318/short9.pdf" authors="Wei-Yao Wang, Wei-Wei Du, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://aclanthology.org/2022.socialnlp-1.0/">paper</a>{% endcapture %}
{% include paper.html selected="false" kind="workshop" badge="NAACL Workshop 2022" title="Proceedings of the Tenth International Workshop on Natural Language Processing for Social Media (SocialNLP 2022)" url="https://aclanthology.org/2022.socialnlp-1.0/" authors="Lun-Wei Ku, Cheng-Te Li, Yu-Che Tsai, Wei-Yao Wang" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://aclanthology.org/2022.ltedi-1.15/">paper</a>{% endcapture %}
{% include paper.html selected="false" kind="workshop" badge="ACL Workshop 2022" title="NYCU_TWD@LT-EDI-ACL2022: Ensemble Models with VADER and Contrastive Learning for Detecting Signs of Depression from Social Media" url="https://aclanthology.org/2022.ltedi-1.15/" authors="Wei-Yao Wang*, Yu-Chien Tang*, Wei-Wei Du*, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://dl.acm.org/doi/10.1145/3487553.3524876">paper</a>{% endcapture %}
{% include paper.html selected="false" kind="workshop" badge="WWW Workshop 2022" title="SocialNLP'22: 10th International Workshop on Natural Language Processing for Social Media" url="https://dl.acm.org/doi/10.1145/3487553.3524876" authors="Lun-Wei Ku, Cheng-Te Li, Yu-Che Tsai, Wei-Yao Wang" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://dl.acm.org/doi/10.1145/3487553.3524664">paper</a>{% endcapture %}
{% include paper.html selected="false" kind="workshop" badge="WWW Workshop 2022" title="KAHAN: Knowledge-Aware Hierarchical Attention Network for Fake News Detection on Social Media" url="https://dl.acm.org/doi/10.1145/3487553.3524664" authors="Yu-Wun Tseng, Hui-Kuo Yang, Wei-Yao Wang, Wen-Chih Peng" links=links %}

{% capture links %}<a class="paper-link-btn" href="https://arxiv.org/abs/2201.11664">paper</a>{% endcapture %}
{% include paper.html kind="workshop" badge="AAAI Workshop 2022" award="Best Paper" title="Team Yao at Factify 2022: Utilizing Pre-trained Models and Co-attention Networks for Multi-Modal Fact Verification" url="https://arxiv.org/abs/2201.11664" authors="Wei-Yao Wang, Wen-Chih Peng" links=links %}

</div>

# Academic Services

**Conference (Senior) Program Committee:**
ICML'26, CVPR'26, ICCV'25, ICLR (25-now), KDD (25-now), AAAI (22-now), IJCAI (23-now), ACL ARR (22-now), ISACE'23, LT-EDI-ACL 2022 @ ACL'22

**Organizer:**
GenProCC @ NeurIPS'25, ITPSS @ IJCAI'23-24, CoachAI Challenge @ IJCAI'23, SocialNLP @ TheWebConf'22 and NAACL'22

**Student Volunteer:**
IJCAI'23, KDD'23

# Honors and Awards

1. [Apr. 2025] Honorary Membership, *The Phi Tau Phi Scholastic Honor Society*
2. [Mar. 2025] Best Dissertation Award, *Institute of Information & Computing Machinery*
3. [Dec. 2024] Top-10% Outstanding Reviewer, *KDD 2025*
4. [Dec. 2024] Best Dissertation Award, *Taiwanese Association for Artificial Intelligence*
5. [Sep. 2023] Sports Science Research Award, *Sport Administration, Ministry of Education*
6. [Aug. 2023] KDD Student Scholarship, *ACM*
7. [Aug. 2023] Top Research of AI and Information Technology Scholarship, *Appier*
8. [May 2023] 21st Y.Z. Hsu Science Paper Award, *Far Eastern Y.Z. Hsu Foundation*
9. [Feb. 2023] AAAI Student Scholarship, *AAAI*
10. [Jan. 2023] Google Conference Scholarships, *Google*
11. [Jan. 2023] AAAI Student Scholarships, *AAAI*
12. [Mar. 2022] Google Conference Scholarships, *Google*
13. [Feb. 2022] Best Paper Award, *AAAI DeFactify Workshop*
14. [Feb. 2022] AAAI Student Scholarships, *AAAI*
15. [Jan. 2022] Top Research of AI and Information Technology Scholarship, *Appier*
16. [Aug. 2019] The Yin Zhi Tong Memorial Scholarship, *National Yang Ming Chiao Tung University*
17. [Jul. 2019] College Student Research Scholarship, *Ministry of Science and Technology*

# Competition Awards

1. [Dec. 2022] **1st Place in Factify 2.0 Challenge**, De-Factify @ AAAI 2023 Workshop [[code](https://github.com/wwweiwei/Pre-CoFactv2-AAAI-2023)]
2. [Oct. 2022] **4th Place in Rounded Evaluation of Recommender Systems**, EvalRS @ CIKM’22 Workshop
3. [Feb. 2022] **2nd Place in Detecting Signs of Depression from Social Media Text**, LT-EDI @ ACL 2022 Workshop [[code](https://github.com/wywyWang/Depression-Detection-LT-EDI-ACL-2022)]
4. [Nov. 2021] **5th Place and Best Paper Award in Factify Challenge**, De-Factify @ AAAI 2022 Workshop [[code](https://github.com/wywyWang/Multi-Modal-Fact-Verification-2021)]
5. [Sep. 2021] **3rd Place and National Judges Award**, Legal-Tech Hackathon 2021. [[code](https://github.com/wywyWang/Legal-tech-2021)]
6. [Jun. 2021] **1st Place in Fake-EmoReact Challenge**, SocialNLP @ NAACL 2021 Workshop [[code](https://github.com/wywyWang/Fake-EmoReact-2021)]
7. [Jan. 2021] **Bronze Medal in Riiid Answer Correctness Prediction Challenge**, AAAI 2021 Workshop [[code](https://github.com/wywyWang/Riiid-Answer-Correctness-Prediction)]
8. [Jun. 2020] **3rd Place in EmotionGIF Challenge**, SocialNLP @ ACL 2020 Workshop [[report](https://arxiv.org/abs/2007.02259), [code](https://github.com/wywyWang/NLP-2020-EmotionGIF)]
9. [Dec. 2019] **Excellent Award on Research Project Competition**, National Chiao Tung University
