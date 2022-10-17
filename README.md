### git create
```shell
gh repo create elbowcli -d "elbowcli argparser"  --public
git add .
git commit -m "first commit"
git branch -M main 
git remote add origin https://github.com/donwany/elbowcli.git
git push -u origin main
```
### Usage:
```shell
     elbowaicli \
     --epochs=200 \
     --lr=0.005 \
     --model="RandomForest" \
     --square=25 \
     --output=config.csv \
     --verbosity=2
     
python app.py \
    --epochs 200 \
    --lr 0.005 \
    --model "RandomForest" \
    --square 25 \
    --output config.csv \
    --verbosity 2
     
python app.py -e=200 -l=0.005 -m="RandomForest" -s=25 -o=config.csv -v=2 
python app.py -e 200 -l 0.005 -m "RandomForest" -s 25 -o config.csv -v 2
  
```