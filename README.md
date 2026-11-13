# Automatic Room Classification from Architectural Blueprint Images

### Deep Learning | Computer Vision | Image Classification | Transfer Learning

An automated room classification system using deep learning to identify room types from architectural blueprint images.

This project investigates the use of Convolutional Neural Networks (CNN) and transfer learning with EfficientNetB0 to classify architectural blueprint images into 19 different room categories.

---

## 1. Project Overview

Managing large building portfolios involves processing thousands of architectural room images. Manually identifying and labelling these rooms is time-consuming, inconsistent, and difficult to scale.

The objective of this project was to explore deep learning approaches for automating room classification from architectural blueprint images.

Two models were developed and evaluated:

- **BlueprintCNN:** A custom convolutional neural network trained from scratch.
- **EfficientNetB0:** A pretrained deep learning model adapted using transfer learning and two-phase fine-tuning.

## 2. Project Workflow

The following workflow illustrates the classification pipeline, from architectural blueprint image processing to model training and room classification.

![Architectural Blueprint Room Classification Workflow](images/Blueprint%20to%20AI%20Room%20Classification%20Workflow.png)

## 3. Dataset Overview

The dataset contains:

| Dataset characteristic | Details |
|---|---|
| Total images | 1,517 |
| Building projects | 20 |
| Room categories | 19 |
| Image format | PNG |
| Image characteristics | Black-and-white architectural drawings |

The dataset was divided at building level to prevent data leakage:

| Dataset | Buildings | Images |
|---|---|---:|
| Training | 1–14 | 1,060 |
| Validation | 15–17 | 223 |
| Testing | 18–20 | 234 |

This strategy evaluates model performance on buildings not encountered during training.

*Note: Original project dataset images are not included in this repository.*

## 4. Methodology

The project followed a structured deep learning workflow involving image preprocessing, model development, training and evaluation.

### A. Image Preprocessing

- Contrast enhancement using CLAHE.
- Aspect-ratio-preserving image padding.
- Image resizing to 224 × 224 pixels.
- Model-specific image normalization.
- Data augmentation using Albumentations.

### B. Model 1: BlueprintCNN

A custom CNN architecture was developed and trained from random initialization.

The architecture consists of four convolutional blocks with increasing filter sizes:

**32 → 64 → 128 → 256**

It uses convolution, batch normalization, ReLU activation, max pooling, dropout and a classification head.

### C. Model 2: EfficientNetB0

EfficientNetB0 pretrained on ImageNet was adapted to the architectural blueprint domain.

Two-phase training was applied:

**Phase 1 — Frozen Backbone**

- Freeze pretrained backbone parameters.
- Train the new classification head.
- Maximum 20 epochs.
- Learning rate: 0.001.

**Phase 2 — Fine-Tuning**

- Unfreeze the last 30 backbone layers.
- Fine-tune the model using a smaller learning rate.
- Maximum 20 epochs.
- Learning rate: 0.00002.

### D. Class Imbalance Handling

Two techniques were used:

- WeightedRandomSampler.
- Class-weighted CrossEntropyLoss.

These methods help address the uneven distribution of room categories.

## 5. Experimental Results

Both models were evaluated using the same unseen-building test dataset containing 234 images.

| Model | Test Accuracy | Weighted F1 |
|---|---:|---:|
| BlueprintCNN | 1.28% | 0.0082 |
| EfficientNetB0 | **41.03%** | **0.4095** |

EfficientNetB0 significantly outperformed the custom CNN baseline.

The results demonstrate the potential value of transfer learning when working with a relatively small and imbalanced image dataset.

However, the results also indicate that further improvements are needed to achieve reliable classification across all room categories.

## 6. Challenges and Key Learnings

Several challenges and observations emerged during the experiments:

- Limited training samples affected the models' ability to generalize.
- Class imbalance reduced performance on underrepresented room categories.
- Training a CNN from scratch performed poorly on unseen buildings.
- Transfer learning improved classification performance substantially.
- Building-level dataset splitting provided a more realistic evaluation.
- Model accuracy alone was insufficient to understand performance across individual room categories.

The experiments provided practical insights into CNN architectures, transfer learning, image preprocessing and model evaluation.

For a more detailed discussion, see [Challenges and Learnings](docs/challenges-and-learnings.md).

## 7. Technologies and Concepts

| Category | Technologies / Concepts |
|---|---|
| Programming | Python |
| Deep Learning Framework | PyTorch |
| Computer Vision | OpenCV |
| Model Architectures | CNN, EfficientNetB0 |
| Image Processing | CLAHE, Image Resizing, Padding |
| Data Augmentation | Albumentations |
| Machine Learning | Transfer Learning, Fine-Tuning |
| Evaluation | Accuracy, Precision, Recall, F1-score |
| Development | Jupyter Notebook, Google Colab |

## 8. Repository Structure

```text
Architectural-Blueprint-Room-Classification/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── images/
│   └── Blueprint to AI Room Classification Workflow.png
│
├── notebooks/
│   └── room_classification.ipynb
│
├── src/
│   └── helper.py
│
└── docs/
    ├── methodology.md
    └── challenges-and-learnings.md
```

## 9. Project Documentation

Additional documentation is available in the following files:

- [Methodology](docs/methodology.md) — Detailed explanation of the dataset, preprocessing, model architectures, training and evaluation.
- [Challenges and Learnings](docs/challenges-and-learnings.md) — Technical challenges, experimental observations and lessons learned.
- [Jupyter Notebook](notebooks/room_classification.ipynb) — Main deep learning implementation.
- [Supporting Python Code](src/helper.py) — Helper functions for blueprint processing and visualisation.

## 10. Future Improvements

- Increase the number of samples for underrepresented room categories.
- Investigate semi-supervised learning.
- Explore alternative pretrained architectures and ensemble models.
- Improve generalization to unseen buildings.
- Investigate additional image preprocessing techniques.
- Experiment with strategies to improve class-specific performance.

## 11. Contributors

**Reshma Mani**  
**Ardra Suresh**

School of Engineering, Jönköping University, Sweden.

## Acknowledgements

This project was conducted in the context of architectural room classification for a building portfolio associated with Herenco.

---

*Exploring how deep learning can transform architectural image analysis.*

