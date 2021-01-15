[# Projeto 1: Modelo preditivo de preço de casas - Kaggle's Competition](https://github.com/camdsDS/Cesar_Portfolio/blob/main/HousePrices_from_Kaggle_RandomForestRegressor.ipynb)

* Modelo feito com Google Colab - Python.

* Para elaborar este modelo realizei:
	* Tratamento de dados:
		* Missing;
		* Transformação de dados categóricos em numéricos;
		* Normalização de dados.
	* Divisão da base de dados teste em subgrupo de desenvolvimento e subgrupo de validação (70% e 30%, respectivamente).
* Algoritmo usado: RandomForestRegressor com GridSearchCV.

[# Projeto 2: Modelo preditivo de sobreviventes do Titanic - Kaggle's Competition](https://github.com/camdsDS/Cesar_Portfolio/blob/main/Titanic_from_kaggle_GradientBoostingClassifier.ipynb)

* Modelo feito com Google Colab - Python.

* Para elaborar este modelo realizei:
	* Tratamento de dados:
		* Missing;
		* Outliers;
		* Inconsistentes;
		* Transformação de dados categóricos em numéricos (com get_dummies);
		* Normalização de dados (com MinMaxScaler).
	* Divisão da base de dados teste em subgrupo de desenvolvimento e subgrupo de validação (80% e 20%, respectivamente) - train_test_split.
	* Cross_validate para escolher o melhor modelo entre LogisticRegression, GradientBoostingClassifier e RandomForestClassifier.
	* GridSearchCV.
	* Score com roc_auc_score.
		* roc_score_desenv: 0.8993933939939339
		* roc_score_valid: 0.8033916269210387
	* Apresentação de gráfico (com seaborn) das variáveis utilizadas e os valores que representam respectivamente a importância delas no modelo.
* Algoritmo usado: GradientBoostingClassifier.
