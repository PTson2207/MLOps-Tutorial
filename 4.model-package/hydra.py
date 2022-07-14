from omegaconf import OmegaConf

config = OmegaConf.load("configs/basic.yaml")


print(config.preferences.user)
print(config["preferences"]["trait"])