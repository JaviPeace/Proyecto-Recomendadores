# Proyecto de Sistemas Recomendadores

Este repositorio contiene la entrega final de Proyecto de sistemas recomendadores


# Fair Team Formation with Adila and FIFA23 Data

This project explores fairness-aware team formation in professional football using the Adila framework. We adapt Adila — originally designed for expert team recommendation — to the domain of football, leveraging real-world FIFA23 player data.

## 🎯 Objectives

- Adapt Adila’s fairness-aware reranking algorithms to football team formation.
- Build a cleaned and structured dataset from FIFA23 data.
- Evaluate the impact of fairness constraints (Demographic Parity) on team recommendations.

## 🏗️ Contributions

1. **FIFA23 Dataset Creation**: Cleaned, deduplicated player data with unique identifiers and club mappings.
2. **Adila-Compatible Format**: Serialized output (`teams.pkl`, `teamsvecs.pkl`, `indexes.pkl`) matching Adila’s input requirements.
3. **Reproducible Pipeline**:
   - Load and preprocess data.
   - Generate baseline team predictions.
   - Apply Adila's `det cons` reranking.
   - Evaluate fairness and utility metrics.
4. **Metric Evaluation**: NDCG@k, MAP@k (utility); exposure difference, utility-aware exposure, representation skew, and KL-divergence (fairness).
5. **First Step Toward Larger Research Agenda**: Provides a foundation for future studies on fair team recommendation in sports.

## ⚙️ Pipeline Overview

1. Generate initial team predictions (`simple_predictor_folds_22.py`).
2. Apply reranking (`det cons`) using Adila’s fairness algorithms.
3. Evaluate before/after using utility & fairness metrics.
4. Repeat across 3 folds (f0, f1, f2).
## 📊 Metrics

| Metric Type | Examples |
|-------------|----------|
| Utility     | NDCG@k, MAP@k |
| Fairness    | EXP, EXPU, Skew, NDKL |

## 👥 Integrantes

- **Javiera Belén López Massaro**  
- **Javiera Paz Azócar Oliva**  
- **Pablo Poblete Arraé**  
- **Gabriel Acevedo**
