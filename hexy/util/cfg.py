# -*- coding: utf-8 -*-
"""yaml based configuration, with a dotted access of configuration """
import flatdict
import yaml

cfg=flatdict.FlatDict()
cfg.set_delimiter('.')

#todo export yaml file:
config_yaml_file='./hexy_config.yaml'
cfg['util.cfg.yaml_config_file']=config_yaml_file


def read_config(yaml_cfg_file=config_yaml_file,default=cfg):
 with open(yaml_cfg_file) as yfile:
  ycfg = yaml.load(yfile)
  fcfg = flatdict.FlatDict(ycfg)
  fcfg.set_delimiter('.')
  return fcfg
 return cfg


def write_config(yaml_cfg_file=config_yaml_file,fcfg=cfg):
 ystr = yaml.dump(fcfg.as_dict(),
                  indent=4,
                  default_flow_style=False)
 with open(yaml_cfg_file, 'w') as yaml_file:
  res = yaml_file.write(ystr)
  return res
