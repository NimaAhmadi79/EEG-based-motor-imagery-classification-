# Model checkpoint

| File                  | Size   | What it is                                                      |
| --------------------- | ------ | --------------------------------------------------------------- |
| `model_checkpoint.h5` | ~4.4 MB | Best weights of the multi-branch SE-Net, saved by Keras during training (lowest validation loss). |

This is the trained Keras model from `main.ipynb`, saved via
`ModelCheckpoint("model_checkpoint.h5", monitor='val_loss', save_best_only=True)`.

## Loading it

The checkpoint stores the full model (architecture + weights), so you can load it
directly:

```python
import tensorflow as tf

model = tf.keras.models.load_model("models/model_checkpoint.h5")
model.summary()
```

The network has **three identical inputs**, so inference is run as:

```python
# x is an array of shape (n_samples, 1000, 22)
y_prob = model.predict([x, x, x])      # softmax over 4 classes
y_pred = y_prob.argmax(axis=1)         # 0=left hand, 1=right hand, 2=feet, 3=tongue
```

> **Note:** the notebook saves the checkpoint into its working directory as
> `model_checkpoint.h5`; the copy kept here under `models/` is that trained file. If you
> re-run training, point the `ModelCheckpoint` path at `models/` (or move the new file
> here) to keep the repository layout tidy.
