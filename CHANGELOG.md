# Changelog

The published version for this project is **version number 2**, but here is all the version and the performance of them.

| Version | Balanced / Unbalanced | Layers        | Kernels       | Total params | Runtime | Accuracy | F1-Score | Comments                                                                                       |
|---------|------------------------|---------------|---------------|--------------|---------|----------|----------|-------------------------------------------------------------------------------------------------|
| 1       | Unbalanced             | 32 - 64 - 128 | 3x3, 3x3, 3x3 | 33,508,817   | 209 min | 0.8329   | 0.8336   | Good result, though very large model file. Going to half the layers and see if the result will be the same and lesser size of the .h5-file |
| 2       | Unbalanced             | 16 - 32 - 64  | 3x3, 3x3, 3x3 | 8,378,609    | 124 min | 0.8258   | 0.8244   | Good result, almost the same result when decreasing the layers to the half of the first version. The model now are around 33Mb instead of over 130Mb with the first model |
| 3       | Unbalanced             | 16 - 32 - 64  | 5x5, 5x5, 5x5 | 7,274,993    | 156 min | 0.8167   | 0.8183   | Good result, almost identical even when increasing the kernel size. Still the largest confusion is between tulips and roses |
| 4       | Unbalanced             | 16 - 32 - 64  | 5x5, 5x5, 5x5 | 223,729      | 55 min  | 0.7087   | 0.6998   | Tried GlobalAveragePooling2D instead of Flatten on this layer and it didn´t go so well. Changing back to Flatten for the next version and increasing the layers. |
| 5       | Unbalanced             | 32 - 64 - 64  | 5x5, 5x5, 5x5 | 14,627,857   | 347 min | 0.7021   | 0.6819   | Adjust the augmentation with this model and the performance decreased instead. Will try next time with a balanced version 2. See if the performance of that can increase |
| 6       | Balanced (Undersampled)| 16 - 32 - 64  | 3x3, 3x3, 3x3 | 8,379,505    | 68 min  | 0.3536   | 0.2851   | Poor result when undersampled the categories. Settings where the same as the best performance at version 2. Ran with BatchNormalization() that made a poor result |
| 7       | Balanced (Oversampled) | 16 - 32 - 64  | 3x3, 3x3, 3x3 | 8,378,609    | 129 min | 0.8193   | 0.8189   | Deleted BatchNormalization in every layer and got a result very similar to version 2. Seems like oversampling didn´t do that much to the performance. |
