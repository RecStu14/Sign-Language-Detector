# Try 1 

## Hyperparameters

1. Optimizer - Adam
2. Learning Rate - 0.001
3. Batch Size - 32
4. Epochs - 20

## Observations
During the training process from the 3rd epoch onwards, it can be seen that the training accuracy is higher than the validation accuracy. This gap between the training accuracy and the validation accuracy just keeps on increasing as the model trains. 

From the 13th epoch onwards, the training accuracy is 100% however the validation accuracy is around 70% which means that the model is just blindly memorising the train data instead of learning features from it and applying it to predict on the validation data. This could be the case of **overfitting** where the model memorises the data too well and is unable to work accurately on unseen data.

## Possible Solutions to Combat Overfitting
1. Increase Regularisation
2. Train with more data - can be generated from data augmentation, in this case try resizing the images as the dataset already contains images that have been flipped from right to left and vice versa.
3. Try Reducing the Learning Rate - try 0.0001