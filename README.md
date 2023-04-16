# data-factory

This repository contains source code of program used to generate `.caddo` files. Files taht are used in `tool` - which can be found in this organisation.

## 🔌 How to run

```
user@computer:~$ pip install caddo-data-factory
```

1) Implement sextraction function - you can find an example function here: link
2) Create settings.yaml file. All options that needs to be there are present in example settings file (link)

#### Implement extraction function, crete settings.yaml file and run from command line with settings file located in working directory
```
user@computer:~$python -m caddo_data_factory
```

#### Run from command line with custom path to settings file
```
user@computer:~$python -m caddo_data_factory --configuration {{relative_path_to_settings.yaml}}
```

## 📕 Any documentation?

Yes sure, please check our wiki for documentation
