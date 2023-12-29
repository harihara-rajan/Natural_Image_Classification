import tensorflow as tf
from src.utils.common import create_dirs
import os
class BaseModelGeneratorComponent:
    def __init__(self, BaseModelGeneratorEntity):
        self.config = BaseModelGeneratorEntity
    
    def load_base_model(self)-> tf.keras.Model:
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
        
