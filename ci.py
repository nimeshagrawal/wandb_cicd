import wandb
print(wandb.__version__)
assert wandb.__version__ == '0.16.4', f'Expected version 0.16.4, but found {wandb.__version__}'
