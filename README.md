# simple-md-converter
シンプルなマークダウン形式のテキストに整形もしくは変換を行う


## Installation

### リポジトリのクローン
```sh
git clone https://github.com/Mokuichi147/simple-md-converter.git
cd simple-md-converter
```

### Python環境のセットアップ
MacOS or Linux
```sh
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Windows
```pwsh
py -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Usage

```sh
python main.py <input_file> <output_file>
```


## Third party libraries

|LibraryName|License|
|-|-|
|fire|[Apache License 2.0](https://github.com/google/python-fire/blob/master/LICENSE)|
|python-markdownify|[MIT License](https://github.com/matthewwithanm/python-markdownify/blob/develop/LICENSE)|