import argparse


def argpass():
    parser = argparse.ArgumentParser("ElbowAI ML Config")
    parser.add_argument("--epochs", '-e', type=int, default=100, help='Number of epochs')
    parser.add_argument("--lr", '-l', type=float, default=0.0001, help='Learning rate')
    parser.add_argument("--model", '-m', type=str, default="LR", help='Type of Model')
    parser.add_argument("--output", '-o', type=argparse.FileType('w'), help='Output of model config')
    parser.add_argument("--square", '-s', type=int, help='Show the square of a number')
    parser.add_argument("--filename", '-f', type=str, help='Filename to save to')
    parser.add_argument("--verbosity", '-v', type=int, choices=[0, 1, 2], help='Logging levels')
    args = parser.parse_args()
    return args