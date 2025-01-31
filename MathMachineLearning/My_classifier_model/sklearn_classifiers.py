#=====================================================================
# Required: X, y, multi_run [dataname, rtrain, run, CompEnsm]
#=====================================================================
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import VotingClassifier

#-----------------------------------------------
classifiers = [
    LogisticRegression(max_iter = 1000),
    KNeighborsClassifier(5),
    SVC(kernel="linear", C=0.5),
    SVC(gamma=2, C=1),
    RandomForestClassifier(max_depth=5, n_estimators=50, max_features=1),
    MLPClassifier(hidden_layer_sizes=[100], activation='logistic',
                  alpha=0.5, max_iter=1000),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
    GaussianProcessClassifier(),
]
names = [
    "Logistic-Regr",
    "KNeighbors-5 ",
    "SVC-Linear   ",
    "SVC-RBF      ",
    "Random-Forest",
    "MLPClassifier",
    "AdaBoost     ",
    "Naive-Bayes  ",
    "QDA          ",
    "Gaussian-Proc",
]
#-----------------------------------------------
if dataname is None: dataname = 'No-dataname';
if run      is None: run      = 50;
if rtrain   is None: rtrain   = 0.7e0;
if CompEnsm is None: CompEnsm = 2;

#=====================================================================
print('====== Comparision: Scikit-learn Classifiers =================')
#=====================================================================
import os;
acc_max=0; Acc_CLF = np.zeros([len(classifiers),1]);

for k, (name, clf) in enumerate(zip(names, classifiers)):
    accmean, acc_std, etime = multi_run(clf,X,y,rtrain,run)

    Acc_CLF[k] = accmean
    if accmean>acc_max: acc_max,algname = accmean,name
    print('%s: %s: Acc.(mean,std) = (%.2f,%.2f)%%; E-time= %.5f'
        %(os.path.basename(dataname),name,accmean,acc_std,etime/run))
print('--------------------------------------------------------------')
print('sklearn classifiers Acc: (mean,max) = (%.2f,%.2f)%%; Best = %s'
      %(np.mean(Acc_CLF),acc_max,algname))

if CompEnsm <2: quit()
#=====================================================================
print('====== Ensembling: SKlearn Classifiers =======================')
#=====================================================================
names = [x.rstrip() for x in names]
popped_clf = []
popped_clf.append(names.pop(9)); classifiers.pop(9);  #Gaussian Proc
popped_clf.append(names.pop(7)); classifiers.pop(7);  #Naive Bayes
popped_clf.append(names.pop(6)); classifiers.pop(6);  #AdaBoost
popped_clf.append(names.pop(4)); classifiers.pop(4);  #Random Forest
popped_clf.append(names.pop(0)); classifiers.pop(0);  #Logistic Regr
#print('popped_clf=',popped_clf[::-1])

CLFs = [(name, clf) for name, clf in zip(names, classifiers)]
#if 'MyCLF' in locals(): CLFs += [('MyCLF',MyCLF())]
EnCLF = VotingClassifier(estimators=CLFs, voting='hard')
accmean, acc_std, etime = multi_run(EnCLF,X,y,rtrain,run)

print('EnCLF =',[lis[0] for lis in CLFs])
print('%s: Ensemble CLFs: Acc.(mean,std) = (%.2f,%.2f)%%; E-time= %.5f'
       %(os.path.basename(dataname),accmean,acc_std,etime/run))
