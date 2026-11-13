# Methodology — Architectural Blueprint Room Classification

## 1. Project Objective

The objective of this project was to investigate deep learning techniques for automatically classifying architectural blueprint images into different room categories.

Two approaches were implemented and compared:

- BlueprintCNN — a custom Convolutional Neural Network trained from scratch.
- EfficientNetB0 — a pretrained convolutional neural network adapted through transfer learning and fine-tuning.

The objective was to understand how different model architectures perform when classifying room images from previously unseen building projects.

## 2. Dataset Exploration

The dataset used in the notebook contains:

- Total images: 1,517
- Number of room categories: 19
- Image format: PNG
- Building projects: 20

The dataset was organised by building and room category. Initial exploration involved examining image distribution and identifying the number of samples available for each room category.

## 3. Dataset Splitting

To evaluate how well the models generalise to unseen buildings, the dataset was divided at building-project level rather than randomly splitting individual images.

| Dataset | Buildings | Images |
|---|---:|---:|
| Training | 14 | 1,060 |
| Validation | 3 | 223 |
| Testing | 3 | 234 |

The split was approximately 70/15/15 by building projects.

This approach was used to reduce the risk of data leakage between training, validation and test datasets.

A fixed random seed was used for reproducibility.

## 4. Image Preprocessing

Image preprocessing was implemented before feeding images into the deep learning models.

The preprocessing pipeline included:

1. Converting images into RGB format.
2. Padding images with a white background to create square dimensions while preserving aspect ratio.
3. Resizing images to 224 × 224 pixels.
4. Applying Contrast Limited Adaptive Histogram Equalization (CLAHE) to improve image contrast.
5. Converting the processed images into arrays suitable for model input.

## 5. Data Augmentation

Albumentations was used to introduce variations into training images.

The implemented transformations included:

- Horizontal flipping.
- Vertical flipping.
- Random 90-degree rotation.
- Shifting, scaling and rotation.
- Sharpening and unsharp masking.
- Random brightness and contrast adjustments.
- Grid dropout.

Separate transformation pipelines were used for training and validation/testing. Validation and test images were not subjected to random training augmentation.

Different normalization settings were used for the custom CNN and EfficientNetB0.

## 6. Model Development

### 6.1 BlueprintCNN — Custom CNN

A custom CNN architecture was developed and trained from random initialization.

The architecture consisted of four convolutional blocks with increasing filter sizes:

- Block 1: 32 filters
- Block 2: 64 filters
- Block 3: 128 filters
- Block 4: 256 filters

Each block included convolutional layers, batch normalization, ReLU activation, max pooling and dropout.

Global average pooling was used before the final classification layers.

This model served as the baseline for comparison.

### 6.2 EfficientNetB0 — Transfer Learning

EfficientNetB0 pretrained on ImageNet was selected to investigate transfer learning.

A custom classification head was added to adapt the pretrained model to the room classification task.

Training was performed in two phases.

**Phase 1 — Feature Extraction**

- The pretrained backbone was frozen.
- The newly added classification head was trained.
- Learning rate: 0.001.
- Maximum epochs: 20.

**Phase 2 — Fine-Tuning**

- The last 30 backbone layers were unfrozen.
- The model was fine-tuned using a smaller learning rate.
- Learning rate: 0.00002.
- Maximum epochs: 20.

This approach allowed the pretrained model to adapt its learned features to the architectural image classification task.

## 7. Handling Class Imbalance

The dataset contained different numbers of images for different room categories.

Two approaches were implemented:

- Class-weighted CrossEntropyLoss to assign greater importance to underrepresented classes.
- WeightedRandomSampler to increase the sampling probability of minority classes during training.

These methods were used to address uneven class distribution.

## 8. Model Training

Both models were trained using PyTorch.

The notebook used the following training configuration:

| Parameter | Value |
|---|---|
| Image size | 224 × 224 |
| Batch size | 8 |
| Optimizer | Adam |
| Weight decay | 0.0001 |
| Maximum epochs | 20 per training phase |
| Early stopping patience | 8 |
| Learning rate scheduler | ReduceLROnPlateau |
| Hardware | GPU through Google Colab |

The best validation-loss checkpoint was restored after training.

## 9. Model Evaluation

Both models were evaluated on the same held-out test dataset containing images from three unseen buildings.

The evaluation included:

- Test accuracy.
- Weighted F1-score.
- Precision and recall.
- Classification reports.
- Confusion matrix analysis.
- Comparison between the two model architectures.

## 10. Overall Approach

The methodology followed a structured machine learning workflow:

1. Dataset exploration.
2. Image preprocessing.
3. Dataset splitting at building level.
4. Data augmentation.
5. Custom CNN implementation.
6. EfficientNetB0 transfer learning.
7. Model fine-tuning.
8. Evaluation and comparison.

The experiments provided an opportunity to investigate the benefits and limitations of training a CNN from scratch compared with adapting a pretrained model.

---

*This document describes the methodology implemented in the project notebook. It is intended as technical documentation of the experimental workflow.*
