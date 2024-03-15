import wandb
print(wandb.__version__)
assert wandb.__version__ == '1.9.85', f'Expected version 1.9.85, but found {wandb.__version__}'
