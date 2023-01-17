import wandb
print(f'The version of wandb is: {wandb.__version__}')
assert wandb.__version__ == '0.13.9', f'Expected version 0.13.9, but got {wandb.__version__}'
