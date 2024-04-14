import joblib
loaded_recommend = joblib.load('src/model.joblib')

print(loaded_recommend("avatar"))  