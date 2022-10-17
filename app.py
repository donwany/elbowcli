# argparse, click,
import pandas as pd
from utils import argpass

if __name__ == '__main__':

    args = argpass()

    epoch = args.epochs
    learning_rate = args.lr
    model = args.model
    # logistic regression -> LOGISTIC REGRESSION
    if args.model:
        model = args.model.upper()

    # CREATE A DICTIONARY
    config = {"epochs": epoch, "learning_rate": learning_rate, "model": model}

    answer = args.square ** 2
    if args.verbosity == 1:
        print(f"The square of {args.square} == {answer}")
    elif args.verbosity == 2:
        print(f"{args.square}^2 == {answer}")

    if args.output is not None:
        pd.DataFrame.from_dict([config]).to_csv("config.csv", index=False, header=True)

    print(config)





