# Fetch assessment (Bonus CI/CD implementation)

I would like to begin by expressing my gratitude for this coding challenge. I have put my abilities to the test in this challenge. I have devised the most adaptable and modular strategy possible to address this challenge. 

In addition to applying the MLops principle, I have implemented a comprehensive end-to-end solution for this issue utilizing the CI/CD infrastructure. Therefore, allow me to walk you through the code.

Prior to that, allow me to elucidate the reasoning that underpins my proposed solution.

![](https://github.com/SaiShashank12/fetch_assessment/blob/main/images/fetch-training.png)

# How to run?

# Please have internet connection

**Since the data is not included the git file** 
### Steps for docker
Clone the repository

```bash
git clone https://github.com/SaiShashank12/fetch_assessment.git
```
### Step 01- change the directory

```bash
cd fetch_assessment
```
### Step 02- Build the image

```bash
docker build -t fetch_assessment .
```
### Step 03- Run the image

```bash
docker run -d -p 8501:8501 fetch_assessment 
```

Now open browser to this address,

```bash
http://localhost:8501/
```

# Steps for AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 764611553403.dkr.ecr.us-east-1.amazonaws.com/forcast
	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

## Steps for without docker implementation

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n forcast python=3.8 -y
```

```bash
conda activate forcast
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


```bash
Author: Sai Shashank Mudliar
Data Scientist
Email: shashanksai@gmail.com

```


## Proposed Solution Overview and Rationalization

When I got hands on the data I had the did 4 basic steps in ML which are as follows:

1. **Exploratory Data Analysis:**
<br/>

- The first thing I did was to do intial analysis of the from that I go below graphs.
      
    ![images\EDA_graph1.png](https://github.com/SaiShashank12/fetch_assessment/blob/main/images/EDA_graph1.png)     
    
    ![EDA](https://github.com/SaiShashank12/fetch_assessment/blob/main/images/Eda2.png)

- In my analysis of the provided images, I observed:
        <br/>
  - **Trend Analysis**: The first image showed an upward trend in Receipt_Count over the year, indicating an average growth in receipt counts.
    - **Seasonal Decomposition**:
	- **Trend Component**: There was a clear upward trajectory, suggesting positive growth in the dataset.
	- **Seasonal Component**: Regular fluctuations were present but relatively small compared to the overall Receipt_Count.
	- **Residual Component**: The residuals were stable with no apparent patterns, indicating effective capture of the main series components.
   -For forecasting:
	  - **Trend Consideration**: I considered models like Holt-Winters or ARIMA to account for the upward trend.
	  - **Seasonality**: Given the seasonal fluctuations, I found a model like SARIMA or seasonal exponential smoothing advisable.
	  - **Model Simplicity**: The lack of patterns in residuals suggested that a simpler model might suffice.
</br>
- I approached forecasting with caution, mindful of potential overfitting, and validated the model using out-of-sample testing or cross-validation, considering we had only one seasonal cycle in the data.
</br>
2. **Feature Engineering**:
<br/>
	- Due to the fact that there was only one feature, I resolved to add the following:  
  		- Day
  - Month
  - Year
  - lag1: a day after the present (t+1)
  - lag2: a day after the present (t+2)
  - lag3: a day after the present (t+3)

- I had to scale the data down since I had decided to use NeuralNetwork for training.

- Utilizing time-series data, I constructed X and Y as follows: X represents data arranged in a predetermined sequence of days, and Y denotes the day following the set. The term for this set is "lookback set."


<br/>

3. **Model training**:
<br/>   
    - For the purpose of training model on the given data, I decided to use the following algorithm:
        - RNN
        - LSTM
        - LSTM-CNN
        - GRU-CNN
        - XGBoost

    - After training and Hyperamater tuning, I decieded to go with LSTM-CNN on the basis of erros and whether the models were overfitting or underfitting

    - As mentioned in the preceding section, overfitting of models is a possibility. To counter that circumstance, I employed:
        
        - Early stopping
        - Dropout layer
    
    - I also implemented Learning rate decay for better performance.
</br>

4. **Model Evaluating**:

    - For Evaluation purposes,  I chose Root Mean squared error(RMSE) which is good for Regression task like these.

## CI/CD pipeline:

   <p> I have also implemented CI/CD pipeline using github actions, AWS ECR(for storing the docker image) and EC2 for Deployment. So, whenever I do a commmit it is automatically deployed on EC2 instance.

   The implementation code is in .github\workflows\main.yaml . If you are interested in how does it work and also I have given instructions.
</p>

## Research:
 
<p>      This is the director where I have done most of the research work or implemented pipline code before it being modularized. It will also give you an idea of how the pipeline works.
</p>

## Artifacts:

<p>     This folder is created after code is run once. I have not included it in git since it a folder where Data and models are store. Something these data and models can be large which can cause problems when uploading to repositories. One more way was to use DVC but since data wasn't that big . So I droppe dthe plan.
</p>

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py


