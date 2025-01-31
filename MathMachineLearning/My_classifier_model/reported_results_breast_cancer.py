import numpy as np
from sklearn import datasets
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

# Load data
data = datasets.load_breast_cancer()
X = data.data
y = data.target

# Create report
report = []
report.append("BREAST CANCER DATASET - SIMPLE REPORT")
report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
report.append("-" * 50)

# Basic counts
n_patients = len(y)
n_malignant = sum(y == 0)
n_benign = sum(y == 1)

report.append("\nPATIENT COUNTS:")
report.append(f"Total Patients: {n_patients}")
report.append(f"Malignant (Cancer): {n_malignant}")
report.append(f"Benign (Not Cancer): {n_benign}")

# Top 5 measurements
report.append("\nKEY MEASUREMENTS:")
for i in range(5):
    feature_name = data.feature_names[i]
    avg_value = np.mean(X[:, i])
    report.append(f"{feature_name}: {avg_value:.2f}")

# Test different classifiers
classifiers = {
    'Random Forest': RandomForestClassifier(random_state=42),
    'SVM': SVC(random_state=42),
    'Neural Network': MLPClassifier(random_state=42),
    'KNN': KNeighborsClassifier()
}

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

report.append("\nMODEL PERFORMANCE:")
report.append("-" * 20)

best_accuracy = 0
best_classifier = None

for name, clf in classifiers.items():
    # Train and test
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test) * 100
    error = 100 - accuracy
    
    report.append(f"\n{name}:")
    report.append(f"Accuracy: {accuracy:.2f}%")
    report.append(f"Error Rate: {error:.2f}%")
    
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_classifier = name

report.append("\nBEST CLASSIFIER:")
report.append(f"{best_classifier} (Accuracy: {best_accuracy:.2f}%)")

# Save report
report_filename = 'simple_cancer_report.txt'
with open(report_filename, 'w') as f:
    f.write('\n'.join(report))

print(f"Report saved to {report_filename}")
print('\n'.join(report))