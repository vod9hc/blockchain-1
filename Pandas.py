import pandas as pd

s = pd.DataFrame(
    {
        "Name": ["hallo","Hondo","Hollo",],
        "Age": [22, 33,  57],
        "Sex": ["male", "female", "male"],
    }
)

s = s.replace("hallo", "6aa", regex=False)
print(s)
