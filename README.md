# Spec

The task at hand involves a set of CSV files stored in the dataset folder. Each file has a specific structure, as shown below:

```
time,open,high,low,close,volume,rsi
1609464600000,0.0047319,0.00475,0.0047189,0.00475,8315920.0,63.4633309356425
1609465500000,0.0047467,0.0047639,0.0047199,0.0047365,25398760.0,59.419527863771584
1609466400000,0.0047312,0.0047383,0.0047204,0.0047263,2457619.0,56.49069147000932
```

The objective is to train a model that can recognize a specific pattern referred to as the "climbing pattern":

![Climbing pattern](./docs/pattern.png)

The model's goal is to identify the safest place to predict an upward trend. By recognizing more accurate patterns, the model should improve its ability to predict upward trends.

# Structure
The dataset folder contains one file named DOGEUSDT.csv, which serves as a sample training dataset. If necessary, the model should be trained on the entire dataset within the folder. There is also a list of symbols that are currently commented out, potentially for future use.

The dataset includes the Relative Strength Index (RSI), which can be a helpful feature. Additionally, other technical indicators can be added if deemed necessary.

To generate more data, the create_dataset.py script can be executed.

# Training
The model should be saved to disk after training.

# prediction

The prediction specifications are outlined in predict.py:

* Retrieve the latest data for a given symbol.
* Predict the next 10 candles (if possible) and detect if an upward trend is present.

```python
def predict(dataset):
    # load the model from disk


    # calculate the result
    next10Candles = []
    trendIsUp = False
    return next10Candles, trendIsUp
```