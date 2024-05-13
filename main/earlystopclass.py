from keras.callbacks import Callback

class EarlyStopAtAccuracy(Callback):
    def __init__(self, monitor='val_accuracy', target_accuracy=0.93, patience=0, verbose=0, mode='auto'):
        super(EarlyStopAtAccuracy, self).__init__()
        self.monitor = monitor
        self.target_accuracy = target_accuracy
        self.patience = patience
        self.verbose = verbose
        self.wait = 0
        self.stopped_epoch = 0
        self.mode = mode
        if mode == 'auto':
            if 'acc' in self.monitor:
                self.mode = 'max'
            else:
                self.mode = 'min'

    def on_epoch_end(self, epoch, logs=None):
        current_accuracy = logs.get(self.monitor)
        if current_accuracy is None:
            print("Early stopping requires %s available!" % self.monitor, 'WARNING')
            return

        if self.mode == 'max':
            improvement = (current_accuracy - self.target_accuracy) / self.target_accuracy
        else:
            improvement = (self.target_accuracy - current_accuracy) / self.target_accuracy

        if improvement >= 0:
            self.wait += 1
            if self.wait >= self.patience:
                self.stopped_epoch = epoch
                self.model.stop_training = True
                if self.verbose > 0:
                    print('Epoch %05d: early stopping at accuracy %.2f' % (epoch, self.target_accuracy))
        else:
            self.wait = 0