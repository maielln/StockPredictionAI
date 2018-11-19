# AI Stock Market Predictor

## Background
This is a tool to be used to predict the stock market. With a focus on blue chip tech stocks.

## Setup
The following pip packages are required:
- argparse -> `pip install argparse`
- requests -> `pip install requests`

## Running
There are two files that can be run in this project

### Trainer
This file is responsable for training and then saving the neural network data for use by the predictor. The trainer trains for a select group of blue chip tech stocks.

Runnable with: 
```
python train.py [time]
```

- `time` is the time frame that you will want to predict into the future. Example) 2 would be 2 days

### Predictor
This file is responsable for the prediction of individual stocks

Runnable with: 
```
python predictor.py [ticker] [time]
```

- `ticker` is the ticker symbol for the stock to be predicted. Example) MSFT would be for Microsoft

- `time` is the time frame that you will want to predict into the future. Example) 2 would be 2 days