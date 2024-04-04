# Formal Way to process image
1. By default, image use np.uint8 as default type.
2. When processing, convert RGB channels into np.float32.
3. After processing, convert RGB channels back to np.uint8.
