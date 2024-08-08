import helpers
import numpy
from sklearn import linear_model
from sklearn.svm import SVC, NuSVC, LinearSVC

X_features = []
Y_features = []
rootdir = "Texts/"

labels = []
truth = open("truth.txt","r")
for line in truth:
    dataTruth = line.split()
    labels.append(dataTruth[1])
    
X_labels = labels[0:80]
Y_labels = labels[80:101] 

for i in range(1,81):
    # Get directory of the two text files
    knownDirs, unknownDirs = helpers.getDirs(i, rootdir)
    # Get sentence list of the text files
    knownSents = helpers.makeSentList(knownDirs)
    unknownSents = helpers.makeSentList(unknownDirs)
    # Calculate features out of the sentence list
    X_features.append(helpers.makeFeatures(knownSents, unknownSents))
    
for i in range(81,101):
    # Get directory of the two text files
    knownDirs, unknownDirs = helpers.getDirs(i, rootdir)
    # Get sentence list of the text files
    knownSents = helpers.makeSentList(knownDirs)
    unknownSents = helpers.makeSentList(unknownDirs)
    # Calculate features out of the sentence list
    Y_features.append(helpers.makeFeatures(knownSents, unknownSents))    
    
#maxent = linear_model.LogisticRegression()
#maxent.fit(X_features, X_labels)
#predict = maxent.predict(Y_features)

svc_clf = LinearSVC()
svc_clf.fit(X_features,X_labels)
predict_svc_dev = svc_clf.predict(Y_features)
predict_file = open('prediction.txt', 'w')
for prediction in predict_svc_dev:
    predict_file.write(prediction+"\n")

print "Done."