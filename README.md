# keras2onnx
Package for the automatic conversion between .h5 models to .onnx

## Prerequisites
1. tensorflow
2. tf2onnx

## Install

Clone this repository: 
```
git clone https://github.com/alesof/keras2onnx.git
```

Install tf2onnx:
```
pip install -U tf2onnx
pip install onnx==1.14.1
```
*Note*: onnx 1.14.1 is necessary as tf2onnx install the 1.15 version which is not currently supported


## How to convert .h5 model to .onnx

1. Convert .h5 model to .pb model:
```
python keras2pb.py <path-to-model.h5> --verbose
```

2. Convert .pb in .onnx:
```
python -m tf2onnx.convert --saved-model <path-to-generated-pb-model> --output <output-path\model-name.onnx>
```

*Note* keras2pb.py can also be launched in silent mode without --verbose 
