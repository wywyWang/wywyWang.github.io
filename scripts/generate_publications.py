#!/usr/bin/env python3
"""Generate Hugo publication pages from a structured list."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "content" / "publications"


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80]


def yaml_quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_pub(pub: dict) -> None:
    slug = pub.get("slug") or slugify(pub["title"])
    folder = ROOT / slug
    folder.mkdir(parents=True, exist_ok=True)

    authors = pub["authors"]
    # Ensure "me" appears for Wei-Yao Wang
    authors_yaml = "\n".join(f"  - {yaml_quote(a) if a != 'me' else 'me'}" for a in authors)

    links = pub.get("links") or []
    links_yaml = ""
    if links:
        links_yaml = "links:\n"
        for link in links:
            links_yaml += f"  - type: {link['type']}\n    url: {yaml_quote(link['url'])}\n"

    awards = pub.get("awards") or []
    awards_yaml = ""
    if awards:
        awards_yaml = "awards:\n"
        for award in awards:
            awards_yaml += f"  - name: {yaml_quote(award)}\n    level: winner\n"

    pub_type = pub.get("publication_types", ["paper-conference"])
    types_yaml = "[" + ", ".join(yaml_quote(t) for t in pub_type) + "]"

    publication_name = pub.get("publication_name", "")
    publication_short = pub.get("publication_short", "")

    content = f"""---
title: {yaml_quote(pub["title"])}
authors:
{authors_yaml}
date: '{pub["date"]}'
publishDate: '{pub["date"]}'
publication_types: {types_yaml}
publication:
  name: {yaml_quote(publication_name)}
  short_name: {yaml_quote(publication_short)}
featured: false
{awards_yaml}{links_yaml}---
"""
    (folder / "index.md").write_text(content, encoding="utf-8")
    print(f"wrote {slug}")


PUBLICATIONS = [
    # Journals and Conferences
    {
        "title": "Omni-Interactive Universal Embedder",
        "authors": ["me", "Kazuya Tateishi", "Shuyang Cui", "Christian Simon", "Takashi Shibuya", "Shusuke Takahashi", "Yuki Mitsufuji"],
        "date": "2026-06-01T00:00:00Z",
        "publication_name": "Preprint",
        "publication_short": "Preprint",
        "publication_types": ["article"],
    },
    {
        "title": "WebGen-V Bench: Structured Representation for Enhancing Visual Design in LLM-based Web Generation and Evaluation",
        "authors": ["Kuang-Da Wang", "Zhao Wang", "Yotaro Shimose", "me", "Shingo Takamatsu"],
        "date": "2025-10-01T00:00:00Z",
        "publication_name": "Preprint",
        "publication_short": "Preprint",
        "publication_types": ["article"],
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2510.15306v1"}],
    },
    {
        "title": "MCA: Modality Composition Awareness for Robust Composed Multimodal Retrieval",
        "authors": ["Qiyu Wu", "Shuyang Cui", "Satoshi Hayakawa", "me", "Hiromi Wakaki", "Yuki Mitsufuji"],
        "date": "2025-10-02T00:00:00Z",
        "publication_name": "Preprint",
        "publication_short": "Preprint",
        "publication_types": ["article"],
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2510.15543"}],
    },
    {
        "title": "SF-Mamba: Rethinking State Space Model for Vision",
        "authors": ["Masakazu Yoshimura", "Teruaki Hayashi", "Yuki Hoshino", "me", "Takeshi Ohashi"],
        "date": "2026-07-01T00:00:00Z",
        "publication_name": "International Conference on Machine Learning (ICML)",
        "publication_short": "ICML",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2603.16423"}],
    },
    {
        "title": "Agentic Model Predictive Questioning Control in Visual Design",
        "authors": ["Kuang-Da Wang", "Zhao Wang", "me", "Yotaro Shimose", "Jaechang Kim", "Shingo Takamatsu"],
        "date": "2026-07-02T00:00:00Z",
        "publication_name": "International Conference on Machine Learning (ICML)",
        "publication_short": "ICML",
    },
    {
        "title": "Seeing is Understanding: Unlocking Causal Attention into Modality-Mutual Attention for Multimodal LLMs",
        "authors": ["me", "Zhao Wang", "Helen Suzuki", "Yoshiyuki Kobayashi"],
        "date": "2026-07-03T00:00:00Z",
        "publication_name": "International Conference on Machine Learning (ICML)",
        "publication_short": "ICML",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2503.02597"}],
    },
    {
        "title": "NEWSAGENT: Benchmarking Multimodal Agents as Journalists with Real-World Newswriting Tasks",
        "authors": ["Yen-Che Chien", "Kuang-Da Wang", "me", "Wen-Chih Peng"],
        "date": "2026-08-01T00:00:00Z",
        "publication_name": "ACL 2026 Findings",
        "publication_short": "ACL Findings",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2509.00446"}],
    },
    {
        "title": "Talk Structurally, Act Hierarchically: A Collaborative Framework for LLM Multi-Agent Systems",
        "authors": ["Zhao Wang", "Sota Moriyama", "me", "Briti Gangopadhyay", "Shingo Takamatsu"],
        "date": "2026-01-15T00:00:00Z",
        "publication_name": "IEEE Transactions on Artificial Intelligence",
        "publication_short": "IEEE TAI",
        "publication_types": ["article-journal"],
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2502.11098"}],
    },
    {
        "title": "Echoes Over Time: Unlocking Length Generalization in Video-to-Audio Generation Models",
        "authors": ["Christian Simon", "Masato Ishii", "me", "Koichi Saito", "Akio Hayakawa", "Dongseok Shim", "Zhi Zhong", "Shuyang Cui", "Takashi Shibuya", "Shusuke Takahashi", "Yuki Mitsufuji"],
        "date": "2026-06-15T00:00:00Z",
        "publication_name": "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)",
        "publication_short": "CVPR",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2602.20981"}],
    },
    {
        "title": "VIRTUE: Visual-Interactive Text-Image Universal Embedder",
        "authors": ["me", "Kazuya Tateishi", "Qiyu Wu", "Shusuke Takahashi", "Yuki Mitsufuji"],
        "date": "2026-04-01T00:00:00Z",
        "publication_name": "International Conference on Learning Representations (ICLR)",
        "publication_short": "ICLR",
        "links": [
            {"type": "pdf", "url": "https://arxiv.org/abs/2510.00523"},
            {"type": "project", "url": "https://sony.github.io/virtue/"},
        ],
    },
    {
        "title": "Adapting to Evolving Data: Test-Time Expert Aggregation for Imbalanced Tabular Regression",
        "authors": ["Yung-Chien Wang", "Kuang-Da Wang", "me", "Wen-Chih Peng"],
        "date": "2026-02-01T00:00:00Z",
        "publication_name": "WSDM 2026",
        "publication_short": "WSDM",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2506.07033"}],
    },
    {
        "title": "GenProCC: 1st Workshop on Generative and Protective AI for Content Creation",
        "authors": ["me", "Takashi Shibuya", "Vali Lalioti", "Wei Wang", "Shusuke Takahashi", "Yuki Mitsufuji"],
        "date": "2025-12-01T00:00:00Z",
        "publication_name": "NeurIPS 2025 Workshop",
        "publication_short": "NeurIPS Workshop",
        "publication_types": ["paper-conference"],
        "links": [{"type": "project", "url": "https://genprocc.github.io/"}],
    },
    {
        "title": "Tree-of-Report: Table-to-Text Generation for Sports Game Reports with Tree-Structured Prompting",
        "authors": ["Shang-Hsuan Chiang", "Tsan-Tsung Yang", "Kuang-Da Wang", "me", "An-Zi Yen", "Wen-Chih Peng"],
        "date": "2025-07-01T00:00:00Z",
        "publication_name": "ACL SRW 2025 (Oral)",
        "publication_short": "ACL SRW",
        "awards": ["Oral"],
    },
    {
        "title": "LLM4TS: Aligning Pre-Trained LLMs as Data-Efficient Time-Series Forecasters",
        "authors": ["Ching Chang", "me", "Wen-Chih Peng", "Tien-Fu Chen"],
        "date": "2025-03-01T00:00:00Z",
        "publication_name": "ACM Transactions on Intelligent Systems and Technology (TIST)",
        "publication_short": "ACM TIST",
        "publication_types": ["article-journal"],
        "links": [{"type": "pdf", "url": "https://dl.acm.org/doi/10.1145/3719207"}],
    },
    {
        "title": "ShuttleSHAP: A Turn-Based Feature Attribution Approach for Analyzing Forecasting Models in Badminton",
        "authors": ["me", "Wen-Chih Peng", "Wei Wang", "Philip Yu"],
        "date": "2025-05-01T00:00:00Z",
        "publication_name": "PAKDD 2025",
        "publication_short": "PAKDD",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2312.10942"}],
    },
    {
        "title": "APAR: Modeling Irregular Target Functions in Tabular Regression via Arithmetic-Aware Pre-Training and Adaptive-Regularized Fine-Tuning",
        "authors": ["Hong-Wei Wu", "me", "Kuang-Da Wang", "Wen-Chih Peng"],
        "date": "2025-02-01T00:00:00Z",
        "publication_name": "AAAI 2025",
        "publication_short": "AAAI",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2412.10941v1"}],
    },
    {
        "title": "A Survey on Self-Supervised Learning for Non-Sequential Tabular Data",
        "authors": ["me", "Wei-Wei Du", "Derek Xu", "Wei Wang", "Wen-Chih Peng"],
        "date": "2024-12-01T00:00:00Z",
        "publication_name": "ACML 2024",
        "publication_short": "ACML",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2402.01204"}],
    },
    {
        "title": "Professional Basketball Player Behavior Synthesis via Planning with Diffusion",
        "authors": ["me", "Xiusi Chen", "Ziniu Hu", "David Reynoso", "Kun Jin", "Mingyan Liu", "P. Jeffrey Brantingham", "Wei Wang"],
        "date": "2024-10-01T00:00:00Z",
        "publication_name": "CIKM 2024",
        "publication_short": "CIKM",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2306.04090"}],
    },
    {
        "title": "Offline Imitation of Badminton Player Behavior via Experiential Contexts and Brownian Motion",
        "authors": ["Kuang-Da Wang", "me", "Ping-Chun Hsieh", "Wen-Chih Peng"],
        "date": "2024-09-01T00:00:00Z",
        "publication_name": "ECML-PKDD 2024",
        "publication_short": "ECML-PKDD",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2403.12406"}],
    },
    {
        "title": "Benchmarking Stroke Forecasting with Stroke-Level Badminton Dataset",
        "authors": ["me", "Wei-Wei Du", "Wen-Chih Peng"],
        "date": "2024-08-01T00:00:00Z",
        "publication_name": "IJCAI Demo 2024",
        "publication_short": "IJCAI Demo",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2306.15664"}],
    },
    {
        "title": "TimeDRL: Disentangled Representation Learning for Multivariate Time-Series",
        "authors": ["Ching Chang", "Chiao-Tung Chan", "me", "Wen-Chih Peng", "Tien-Fu Chen"],
        "date": "2024-05-01T00:00:00Z",
        "publication_name": "ICDE 2024",
        "publication_short": "ICDE",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2312.04142"}],
    },
    {
        "title": "Look Around! A Neighbor Relation Graph Learning Framework for Real Estate Appraisal",
        "slug": "look-around-pakdd-2024",
        "authors": ["Chih-Chia Li", "me", "Wei-Wei Du", "Wen-Chih Peng"],
        "date": "2024-05-02T00:00:00Z",
        "publication_name": "PAKDD 2024",
        "publication_short": "PAKDD",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2212.12190"}],
    },
    {
        "title": "Style-News: Incorporating Stylized News Generation and Adversarial Verification for Neural Fake News Detection",
        "authors": ["me", "Yu-Chieh Chang", "Wen-Chih Peng"],
        "date": "2024-03-01T00:00:00Z",
        "publication_name": "EACL 2024",
        "publication_short": "EACL",
        "links": [{"type": "pdf", "url": "https://aclanthology.org/2024.eacl-long.92/"}],
    },
    {
        "title": "Root Cause Analysis In Microservice Using Neural Granger Causal Discovery",
        "authors": ["Zheng-Ming Lin", "Ching Chang", "me", "Kuang-Da Wang", "Wen-Chih Peng"],
        "date": "2024-02-01T00:00:00Z",
        "publication_name": "AAAI 2024",
        "publication_short": "AAAI",
        "links": [{"type": "pdf", "url": "https://ojs.aaai.org/index.php/AAAI/article/view/27772"}],
    },
    {
        "title": "SeGA: Preference-Aware Self-Contrastive Learning with Prompts for Anomalous User Detection on Twitter",
        "authors": ["Ying-Ying Chang", "me", "Wen-Chih Peng"],
        "date": "2024-02-02T00:00:00Z",
        "publication_name": "AAAI 2024",
        "publication_short": "AAAI",
        "links": [{"type": "pdf", "url": "https://ojs.aaai.org/index.php/AAAI/article/view/27752"}],
    },
    {
        "title": "The CoachAI Badminton Environment: Bridging the Gap Between a Reinforcement Learning Environment and Real-World Badminton Games",
        "slug": "coachai-aaai-demo-2024",
        "authors": ["Kuang-Da Wang", "Yu-Tse Chen", "Yu-Heng Lin", "me", "Wen-Chih Peng"],
        "date": "2024-02-03T00:00:00Z",
        "publication_name": "AAAI Demo 2024",
        "publication_short": "AAAI Demo",
        "links": [{"type": "pdf", "url": "https://ojs.aaai.org/index.php/AAAI/article/view/30584"}],
    },
    {
        "title": "The CoachAI Badminton Environment: A Novel Reinforcement Learning Environment with Realistic Opponents (Student Abstract)",
        "slug": "coachai-aaai-sa-2024",
        "authors": ["Kuang-Da Wang", "me", "Yu-Tse Chen", "Yu-Heng Lin", "Wen-Chih Peng"],
        "date": "2024-02-04T00:00:00Z",
        "publication_name": "AAAI 2024",
        "publication_short": "AAAI",
        "links": [{"type": "pdf", "url": "https://ojs.aaai.org/index.php/AAAI/article/view/30523"}],
    },
    {
        "title": "RSVP: Customer Intent Detection via Agent Response Contrastive and Generative Pre-Training",
        "authors": ["Yu-Chien Tang", "me", "An-Zi Yen", "Wen-Chih Peng"],
        "date": "2023-12-01T00:00:00Z",
        "publication_name": "EMNLP Findings 2023",
        "publication_short": "EMNLP Findings",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2310.09773"}],
    },
    {
        "title": "DoRA: Domain-Based Self-Supervised Learning Framework for Low-Resource Real Estate Appraisal",
        "authors": ["Wei-Wei Du", "me", "Wen-Chih Peng"],
        "date": "2023-10-01T00:00:00Z",
        "publication_name": "CIKM 2023",
        "publication_short": "CIKM",
        "links": [{"type": "pdf", "url": "https://dl.acm.org/doi/10.1145/3583780.3615470"}],
    },
    {
        "title": "ShuttleSet: A Human-Annotated Stroke-Level Singles Dataset for Badminton Tactical Analysis",
        "authors": ["me", "Yung Chang Huang", "Tsi-Ui Ik", "Wen-Chih Peng"],
        "date": "2023-08-01T00:00:00Z",
        "publication_name": "KDD 2023",
        "publication_short": "KDD",
        "links": [{"type": "pdf", "url": "https://dl.acm.org/doi/10.1145/3580305.3599906"}],
    },
    {
        "title": "Where Will Players Move Next? Dynamic Graphs and Hierarchical Fusion for Movement Forecasting in Badminton",
        "authors": ["Kai-Shiang Chang", "me", "Wen-Chih Peng"],
        "date": "2023-02-01T00:00:00Z",
        "publication_name": "AAAI 2023",
        "publication_short": "AAAI",
        "links": [{"type": "pdf", "url": "https://ojs.aaai.org/index.php/AAAI/article/view/25855"}],
    },
    {
        "title": "A Reinforcement Learning Badminton Environment for Simulating Player Tactics (Student Abstract)",
        "authors": ["Li-Chun Huang", "Nai-Zen Hseuh", "Yen-Che Chien", "me", "Kuang-Da Wang", "Wen-Chih Peng"],
        "date": "2023-02-02T00:00:00Z",
        "publication_name": "AAAI 2023",
        "publication_short": "AAAI",
        "links": [{"type": "pdf", "url": "https://ojs.aaai.org/index.php/AAAI/article/view/26976"}],
    },
    {
        "title": "Modeling Turn-Based Sequences for Player Tactic Applications in Badminton Matches",
        "authors": ["me"],
        "date": "2022-10-01T00:00:00Z",
        "publication_name": "CIKM 2022",
        "publication_short": "CIKM",
        "links": [{"type": "pdf", "url": "https://dl.acm.org/doi/abs/10.1145/3511808.3557820"}],
    },
    {
        "title": "How Is the Stroke? Inferring Shot Influence in Badminton Matches via Long Short-Term Dependencies",
        "authors": ["me", "Teng-Fong Chan", "Wen-Chih Peng", "Hui-Kuo Yang", "Chih-Chuan Wang", "Yao-Chung Fan"],
        "date": "2022-01-01T00:00:00Z",
        "publication_name": "ACM Transactions on Intelligent Systems and Technology (TIST)",
        "publication_short": "ACM TIST",
        "publication_types": ["article-journal"],
        "links": [{"type": "pdf", "url": "https://dl.acm.org/doi/full/10.1145/3551391"}],
    },
    {
        "title": "ShuttleNet: Position-Aware Fusion of Rally Progress and Player Styles for Stroke Forecasting in Badminton",
        "authors": ["me", "Hong-Han Shuai", "Kai-Shiang Chang", "Wen-Chih Peng"],
        "date": "2022-02-01T00:00:00Z",
        "publication_name": "AAAI 2022",
        "publication_short": "AAAI",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2112.01044"}],
    },
    {
        "title": "Exploring the Long Short-Term Dependencies to Infer Shot Influence in Badminton Matches",
        "authors": ["me", "Teng-Fong Chan", "Hui-Kuo Yang", "Chih-Chuan Wang", "Yao-Chung Fan", "Wen-Chih Peng"],
        "date": "2021-12-01T00:00:00Z",
        "publication_name": "ICDM 2021",
        "publication_short": "ICDM",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2109.06431"}],
    },
    {
        "title": "Badminton Coach AI: A badminton match data analysis platform based on deep learning",
        "authors": ["me", "Kai-Shiang Chang", "Teng-Fong Chen", "Chih-Chuan Wang", "Wen-Chih Peng", "Chih-Wei Yi"],
        "date": "2020-06-01T00:00:00Z",
        "publication_name": "Physical Education Journal",
        "publication_short": "PEJ",
        "publication_types": ["article-journal"],
        "links": [{"type": "pdf", "url": "https://www.airitilibrary.com/Publication/alDetailedMesh?docid=10247297-202006-202007060015-202007060015-201-213"}],
    },
    # Workshops
    {
        "title": "Align and Fine-Tune: Enhancing LLMs for Time-Series Forecasting",
        "authors": ["Ching Chang", "me", "Wen-Chih Peng", "Tien-Fu Chen", "Sagar Samtani"],
        "date": "2024-12-10T00:00:00Z",
        "publication_name": "NeurIPS 2024 Workshop on Time Series in the Age of Large Models",
        "publication_short": "NeurIPS Workshop",
    },
    {
        "title": "Self-Supervised Learning of Disentangled Representations for Multivariate Time-Series",
        "authors": ["Ching Chang", "Chan Chiao-Tung", "me", "Wen-Chih Peng", "Tien-Fu Chen"],
        "date": "2024-12-11T00:00:00Z",
        "publication_name": "NeurIPS 2024 Workshop on Self-Supervised Learning - Theory and Practice",
        "publication_short": "NeurIPS Workshop",
    },
    {
        "title": "The CoachAI Badminton Environment: Improving Badminton Player Tactics with A Novel Reinforcement Learning Environment",
        "slug": "coachai-kdd-workshop-2023",
        "authors": ["Kuang-Da Wang", "Yu-Tse Chen", "Yu-Heng Lin", "me", "Wen-Chih Peng"],
        "date": "2023-08-10T00:00:00Z",
        "publication_name": "ACM SIGKDD Workshop on Data Science and AI for Sports, 2023",
        "publication_short": "KDD Workshop",
    },
    {
        "title": "Generating Turn-Based Player Behavior via Experience from Demonstrations",
        "authors": ["Kuang-Da Wang", "me", "Ping-Chun Hsieh", "Wen-Chih Peng"],
        "date": "2023-07-01T00:00:00Z",
        "publication_name": "ICML 2023 Workshop on Structured Probabilistic Inference & Generative Modeling",
        "publication_short": "ICML Workshop",
        "links": [{"type": "pdf", "url": "https://openreview.net/forum?id=9cuULoi7Ex"}],
    },
    {
        "title": "Look Around! A Neighbor Relation Graph Learning Framework for Real Estate Appraisal",
        "slug": "look-around-aaai-workshop-2023",
        "authors": ["Chih-Chia Li", "me", "Wei-Wei Du", "Wen-Chih Peng"],
        "date": "2023-02-10T00:00:00Z",
        "publication_name": "AAAI Workshop on Modelling Uncertainty in the Financial World, 2023",
        "publication_short": "AAAI Workshop",
        "awards": ["Best Paper Award"],
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2212.12190"}],
    },
    {
        "title": "Team Triple-Check at Factify 2: Parameter-Efficient Large Foundation Models with Feature Representations for Multi-Modal Fact Verification",
        "authors": ["Wei-Wei Du", "Hong-Wei Wu", "me", "Wen-Chih Peng"],
        "date": "2023-02-11T00:00:00Z",
        "publication_name": "AAAI Workshop on Multimodal Fact Checking and Hate Speech Detection, 2023",
        "publication_short": "AAAI Workshop",
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2302.07740"}],
    },
    {
        "title": "Track2Vec: Fairness Music Recommendation with a GPU-Free Customizable-Driven Framework",
        "authors": ["Wei-Wei Du", "me", "Wen-Chih Peng"],
        "date": "2022-10-10T00:00:00Z",
        "publication_name": "CIKM Workshop on A Rounded Evaluation of Recommender Systems, 2022",
        "publication_short": "CIKM Workshop",
        "links": [{"type": "pdf", "url": "https://ceur-ws.org/Vol-3318/short10.pdf"}],
    },
    {
        "title": "RecFormer: Personalized Temporal-Aware Transformer for Fair Music Recommendation",
        "authors": ["me", "Wei-Wei Du", "Wen-Chih Peng"],
        "date": "2022-10-11T00:00:00Z",
        "publication_name": "CIKM Workshop on A Rounded Evaluation of Recommender Systems, 2022",
        "publication_short": "CIKM Workshop",
        "links": [{"type": "pdf", "url": "https://ceur-ws.org/Vol-3318/short9.pdf"}],
    },
    {
        "title": "Proceedings of the Tenth International Workshop on Natural Language Processing for Social Media (SocialNLP 2022)",
        "authors": ["Lun-Wei Ku", "Cheng-Te Li", "Yu-Che Tsai", "me"],
        "date": "2022-07-01T00:00:00Z",
        "publication_name": "NAACL Workshop on Natural Language Processing for Social Media, 2022",
        "publication_short": "NAACL Workshop",
        "links": [{"type": "pdf", "url": "https://aclanthology.org/2022.socialnlp-1.0/"}],
    },
    {
        "title": "NYCU_TWD@LT-EDI-ACL2022: Ensemble Models with VADER and Contrastive Learning for Detecting Signs of Depression from Social Media",
        "authors": ["me", "Yu-Chien Tang", "Wei-Wei Du", "Wen-Chih Peng"],
        "date": "2022-05-01T00:00:00Z",
        "publication_name": "ACL Workshop on Language Technology for Equality, Diversity, Inclusion, 2022",
        "publication_short": "ACL Workshop",
        "links": [{"type": "pdf", "url": "https://aclanthology.org/2022.ltedi-1.15/"}],
    },
    {
        "title": "SocialNLP'22: 10th International Workshop on Natural Language Processing for Social Media",
        "authors": ["Lun-Wei Ku", "Cheng-Te Li", "Yu-Che Tsai", "me"],
        "date": "2022-04-01T00:00:00Z",
        "publication_name": "WWW Workshop on Natural Language Processing for Social Media, 2022",
        "publication_short": "WWW Workshop",
        "links": [{"type": "pdf", "url": "https://dl.acm.org/doi/10.1145/3487553.3524876"}],
    },
    {
        "title": "KAHAN: Knowledge-Aware Hierarchical Attention Network for Fake News Detection on Social Media",
        "authors": ["Yu-Wun Tseng", "Hui-Kuo Yang", "me", "Wen-Chih Peng"],
        "date": "2022-04-02T00:00:00Z",
        "publication_name": "WWW Workshop on Natural Language Processing for Social Media, 2022",
        "publication_short": "WWW Workshop",
        "links": [{"type": "pdf", "url": "https://dl.acm.org/doi/10.1145/3487553.3524664"}],
    },
    {
        "title": "Team Yao at Factify 2022: Utilizing Pre-trained Models and Co-attention Networks for Multi-Modal Fact Verification",
        "authors": ["me", "Wen-Chih Peng"],
        "date": "2022-02-20T00:00:00Z",
        "publication_name": "AAAI Workshop on Multimodal Fact Checking and Hate Speech Detection, 2022",
        "publication_short": "AAAI Workshop",
        "awards": ["Best Paper Award"],
        "links": [{"type": "pdf", "url": "https://arxiv.org/abs/2201.11664"}],
    },
]


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for pub in PUBLICATIONS:
        write_pub(pub)
    print(f"generated {len(PUBLICATIONS)} publications")


if __name__ == "__main__":
    main()
