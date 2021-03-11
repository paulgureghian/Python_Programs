import ray
import torch
import torchvision.transforms as transforms

from ray.util.sgd.torch import TorchTrainer
from ray.util.sgd.torch import TrainingOperator
# https://github.com/kuangliu/pytorch-cifar/blob/master/models/resnet.py
from ray.util.sgd.torch.resnet import ResNet18
from torch.utils.data import DataLoader
from torchvision.datasets import CIFAR10

def cifar_creator(config):
    """Returns dataloaders to be used in `train` and `validate`."""
    tfms = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465),
                             (0.2023, 0.1994, 0.2010)),
    ])  # meanstd transformation
    train_loader = DataLoader(
        CIFAR10(root="~/data", download=True, transform=tfms), batch_size=config["batch"])
    validation_loader = DataLoader(
        CIFAR10(root="~/data", download=True, transform=tfms), batch_size=config["batch"])
    return train_loader, validation_loader

def optimizer_creator(model, config):
    """Returns an optimizer (or multiple)"""
    return torch.optim.SGD(model.parameters(), lr=config["lr"])

CustomTrainingOperator = TrainingOperator.from_creators(
    model_creator=ResNet18,  # A function that returns a nn.Module
    optimizer_creator=optimizer_creator,  # A function that returns an optimizer
    data_creator=cifar_creator,  # A function that returns dataloaders
    loss_creator=torch.nn.CrossEntropyLoss  # A loss function
)

ray.init()

trainer = TorchTrainer(
    training_operator_cls=CustomTrainingOperator,
    config={"lr": 0.01,  # used in optimizer_creator
            "batch": 64  # used in data_creator
            },
    num_workers=2,  # amount of parallelism
    use_gpu=torch.cuda.is_available(),
    use_tqdm=True)

stats = trainer.train()
print(trainer.validate())

torch.save(trainer.state_dict(), "checkpoint.pt")
trainer.shutdown()
print("success!")
