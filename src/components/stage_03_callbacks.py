import tensorflow as tf
from src.utils.common import create_dirs
import os
import time
class CALLBACKSCOMPONENT:
    
    def __init__(self, CALLBACKSENTITY):
        self.config = CALLBACKSENTITY
        create_dirs([self.config.root_dir, 
                     self.config.tensorboard_log_dir, 
                     os.path.dirname(self.config.checkpoint_file_path)])
        
    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_log_dir = os.path.join(self.config.tensorboard_log_dir,
                                  f"tb_logs_at{timestamp}")
        return tf.keras.callbacks.TensorBoard(log_dir=tb_log_dir)
    
    @property
    def _create_checkpoint_callback(self):
        return tf.keras.callbacks.ModelCheckpoint(self.config.checkpoint_file_path, 
                                                  save_best_only=True)
    
    def callbacks_list(self):
        return [self._create_tb_callbacks, self._create_checkpoint_callback]