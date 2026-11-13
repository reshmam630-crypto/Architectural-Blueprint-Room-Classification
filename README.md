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

The following workflow illustrates the complete classification pipeline, from blueprint image processing to model evaluation and room prediction.

![Architectural Blueprint Room Classification Workflow](images/room-classification-workflow.png)

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

- Training: Buildings 1–14 (1,060 images)
- Validation: Buildings 15–17 (223 images)
- Testing: Buildings 18–20 (234 images)

This strategy evaluates model performance on buildings not encountered during training.

*Note: Original project dataset images are not included in this public repository.*

## 4. Methodology

### A. Image Preprocessing

- Contrast enhancement using CLAHE.
- Aspect-ratio-preserving image padding.
- Model-specific image normalization.
- Data augmentation.

### B. Model 1: BlueprintCNN

A custom CNN architecture trained from random initialization.

The architecture consists of four convolutional blocks with increasing filter sizes:

32 → 64 → 128 → 256

It uses convolution, batch normalization, ReLU activation, max pooling, dropout, and a classification head.

### C. Model 2: EfficientNetB0

EfficientNetB0 pretrained on ImageNet was adapted to the architectural blueprint domain.

Two-phase training was applied:

**Phase 1 — Frozen Backbone**
- Freeze pretrained backbone parameters.
- Train the new classification head.
- 20 epochs.
- Learning rate: 0.001.

**Phase 2 — Fine-Tuning**
- Unfreeze the last 30 backbone layers.
- Fine-tune the model using a smaller learning rate.
- 20 epochs.
- Learning rate: 0.00002.

### D. Class Imbalance Handling

Two techniques were used:

- WeightedRandomSampler
- Class-weighted CrossEntropyLoss

These methods help address the uneven distribution of room categories.

## 5. Experimental Results

Both models were evaluated using the same unseen-building test dataset.

| Model | Test Accuracy | Weighted F1 |
|---|---:|---:|
| BlueprintCNN | 1.28% | 0.0082 |
| EfficientNetB0 | **41.03%** | **0.4095** |

EfficientNetB0 significantly outperformed the custom CNN baseline.

The results demonstrate the value of transfer learning when working with a relatively small and imbalanced image dataset.

## 6. Challenges and Key Findings

- Limited training samples affected the model's ability to generalize.
- Class imbalance reduced performance on underrepresented room categories.
- Training a CNN from scratch performed poorly on unseen buildings.
- Transfer learning improved classification performance substantially.
- Building-level data splitting provided a more realistic evaluation.

An important finding was that classes with very few training images, such as library and waiting room, remained difficult to classify.

## 7. Technologies and Concepts

- Python
- Deep Learning
- Convolutional Neural Networks
- EfficientNetB0
- Transfer Learning
- Image Preprocessing
- CLAHE
- Data Augmentation
- Model Evaluation
- Confusion Matrix Analysis

## 8. Project Structure

```text
Architectural-Blueprint-Room-Classification/
│
├── README.md
│
└── images/
    └── Blueprint to AI Room Classification Workflow.png
```

Additional source code, experiments, and evaluation visualizations can be added as approved project materials become available.

## 9. Future Improvements

- Increase the number of samples for underrepresented room categories.
- Investigate semi-supervised learning.
- Explore ensemble models.
- Improve generalization to unseen buildings.
- Investigate additional image preprocessing techniques.

## 10. Contributors

**Reshma Mani**  
**Ardra Suresh**

School of Engineering, Jönköping University, Sweden.

## Acknowledgements

This project was conducted in the context of architectural room classification for a building portfolio associated with Herenco.

---

*Exploring how deep learning can transform architectural image analysis.*
