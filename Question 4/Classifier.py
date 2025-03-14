from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


def print_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Good', 'Bad'], yticklabels=['Good', 'Bad'])
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()


def predict_class(classifier, new_instance):
    prediction = classifier.predict([new_instance])
    return prediction[0]


def main():

    banana_file = 'C:\\Users\\Can\\PycharmProjects\\AI\\csv files\\banana_quality.csv'
    data = pd.read_csv(banana_file)

    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0, stratify=y)

    # Karar Ağacı modeli
    dtc_model = DecisionTreeClassifier(random_state=0)
    dtc_model.fit(X_train, y_train)

    # Destek Vektör Makinesi modeli
    svm_model = SVC(random_state=0)
    svm_model.fit(X_train, y_train)

    new_instance = [-2, 1, 1.5, 0.73, -0.34, 1.23, -1.2]

    dtc_prediction = predict_class(dtc_model, new_instance)
    svm_prediction = predict_class(svm_model, new_instance)

    print("DTC Classifier Prediction:", dtc_prediction)
    print("SVM Prediction:", svm_prediction)

    # DTC Classifier için 10 katlı çapraz doğrulama
    dtc_accuracy_scores = cross_val_score(dtc_model, X, y, cv=10, scoring='accuracy')
    dtc_precision_scores = cross_val_score(dtc_model, X, y, cv=10, scoring='precision_macro')
    dtc_recall_scores = cross_val_score(dtc_model, X, y, cv=10, scoring='recall_macro')

    # SVM için 10 katlı çapraz doğrulama
    svm_accuracy_scores = cross_val_score(svm_model, X, y, cv=10, scoring='accuracy')
    svm_precision_scores = cross_val_score(svm_model, X, y, cv=10, scoring='precision_macro')
    svm_recall_scores = cross_val_score(svm_model, X, y, cv=10, scoring='recall_macro')

    # Skorları yazdır
    print("\nDTC:")
    print("Accuracy:", np.mean(dtc_accuracy_scores))
    print("Precision:", np.mean(dtc_precision_scores))
    print("Recall:", np.mean(dtc_recall_scores))

    print("\nSVM:")
    print("Accuracy:", np.mean(svm_accuracy_scores))
    print("Precision:", np.mean(svm_precision_scores))
    print("Recall:", np.mean(svm_recall_scores))

    # Karışıklık matrislerini yazdır
    y_pred_dtc = dtc_model.predict(X_test)
    y_pred_svm = svm_model.predict(X_test)

    print_confusion_matrix(y_test, y_pred_dtc)
    print_confusion_matrix(y_test, y_pred_svm)


main()
