from sklearn.metrics import accuracy_score, confusion_matrix

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 0]

accuracy = accuracy_score(y_true, y_pred)
cm = confusion_matrix(y_true, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(cm)
