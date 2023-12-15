import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, SubsetRandomSampler
from sklearn.model_selection import train_test_split
from src.entity.entity_config import ConfigPreprocess
class PreprocessComponent:
    def __init__(self, config_preprocess:ConfigPreprocess):
        self.config = config_preprocess
    
    def perform_augmentation(self):
        if self.config.Augmentation:
            train_transform = transforms.Compose([
                transforms.RandomResizedCrop(self.config.Image_Size[0]),
                transforms.RandomHorizontalFlip(p=0.5),
                transforms.RandomRotation(self.config.Rotation),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])])
        else:
            train_transform = transforms.Compose([
                transforms.Resize(tuple(self.config.Image_Size)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])])

        val_transform = transforms.Compose([
            transforms.Resize(tuple(self.config.Image_Size)),
            transforms.ToTensor(), 
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])])
        return [train_transform, val_transform]

    def split_train_test(self, t_data, v_data):
        total_indices= list(range(len(t_data)))
        t_indices, v_indices = train_test_split(total_indices, test_size=0.3)
        t_sampler = SubsetRandomSampler(t_indices)
        v_sampler = SubsetRandomSampler(v_indices)
        t_loader = DataLoader(dataset=t_data,
                                    batch_size=self.config.Batch_Size,
                                    sampler=t_sampler)
        
        v_loader = DataLoader(dataset=v_data,
                                    batch_size=self.config.Batch_Size,
                                    sampler=v_sampler)
        return t_loader, v_loader
    
    def load_data(self):
        transform_list = self.perform_augmentation()
 
        train_data = ImageFolder(self.config.data_folder, 
                    transform=transform_list[0])
        val_data = ImageFolder(self.config.data_folder, 
                               transform_list[1])
        return train_data, val_data

    def preprocess_data(self):
        """
        preprocessing steps:
        0. Load the data
        1. Augmentation
            - resizing the image to the required dimensions
            - Flipping the image 
            - Normalizing the image        
        2. Splitting the data into train-test split
        """
        t_data_transform, v_data_transform = self.load_data()
        t_loader, v_loader = self.split_train_test(t_data_transform, v_data_transform)
        return t_loader, v_loader