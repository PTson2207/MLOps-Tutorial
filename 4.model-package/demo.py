import hydra
from omegaconf import OmegaConf

@hydra.main(config_name="configs/basic.yaml")
def main(cfg):
    # Print the config file using `to_yaml` method which prints in a pretty manner
    print(OmegaConf.to_yaml(cfg))
    print(cfg.preferences.user)

if __name__ == "__main__":
    main()