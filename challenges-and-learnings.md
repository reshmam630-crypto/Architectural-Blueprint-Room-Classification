# Challenges and Learnings — Architectural Blueprint Room Classification

## 1. Introduction

During the development of the architectural blueprint room classification project, several challenges were observed while working with image preprocessing, dataset distribution, model training and evaluation.

This document records the main technical challenges, observations and lessons learned during the experiments.

## 2. Challenges Encountered

### 2.1 Limited Dataset Size

The dataset contained 1,517 images distributed across 19 room categories.

Some categories had considerably fewer images than others.

**Observation:**

Limited training examples made it difficult for the models to learn reliable visual patterns for every room category.

**Learning:**

Understanding the importance of dataset size and class distribution when developing deep learning models.

### 2.2 Class Imbalance

The number of images varied significantly between room categories.

For example, some categories had many more samples than others.

**Approach explored:**

- Class-weighted CrossEntropyLoss.
- WeightedRandomSampler.
- Data augmentation.

**Learning:**

Overall accuracy alone does not provide a complete picture of model performance when working with imbalanced datasets. Weighted F1-score, precision and recall are also important.

### 2.3 Generalisation to Unseen Buildings

One important challenge was evaluating the models on buildings that were not included during training.

Instead of randomly splitting individual images, the dataset was divided at building-project level.

**Observation:**

The models were evaluated on three buildings that were completely held out from training and validation.

This made the evaluation more representative of performance on previously unseen building projects.

**Learning:**

Data leakage can produce misleading evaluation results. The way a dataset is split is especially important when images originate from related buildings or projects.

### 2.4 Custom CNN Performance

BlueprintCNN was trained from scratch using four convolutional blocks.

The model achieved:

- Test accuracy: 1.28%.
- Weighted F1-score: 0.0082.

**Observation:**

The custom CNN baseline struggled to generalise to the unseen test buildings.

**Learning:**

Designing a CNN architecture alone does not guarantee good classification performance. Dataset size, feature quality, model capacity and generalisation all matter.

### 2.5 Transfer Learning and Fine-Tuning

EfficientNetB0 was introduced to investigate whether pretrained image features could improve classification.

The experiment involved:

- Freezing the pretrained backbone.
- Training a new classification head.
- Unfreezing the last 30 backbone layers.
- Fine-tuning with a smaller learning rate.

**Observation:**

EfficientNetB0 achieved 41.03% test accuracy and a weighted F1-score of 0.4095.

This was a substantial improvement over the custom CNN baseline.

**Learning:**

Transfer learning can be valuable when the available dataset is relatively small and training a deep network from scratch is challenging.

However, the results also show that transfer learning does not automatically solve all generalisation problems.

### 2.6 Class-Level Prediction Performance

Although EfficientNetB0 performed better overall, its classification report showed that performance varied considerably across room categories.

Some categories had very low or zero F1-scores.

**Learning:**

It is important to examine individual class performance rather than relying only on overall accuracy.

Categories with very few training or test samples require additional attention.

## 3. Key Technical Learnings

Through these experiments, I developed a better understanding of:

- Image preprocessing and contrast enhancement using CLAHE.
- Building custom CNN architectures using PyTorch.
- Transfer learning using pretrained EfficientNetB0.
- Two-phase training and fine-tuning.
- Data augmentation using Albumentations.
- Class imbalance handling.
- Building-level dataset splitting.
- Model evaluation using accuracy, precision, recall and F1-score.
- The importance of generalisation to unseen data.

## 4. Areas for Future Improvement

Based on the experimental observations, several improvements could be investigated:

1. Collect additional samples for underrepresented room categories.
2. Explore alternative data augmentation strategies.
3. Investigate other pretrained architectures.
4. Experiment with different learning rates and training configurations.
5. Explore techniques for improving generalisation to unseen buildings.
6. Investigate class-specific performance and prediction errors.
7. Evaluate whether additional preprocessing approaches improve classification.

## 5. Personal Reflection

One of the important takeaways from this project was understanding that building a machine learning model involves much more than implementing an architecture.

Dataset exploration, preprocessing, experimental design, model selection and evaluation all influence the final outcome.

Comparing a custom CNN with EfficientNetB0 helped me understand the practical value of transfer learning and the challenges associated with real-world image classification.

The experiments also highlighted the importance of analysing unsuccessful results, identifying limitations and using them to guide future improvements.

---

*Documenting challenges and learning from experiments is an important part of developing reliable machine learning solutions.*
