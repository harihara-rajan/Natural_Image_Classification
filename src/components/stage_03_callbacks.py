import tensorflow as tf
from src.utils.common import create_dirs
import os
import time
class CALLBACKSCOMPONENT:
    """
    CALLBACKSCOMPONENT is a class designed for managing and creating callbacks commonly used in deep learning model training.
    It includes functionalities to create TensorBoard callbacks for monitoring training and create ModelCheckpoint callbacks
    for saving the best model during training.

    Attributes:
        config (CALLBACKSENTITY): An instance of CALLBACKSENTITY containing configuration parameters.
    
    Methods:
        __init__(self, CALLBACKSENTITY): Constructor method to initialize CALLBACKSCOMPONENT with a CALLBACKSENTITY.
        _create_tb_callbacks(self): Creates and returns a TensorBoard callback for monitoring training progress.
        _create_checkpoint_callback(self): Creates and returns a ModelCheckpoint callback for saving the best model.
        callbacks_list(self): Retrieves a list of commonly used callbacks for deep learning model training.

    Example Usage:
        # Instantiate CALLBACKSENTITY with necessary configuration parameters
        callbacks_entity = CALLBACKSENTITY(
            root_dir='path/to/root',
            tensorboard_log_dir='path/to/tensorboard/logs',
            checkpoint_file_path='path/to/checkpoint/file.h5'
        )

        # Instantiate CALLBACKSCOMPONENT with CALLBACKSENTITY
        callbacks_component = CALLBACKSCOMPONENT(callbacks_entity)

        # Get a list of commonly used callbacks
        callback_list = callbacks_component.callbacks_list()
    """
    def __init__(self, CALLBACKSENTITY):
        """
        Initializes CALLBACKSCOMPONENT with a given CALLBACKSENTITY.

        Args:
            CALLBACKSENTITY (CALLBACKSENTITY): An instance of CALLBACKSENTITY containing configuration parameters.
        """
        self.config = CALLBACKSENTITY
        create_dirs([self.config.root_dir, 
                     self.config.tensorboard_log_dir, 
                     os.path.dirname(self.config.checkpoint_file_path)])
        
    @property
    def _create_tb_callbacks(self):
        """
        Creates and returns a TensorBoard callback for monitoring training progress.

        Returns:
            tf.keras.callbacks.TensorBoard: TensorBoard callback.
        """
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_log_dir = os.path.join(self.config.tensorboard_log_dir,
                                  f"tb_logs_at{timestamp}")
        return tf.keras.callbacks.TensorBoard(log_dir=tb_log_dir)
    
    @property
    def _create_checkpoint_callback(self):
        """
        Creates and returns a ModelCheckpoint callback for saving the best model.

        Returns:
            tf.keras.callbacks.ModelCheckpoint: ModelCheckpoint callback.
        """
        return tf.keras.callbacks.ModelCheckpoint(self.config.checkpoint_file_path, 
                                                  save_best_only=True)
    
    def callbacks_list(self):
        """
        Retrieves a list of commonly used callbacks for deep learning model training.

        Returns:
            list: List of callbacks.
        """
        return [self._create_tb_callbacks, self._create_checkpoint_callback]