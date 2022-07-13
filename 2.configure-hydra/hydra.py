from omegaconf import OmegaConf

config = OmegaConf.load("configs/config.yaml")


print(config.preferences.user)
print(config["preferences"]["trait"])