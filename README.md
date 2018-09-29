# HumanActivityClassifier

## Objective
To build a model that classifies common human activities like walking,standing,laying on the basis of readings obtained from smartphone sensors.
## Dataset
Source: UCI ML Repository-
Human Activity Recognition Using Smartphones Data Set
https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones#
## Model
* Data was clean with no missing values or inconsistent data. It had 561 attributes so Principal Component Analysis(PCA) was used to reduce the dimension.
* Best results were obtained by taking about 200 principal components.
* Linear SVM("one vs one") was used to classify the data
## About Repository
* Activity_Classifier_Pre.py --- script to pickle data
* Activity_Classifier_Modelling.py --- classification script
* H_A_C pca.png -- image showing 2 principal components of the data
* Training_Development_Testing.png -- shows a plot of training, development and testing accuracies over number of principal components
## Results
* Training accuracy ~ 99%
* Development or cross-validation accuracy ~ 98%
* Testing accuracy ~ 95-96%
* Most mis-classifications were obtained for standing and sitting classes as there very little difference between the 2 postures.

## Future Scope
* Deep Learning can be used to further improve the model specially between standing and sitting.


