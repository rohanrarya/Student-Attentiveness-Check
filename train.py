import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv("student_attentiveness_data_clean.csv")

# print(df.head())

num_col = ["phone_uses_hrs","attendance_percent","study_hrs"]

target = "attentive"


le = LabelEncoder()
df["talkative"] = le.fit_transform(df["talkative"])
df["eye_contact"] = le.fit_transform(df["eye_contact"])
df[target] = le.fit_transform(df[target])

x = df.drop(columns="attentive")
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)


scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)



model = LogisticRegression()
model.fit(x_train_scaled,y_train)
predict = model.predict(x_test)


    
print(f"Accuracy : {accuracy_score(y_test,predict)* 100}% ")


