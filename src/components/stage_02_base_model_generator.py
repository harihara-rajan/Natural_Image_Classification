import tensorflow as tf
from src.utils.common import create_dirs
import os
class BaseModelGeneratorComponent:
    """
    BaseModelGeneratorComponent is a class designed for generating base and actual deep learning models using TensorFlow and Keras.
    It includes functionalities for loading a pre-trained base model, modifying it to create an actual model with customizable
    configurations, and saving the models.

    Attributes:
        config (BaseModelGeneratorEntity): An instance of BaseModelGeneratorEntity containing configuration parameters.

    Methods:
        __init__(self, BaseModelGeneratorEntity): Constructor method to initialize the BaseModelGeneratorComponent with a BaseModelGeneratorEntity.
        load_base_model(self) -> tf.keras.Model: Loads a pre-trained base model, compiles it, and saves it for future use.
        actual_model(self, classes, freeze_all, freeze_till, learning_rate) -> tf.keras.Model: Generates an actual model based on the
            loaded base model with customizable configurations, compiles it, and saves it.

    Example Usage:
        # Instantiate BaseModelGeneratorEntity with necessary configuration parameters
        generator_entity = BaseModelGeneratorEntity(
            base_model_path='path/to/base/model.h5',
            actual_model_path='path/to/actual/model.h5',
            IMAGE_SIZE=(224, 224),
            CLASSES=10
        )

        # Instantiate BaseModelGeneratorComponent with BaseModelGeneratorEntity
        generator_component = BaseModelGeneratorComponent(generator_entity)

        # Load the base model
        base_model = generator_component.load_base_model()

        # Generate an actual model with customized configurations
        actual_model = generator_component.actual_model(classes=10, freeze_all=True, freeze_till=0, learning_rate=0.001)
    """
    def __init__(self, BaseModelGeneratorEntity):
        """
        Initializes the BaseModelGeneratorComponent with a given BaseModelGeneratorEntity.

        Args:
            BaseModelGeneratorEntity (BaseModelGeneratorEntity): An instance of BaseModelGeneratorEntity containing configuration parameters.
        """
        self.config = BaseModelGeneratorEntity
    
    def load_base_model(self)-> tf.keras.Model:
        """
        Loads a pre-trained base model, compiles it, and saves it for future use.

        Returns:
            tf.keras.Model: Loaded and compiled base model.
        """
        #create dirs
        create_dirs([os.path.dirname(self.config.base_model_path)])
        #building base model
        model = tf.keras.applications.resnet_v2.ResNet152V2(
            include_top=False, 
            weights='imagenet',
            input_shape=(self.config.IMAGE_SIZE[0], self.config.IMAGE_SIZE[1], 3),
            classes= self.config.CLASSES
        )
        model.compile(
            optimizer='rmsprop', 
            loss='categorical_crossentropy', 
            metrics=['accuracy'])
        model.save(self.config.base_model_path)
        # model.save(self.config.base_model_path)
        return model
    # @staticmethod
    def actual_model(self, classes, freeze_all, freeze_till, learning_rate)-> tf.keras.Model:
        """
        Generates an actual model based on the loaded base model with customizable configurations,
        compiles it, and saves it.

        Args:
            classes (int): Number of output classes for the actual model.
            freeze_all (bool): Whether to freeze all layers of the base model.
            freeze_till (int): Number of layers to freeze from the end of the base model.
            learning_rate (float): Learning rate for the optimizer.

        Returns:
            tf.keras.Model: Generated and compiled actual model.
        """
        create_dirs([os.path.dirname(self.config.actual_model_path)])
        model = tf.keras.applications.resnet_v2.ResNet152V2(
            include_top=False, 
            weights='imagenet',
            input_shape=(self.config.IMAGE_SIZE[0], self.config.IMAGE_SIZE[1], 3),
            classes= self.config.CLASSES
        )
        if freeze_all:
            for _ in model.layers:
                model.trainable = False
        if freeze_till !=0:
            for _ in model.layers[:-freeze_till]:
                model.trainable = False
        flatten = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten)
        model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )
        model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )
        model.save(self.config.actual_model_path)
        model.summary()
        return model
        
