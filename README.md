[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/camdsDS)](https://github.com/camdsDS)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/camds/)](https://www.linkedin.com/in/camds/)

[# Projeto 1: Automação na elaboração e no envio de emails personalizados - relatórios personalizados para serem enviados automaticamente por professores para pais de alunos](https://github.com/camdsDS/Cesar_Portfolio/blob/main/Email_personalizado_com_relat%C3%B3rio_autom%C3%A1tico.ipynb)

* Automação.
* Código em Python.

* Envia automaticamente por email (gmail), a partir de uma planilha de excel com notas de alunos, um relatório personalizado para cada responsável de cada aluno. Os emails são todos disparados ao mesmo tempo. Segue um exemplo de email: [imagem](https://github.com/camdsDS/Cesar_Portfolio/blob/main/Exemplo_email.jpg)

 ![](https://github.com/camdsDS/Cesar_Portfolio/blob/main/Exemplo_email.jpg)


# Projetos de Machine Learning

[# Projeto_ML 1: Modelo preditivo da probabilidade de um motorista acionar o seguro de automóvel no próximo ano - Kaggle's Competition](https://github.com/camdsDS/Cesar_Portfolio/blob/main/Porto_Seguro_kaggle.ipynb)
 
* [Link](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction) para o desafio do kaggle - Porto Seguro’s Safe Driver Prediction (Predict if a driver will file an insurance claim next year). 
* Algoritmo de classificação (GradientBoostingClassifier com GridSearchCV).
* Código em Python.

* Bibliotecas usadas:
	* pandas;
	* numpy;
	* matplotlib.pyplot;
	* scikit-learn;
* Para elaborar este modelo realizei:
	* Tratamento de dados:
		* Missing (com SimpleImputer - strategy='mean');
		* Divisão do dafaframe principal de acordo com o tipo de dado: binário, categórico de alta cardinalidade, categórico de baixa cardinalidade e numérico. 
		* Transformação de dados categóricos em numéricos (LabelEncoder e get_dummies);
		* Normalização de dados (MinMaxScaler).
	* Relatório com as colunas de maior concentração de valores missing.
	* Gráfico com a bad rate.
	* Divisão da base de dados teste em subgrupo de desenvolvimento e subgrupo de validação (70% e 30%, respectivamente) (train_test_split).
	* Gráfico da curva ROC de desenvolvimento e validação do modelo.
	* Score de desenvolvimento e validação do modelo usando Acurácia, Gini e Área Curva ROC.
	* Tabela com a importância das variáveis.
	* Teste de modelo novo dropando as variáveis menos importantes.	

[# Projeto_ML 2: Modelo preditivo de preço de casas - Kaggle's Competition](https://github.com/camdsDS/Cesar_Portfolio/blob/main/HousePrices_from_Kaggle_RandomForestRegressor.ipynb)

* [Link](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) para o desafio do kaggle. House Prices - Advanced Regression Techniques (Predict sales prices and practice feature engineering, RFs, and gradient boosting).
* Algoritmo de regressão (RandomForestRegressor com GridSearchCV).
* Código em Python.

 Bibliotecas usadas:
	* pandas;
	* numpy;
	* scikit-learn;
* Para elaborar este modelo realizei:
	* Tratamento de dados:
		* Missing;
		* Transformação de dados categóricos em numéricos (get_dummies);
		* Normalização de dados (MinMaxScaler).
	* Score: mean_squared_error
	* Divisão da base de dados teste em subgrupo de desenvolvimento e subgrupo de validação (70% e 30%, respectivamente) (train_test_split).

[# Projeto_ML 3: Modelo preditivo de sobreviventes do Titanic - Kaggle's Competition](https://github.com/camdsDS/Cesar_Portfolio/blob/main/Titanic_from_kaggle_GradientBoostingClassifier.ipynb)

* [Link](https://www.kaggle.com/c/titanic) para o desafio do kaggle. Titanic - Machine Learning from Disaster (Start here! Predict survival on the Titanic and get familiar with ML basics).
* Algoritmo de classificação.
* Código em Python.

* Bibliotecas usadas:
	* pandas;
	* numpy;
	* seaborn;
	* scikit-learn;
* Para elaborar este modelo realizei:
	* Tratamento de dados:
		* Missing;
		* Outliers;
		* Inconsistentes;
		* Transformação de dados categóricos em numéricos (com get_dummies);
		* Normalização de dados (com MinMaxScaler).
	* Divisão da base de dados teste em subgrupo de desenvolvimento e subgrupo de validação (80% e 20%, respectivamente) (train_test_split).
	* Matriz de confusão.
	* Cross_validate para escolher o melhor modelo entre LogisticRegression, GradientBoostingClassifier e RandomForestClassifier.
	* Score: acurácia.
	* Apresentação de gráfico (com seaborn) das variáveis utilizadas e os valores que representam respectivamente a importância delas no modelo.
* Algoritmo usado: GradientBoostingClassifier com GridSearchCV.

[# Projeto_ML 4: Modelo para clusterização de clientes de um shopping](https://github.com/camdsDS/Cesar_Portfolio/blob/main/Mall_Customers_K_Means_clustering.ipynb)

* Algoritmo de clusterização.
* Código em Python.

* Os dados do dataset usado para elaborar este modelo são do curso "Machine Learning A-Z™: Hands-On Python & R In Data Science" da Udemy.

* Para elaborar este modelo realizei:
	* Elbow method para encontrar a melhor quantidade de clusters.
* Algoritmo usado: K-Means Clustering.
